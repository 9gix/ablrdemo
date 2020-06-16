from django.contrib.auth.models import User
from myinfo.client import MyInfoClient
from myinfo.security import get_decoded_access_token, get_decrypted_person_data


class GovSGAuthBackend:

    def _sanitize_data(self, raw):
        return {
            'uinfin': raw['uinfin']['value'],
            'sex': raw['sex']['desc'],
            'race': raw['race']['desc'],
            'nationality': raw['nationality']['desc'],
            'dob': raw['dob']['value'],
            'mobile': raw['mobileno']['nbr']['value'],
            'housetype': raw['housingtype']['desc'],
            'address_block': raw['regadd']['block']['value'],
            'address_street': raw['regadd']['street']['value'],
            'address_unit': raw['regadd']['unit']['value'],
            'address_floor': raw['regadd']['floor']['value'],
            'address_building': raw['regadd']['building']['value'],
            'postal': raw['regadd']['postal']['value'],
        }

    def _create_user_profile(self, data):
        user = User.objects.create_user(
            username=data['uinfin']['value'],
            first_name=data['name']['value'],
            email=data['email']['value'])

        profile = user.profile
        for attr, value in self._sanitize_data(data).items():
            setattr(profile, attr, value)
        profile.save()
        return user

    def authenticate(self, request, code=None):
        client = MyInfoClient()
        resp = client.get_access_token(code)
        access_token = resp["access_token"]
        # Decoding access token
        decoded_access_token = get_decoded_access_token(access_token)
        
        resp = client.get_person(uinfin=decoded_access_token["sub"], access_token=access_token)
        data = get_decrypted_person_data(resp)
        if data:
            try:
                user = User.objects.get(username=data['uinfin']['value'])
            except User.DoesNotExist:
                # Getting person data
                user = self._create_user_profile(data)

            return user
        return None


    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None