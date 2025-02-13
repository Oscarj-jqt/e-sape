import React from "react";
import { useState } from "react";
import "./Login.css"

const Login = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault(); 
        console.log("Username:", username);
        console.log("Password:", password);
    };
    return (
        <div className="App">
             <form onSubmit={handleSubmit}>
                <h1>Login</h1>

                <label htmlFor="username">Username</label>
                <input
                    type="text"
                    placeholder="Email"
                    id="username"
                    className="input"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)} // Met à jour l'état
                    aria-label="Email"
                />

                <label htmlFor="password">Password</label>
                <input
                    type="password"
                    placeholder="Password"
                    id="password"
                    className="input"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)} // Met à jour l'état
                    aria-label="Mot de passe"
                />

                <button type="submit" className="log">Log In</button>
            </form>
            
        </div>
    )
}

export default Login;