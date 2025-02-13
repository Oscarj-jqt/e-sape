import React from "react";
import { Routes, Route } from "react-router-dom";
import Nav from "./components/Nav";
import Home from "./components/Home";
import Login from "./components/Login";
import Register from "./components/Register";
import Footer from "./components/Footer";
import Panier from "./components/Panier";
import Affichage from "./components/Affichage";
import Admin from "./components/Admin";

const App = () => {
  return (
    <div className="app-container">
      <Nav />
      <main>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/admin" element={<Admin />} />
          <Route path="/register" element={<Register />} />
          <Route path="/panier" element={<Panier />} />
          <Route path="/affichage" element={<Affichage />} />
        </Routes>
      </main>
      <Footer />
    </div>
  );
};

export default App;
