import React from "react";
import "./Nav.css";

const Nav = () => {
    return (
        <header>
            <div className="header-left">
                <h1>E-sape</h1>
            </div>
            <nav className="header-center">
                <a href="#">Lorem</a>
                <a href="#">Lorem</a>
                <a href="#">Lorem</a>
            </nav>
            <div className="header-right">
                <input type="text" placeholder="Rechercher" />
                <button>Panier</button>
                <button>Connexion</button>
            </div>
        </header>
    )
}

export default Nav;
