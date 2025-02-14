import React from "react";
import "./Affichage.css"
import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";
import axios from "axios";


const Affichage = () => {

    const [products, setProducts] = useState([]); // État pour stocker les produits
    const { productId } = useParams();

    useEffect(() => {
        axios
          .get(`http://localhost:5000/products/${productId}`) // Appel à l’API Flask
          .then((response) => {
            console.log("Données reçues :", response.data);
            setProducts(response.data.products); // Met à jour l’état avec les produits
          })
          .catch((error) => {
            console.error("Erreur lors de la récupération des produits:", error);
          });
      }, [productId]);

      if (!products) {
        return <p>Chargement ...</p>;
      }

    return (
        <main className="affichage">

            <section className="gauche">
            <img src ={products.image} alt="Veste" className="photo" width="500px"></img>
            </section>

            <section className="droite">
                <h1>{products.name}</h1>

                <p>{products.description}</p>

                <p className="prix">{products.price}€</p>

                <button className="shop-now">Ajoutez au panier</button> 
            </section>
        </main>
    )
}

export default Affichage;