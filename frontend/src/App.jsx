import {React} from "react";
import Nav from "./components/Nav";
import Home from "./components/Home";
import Login from "./components/Login";
import Register from "./components/Register";
import Footer from "./components/Footer";
import "./index.css"
const App = () => {
    return (
        <div className="app-container">
            <Nav />
            <main>
                <Home />
            </main>
            <Footer/>
        </div>
    )
}

export default App;