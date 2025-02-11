import React from "react";
import "./Nav.css";

const Nav = () => {
    return (
        <header>
            <h1>Issape</h1>
            <nav>
                <a href="#">Panier</a>
                <a href="#">Catalogue</a>
                <a href="#">Login</a>
                <input type="text" placeholder="Issape" />
            </nav>
        </header>
    )
}

export default Nav;