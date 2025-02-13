import React from "react";
import { Routes, Route } from "react-router-dom";
import Nav from "./components/Nav";
import Home from "./components/Home";
<<<<<<< HEAD
import Shop from "./components/Shop";
=======
import Login from "./components/Login";
import Register from "./components/Register";
import Footer from "./components/Footer";
import Panier from "./components/Panier";
import Affichage from "./components/Affichage";
>>>>>>> main

const App = () => {
  return (
    <div className="app-container">
      <Nav />
      <main>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
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
