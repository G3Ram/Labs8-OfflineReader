import React, { Component } from 'react';
import { Route } from 'react-router-dom';
import { SignInPage, SignUpPage } from '../';

class App extends Component {
	render() {
		return (
			<div className="App">
				<h1>Anywhere Reader</h1>
				{/* <SignInPage />
        <SignUpPage /> */}
				<Route path="/signIn" component={SignInPage} />
				<Route path="/signUp" component={SignUpPage} />
			</div>
		);
	}
}

export default App;
