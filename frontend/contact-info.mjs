import React from 'react'
import ReactDOM from 'react-dom'

class ContactInfo extends React.Component {
	render(){
		let contact_info = this.props.initialData;
		return (
			<div>
				<form>
					<h2>Contact Info</h2>
					<dl>
						<dt>Mobile Number</dt>
						<dd>{ contact_info['mobile'] }</dd>

						<label for="email">Email Address</label><br/>
						<input value={ contact_info['email'] } id='email' />
					</dl>
					<h2> Registered Address</h2>
					<dl>
						<dt>Block Number</dt>
						<dd>{ contact_info['address_block'] }</dd>

						<dt>Street Name</dt>
						<dd>{ contact_info['address_street'] }</dd>

						<dt>Building</dt>
						<dd>{ contact_info['address_building'] }</dd>

						<dt>Floor</dt>
						<dd>{ contact_info['address_floor'] } - { contact_info['address_unit'] }</dd>

						<dt>Postal</dt>
						<dd>{ contact_info['postal'] }</dd>

						<dt>Type of housing</dt>
						<dd>{ contact_info['housetype'] }</dd>
					</dl>
					<button>Continue</button>
				</form>
			</div>
		)
	}
}


ReactDOM.render(
	<ContactInfo initialData={window.initialData} />,
	document.getElementById('main')
)