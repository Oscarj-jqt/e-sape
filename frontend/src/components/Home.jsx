import {React, useEffect, useState} from 'react';
import axios from "axios";
import './Home.css';

const Home = () => {
  
  // État pour stocker les produits récupérés
  const [products, setProducts] = useState([]);

  // Fonction pour effectuer la requête GET GraphQL pour récupérer les produits
  useEffect(() => {
    fetch("http://127.0.0.1:5000/products")  // Assure-toi que l'URL est correcte
      .then((response) => response.json())
      .then((data) => {
        console.log(data); // Vérifie les données dans la console
        setProducts(data); // Mettre à jour l'état avec les données
      })
      .catch((error) => console.error("Error fetching products:", error));
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
              <div className="product" key={product.id}>
                {/* Afficher l'image, utiliser une image par défaut si nécessaire */}
                <img src={`https://via.placeholder.com/150?text=${product.name}`} alt={product.name} />
                <h3>{product.name}</h3>
                <p>Prix: {product.price}€</p>
                <button>Afficher le produit</button>
              </div>
            ))
          ) : (
            <p>Aucun produit disponible.</p>
          )}
        </div>
      </section>
    </main>
  );
}

export default Home;
