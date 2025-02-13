import React from "react";

const Register = () => {
    return (
        <div>
            <form className="register">
                <h1>Welcome</h1>
                <p>Let's create your account !</p>

                <label for="username">Username</label>
                <input type="email" placeholder="email" id="username" className="input"/>

                <label for="password">Password</label>
                <input type="password" placeholder="password" id="password" className="input"/>

                <label for="password">Confirmation Password</label>
                <input type="password" placeholder="confirmation password" id="password" className="input"/>

                <button className="log">Register</button>
            </form>
        </div>
    )
}

export default Register; 