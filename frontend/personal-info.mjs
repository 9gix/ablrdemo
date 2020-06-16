import React from 'react'
import ReactDOM from 'react-dom'

class PersonalInfo extends React.Component {
	render(){
		let personal_info = this.props.initialData;
		return (
			<div>
				<h2>Personal Info</h2>
				<dl>
					<dt>NRIC/FIN</dt>
					<dd>{ personal_info['uinfin'] }</dd>

					<dt>Principal Name</dt>
					<dd>{ personal_info['name'] }</dd>

					<dt>Sex</dt>
					<dd>{ personal_info['sex'] }</dd>

					<dt>Date of Birth</dt>
					<dd>{ personal_info['dob'] }</dd>

					<dt>Nationality</dt>
					<dd>{ personal_info['nationality'] }</dd>

					<dt>Race</dt>
					<dd>{ personal_info['race'] }</dd>
				</dl>
			</div>
		)
	}
}


ReactDOM.render(
	<PersonalInfo initialData={window.initialData} />,
	document.getElementById('main')
)