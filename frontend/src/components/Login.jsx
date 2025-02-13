import React, { useState } from "react";
import axios from "axios"; 
import "./Login.css";

const Login = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [errorMessage, setErrorMessage] = useState(""); 

    const handleSubmit = async (e) => {
        e.preventDefault();
        console.log("Username:", username);
        console.log("Password:", password);

        try {
            const response = await axios.post("http://localhost:5000/login", {
                username,
                password,
            });

            // Si la connexion est réussie, récupérer le token JWT
            localStorage.setItem("token", response.data.access_token); 
            console.log("Login successful");

            // Rediriger l'utilisateur ou effectuer une action après la connexion réussie
        } catch (error) {
            console.error("Login failed:", error);
            setErrorMessage("Bad username or password"); 
        }
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
                    onChange={(e) => setUsername(e.target.value)}
                    aria-label="Email"
                />

                <label htmlFor="password">Password</label>
                <input
                    type="password"
                    placeholder="Password"
                    id="password"
                    className="input"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    aria-label="Mot de passe"
                />

                <button type="submit" className="log">Log In</button>

                {errorMessage && <p className="error">{errorMessage}</p>} {/* Affiche l'erreur si nécessaire */}
            </form>
        </div>
    );
};

export default Login;
