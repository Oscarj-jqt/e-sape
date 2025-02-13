import React from "react";
import "./Panier.css"

const Panier = () => {
    return (
        <div className="container">
          <div className="cart">
            <div className="cart-header">
              <h1>Votre Panier</h1>
            </div>
    
            <div className="cart-item">
              <img
                className="product-image"
                src="https://i.imgur.com/XiFJkhI.jpg"
                alt="Basic T-shirt"
              />
              <div className="product-details">
                <span className="bold">Basic T-shirt</span>
                <div className="product-desc">
                  <div className="size">
                    <span className="text-grey">Size:</span>
                    <span className="bold"> M</span>
                  </div>
                  <div className="color">
                    <span className="text-grey">Color:</span>
                    <span className="bold"> Grey</span>
                  </div>
                </div>
              </div>
    
              <div className="quantity">
                <h5 className="text-grey">2</h5>
              </div>
    
              <div className="price">
                <h5 className="text-grey">$20.00</h5>
              </div>
    
              <div className="remove">
                <button>Delete</button>
              </div>
            </div>
          </div>
        </div>
      );
}

export default Panier 