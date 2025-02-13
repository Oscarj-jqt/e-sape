import React from "react";
import { Link, useNavigate } from "react-router-dom";
import "./Nav.css";

const Nav = () => {
    const navigate = useNavigate();

    return (
        
        <header>
            <div className="header-left">
                <h1>E-sape</h1>
            </div>
            <nav className="header-center">
                <Link to="/">Accueil</Link>
                <Link to="/shop">Boutique</Link>
                <Link to="/contact">Contact</Link>
            </nav>
            <div className="header-right">
                <input type="text" placeholder="Rechercher" />
                <button>Panier</button>
                <button onClick={() => navigate("/Login")} aria-label="Se connecter">Connexion</button>
            </div>
        </header>
    )
}

export default Nav;
