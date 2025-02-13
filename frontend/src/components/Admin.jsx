import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

const Admin = () => {
    const [products, setProducts] = useState([]);
    const [newProduct, setNewProduct] = useState({ name: "", price: "" });
    const navigate = useNavigate();

    // Vérification du token (Accès restreint)
    useEffect(() => {
        const token = localStorage.getItem("token");
        if (!token) {
            console.log("Accès refusé, redirection vers /");
            navigate("/");
        } else {
            fetchProducts();
        }
    }, [navigate]);

    // Récupération des produits depuis l'API Flask
    const fetchProducts = async () => {
        try {
            const response = await axios.get("http://localhost:5000/products");
            setProducts(response.data.products);
        } catch (error) {
            console.error("Erreur lors de la récupération des produits :", error);
        }
    };

    // Ajout d’un nouveau produit
    const handleAddProduct = async () => {
        if (!newProduct.name || !newProduct.price) return;
        try {
            await axios.post("http://localhost:5000/products", newProduct);
            setNewProduct({ name: "", price: "" });
            fetchProducts(); // Rafraîchir la liste
        } catch (error) {
            console.error("Erreur lors de l'ajout du produit :", error);
        }
    };

    // Suppression d’un produit
    const handleDeleteProduct = async (id) => {
        try {
            await axios.delete(`http://localhost:5000/products/${id}`);
            fetchProducts(); // Rafraîchir la liste
        } catch (error) {
            console.error("Erreur lors de la suppression du produit :", error);
        }
    };

    return (
        <div>
            <h2>Admin Panel</h2>
            <h3>Ajouter un produit</h3>
            <input
                type="text"
                placeholder="Nom du produit"
                value={newProduct.name}
                onChange={(e) => setNewProduct({ ...newProduct, name: e.target.value })}
            />
            <input
                type="number"
                placeholder="Prix"
                value={newProduct.price}
                onChange={(e) => setNewProduct({ ...newProduct, price: e.target.value })}
            />
            <button onClick={handleAddProduct}>Ajouter</button>

            <h3>Liste des produits</h3>
            <ul>
                {products.map((product) => (
                    <li key={product._id}>
                        {product.name} - {product.price}€
                        <button onClick={() => handleDeleteProduct(product._id)}>Supprimer</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Admin;
