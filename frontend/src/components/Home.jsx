import React from 'react';
import './Home.css';


const Home = () => {
    return (
      <main className="App">

        <section className="hero">
          <h2>Bienvenue sur notre boutique en ligne</h2>
          <p>Découvrez les meilleures offres et produits tendances !</p>
          <button className="shop-now">Shoppez Maintenant</button>
        </section>
  
        <section className="products">
          <div className="product-list">
            <div className="product">
              <img src="" alt="Produit 1" />
              <h3>Produit 1</h3>
              <p>Prix: 1.800€</p>
              <button>Afficher le produit</button>
            </div>
            <div className="product">
              <img src="" alt="Produit 2" />
              <h3>Produit 2</h3>
              <p>Prix: 1.500€</p>
              <button>Afficher le produit</button>
            </div>
            <div className="product">
              <img src="" alt="Produit 3" />
              <h3>Produit 3</h3>
              <p>Prix: 2.500€</p>
              <button>Afficher le produit</button>
            </div>
          </div>
        </section>
    </main>
    );
  }


export default Home;