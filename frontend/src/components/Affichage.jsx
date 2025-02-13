import React from "react";
import "./Affichage.css"

const Affichage = () => {
    return (
        <main className="affichage">

            <section class="gauche">
            <img src ="louis-vuitton-blouson-varsity-brode--HPL66ECAW622_PM2_Front view.jpg.webp" alt="Veste" className="photo" width="500px"></img>
            </section>

            <section class="droite">
                <h1>Veste Louis Vuitton</h1>

                <p>Pièce indispensable de la garde-robe, cette veste trucker classique témoigne du savoir-faire Louis Vuitton. Elle est fabriquée en denim japonais de première qualité, délavé à la pierre, avec des surpiqûres couleur tabac, une broderie LV sur la poche de poitrine, un patch LV en nubuck au dos et des boutons façon perles. Ce modèle s'associe aisément aux tenues de tous les jours.</p>

                <p class="prix">1.200€</p>

                <button class="shop-now">Ajoutez au panier</button> 
            </section>
        </main>
    )
}

export default Affichage;