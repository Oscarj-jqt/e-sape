import React from "react";
import "./Login.css"

const Login = () => {
    return (
        <div className="App">
            <form>
                <h1>Login</h1>

                <label for="username">Username</label>
                <input type="text" placeholder="Email" id="username" className="input"/>

                <label for="password">Password</label>
                <input type="password" placeholder="Password" id="password" className="input"/>

                <button className="log">Log In</button>
            </form>
            
        </div>
    )
}

export default Login;