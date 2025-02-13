import React, { useState, useEffect } from "react";
import axios from "axios";

const Admin = () => {
    const [products, setProducts] = useState([]);
    const [name, setName] = useState("");
    const [price, setPrice] = useState("");
    const [description, setDescription] = useState("");
    const [image, setImage] = useState("");
    const [editId, setEditId] = useState(null);
    const [message, setMessage] = useState("");

    // Récupérer le token
    const token = localStorage.getItem("token");

    // Charger les produits
    useEffect(() => {
        fetchProducts();
    }, []);

    const fetchProducts = async () => {
        try {
            const response = await axios.get("http://localhost:5000/products");
            setProducts(response.data.products);
        } catch (error) {
            console.error("Erreur lors du chargement des produits", error);
        }
    };

    // Ajouter un produit
    const addProduct = async () => {
        try {
            const response = await axios.post(
                "http://localhost:5000/admin/products",
                { name, price, description, image },
                { headers: { Authorization: `Bearer ${token}` } }
            );
            setMessage(response.data.msg);
            fetchProducts();
        } catch (error) {
            setMessage(error.response?.data?.msg || "Erreur lors de l'ajout");
        }
    };

    // Modifier un produit
    const updateProduct = async () => {
        try {
            const response = await axios.put(
                "http://localhost:5000/admin/products",
                { id: editId, name, price, description, image },
                { headers: { Authorization: `Bearer ${token}` } }
            );
            setMessage(response.data.msg);
            fetchProducts();
            setEditId(null); // Réinitialiser après modification
        } catch (error) {
            setMessage(error.response?.data?.msg || "Erreur lors de la modification");
        }
    };

    // Supprimer un produit
    const deleteProduct = async (id) => {
        try {
            const response = await axios.delete(
                "http://localhost:5000/admin/products",
                {
                    headers: { Authorization: `Bearer ${token}` },
                    data: { id }, // On met l'id dans le body
                }
            );
            setMessage(response.data.msg);
            fetchProducts();
        } catch (error) {
            setMessage(error.response?.data?.msg || "Erreur lors de la suppression");
        }
    };

    return (
        <div>
            <h1>Admin - Gestion des produits</h1>

            {message && <p>{message}</p>}

            <div>
                <h2>{editId ? "Modifier le produit" : "Ajouter un produit"}</h2>
                <input type="text" placeholder="Nom" value={name} onChange={(e) => setName(e.target.value)} />
                <input type="number" placeholder="Prix" value={price} onChange={(e) => setPrice(e.target.value)} />
                <input type="text" placeholder="Description" value={description} onChange={(e) => setDescription(e.target.value)} />
                <input type="text" placeholder="Image URL" value={image} onChange={(e) => setImage(e.target.value)} />
                <button onClick={editId ? updateProduct : addProduct}>{editId ? "Modifier" : "Ajouter"}</button>
            </div>

            <h2>Liste des produits</h2>
            <ul>
                {products.map((product) => (
                    <li key={product._id}>
                        {product.name} - {product.price}€
                        <button onClick={() => {
                            setEditId(product._id);
                            setName(product.name);
                            setPrice(product.price);
                            setDescription(product.description);
                            setImage(product.image);
                        }}>Modifier</button>
                        <button onClick={() => deleteProduct(product._id)}>Supprimer</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Admin;
