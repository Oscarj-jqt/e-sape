import React from "react";
import { Routes, Route } from "react-router-dom";
import Home from "./Home";
import Login from "./Login";
import Register from "./Register";
import Panier from "./Panier";
import Affichage from "./Affichage";

const AppRouter = () => {
    return (
        <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
            <Route path="/panier" element={<Panier />} />
            <Route path="/affichage" element={<Affichage />} />
        </Routes>
    );
};

export default AppRouter;
