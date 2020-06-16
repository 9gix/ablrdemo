import React from 'react'

class IncomeInfo extends React.Component {
	render(){
		return (
			<div>
				<h2>Income Info</h2>
				Not Implemented Yet
			</div>
		)
	}
}


ReactDOM.render(
	<IncomeInfo initialData={window.initialData} />,
	document.getElementById('main')
)