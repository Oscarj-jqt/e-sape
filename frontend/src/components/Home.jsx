import React, { useEffect, useState } from "react";
import "./Home.css";
import axios from "axios"; // Assure-toi d'avoir installé axios avec npm install axios
import { useNavigate } from "react-router-dom";

const Home = () => {
  const [products, setProducts] = useState([]); // État pour stocker les produits
  const navigate = useNavigate();

  useEffect(() => {
    axios
      .get("http://localhost:5000/products") // Appel à l’API Flask
      .then((response) => {
        setProducts(response.data.products); // Met à jour l’état avec les produits
      })
      .catch((error) => {
        console.error("Erreur lors de la récupération des produits:", error);
      });
  }, []);

  return (
    <main className="App">
      <section className="hero">
        <h2>Bienvenue sur notre boutique en ligne</h2>
        <p>Découvrez les meilleures offres et produits tendances !</p>
        <button className="shop-now">Shoppez Maintenant</button>
      </section>

      <section className="products">
        <div className="product-list">
          {products.length > 0 ? (
            products.map((product) => (
              <div className="product" key={product._id}>
                <h3>{product.name}</h3>
                <img src={product.image} alt={product.name} />
                <p>Prix: {product.price}€</p>
                <button onClick={() => navigate(`/affichage/${product._id}`)}>
                  Afficher le produit
                </button>
              </div>
            ))
          ) : (
            <p>Chargement des produits...</p>
          )}
        </div>
      </section>
    </main>
  );
};

export default Home;