import {React} from 'react';
import './Home.css';

const Home = () => {
  // État pour stocker les produits récupérés
  const [products, setProducts] = useState([]);

  // Fonction pour effectuer la requête GET GraphQL pour récupérer les produits
  useEffect(() => {
    // Requête GET GraphQL pour obtenir les produits
    fetch("http://localhost:5000/graphql", {
      method: "POST",  // Bien que ce soit un GET, GraphQL nécessite toujours une méthode POST
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        query: `
          query {
            products {
              id
              name
              price
            }
          }
        `
      })
    })
    .then(response => response.json())
    .then(data => {
      // Mettre à jour l'état avec les produits récupérés
      setProducts(data.data.products);
    })
    .catch(error => {
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
