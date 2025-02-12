import {React} from "react";
import Nav from "./components/Nav";
import Home from "./components/Home";
import Login from "./components/Login";
import "./index.css"
const App = () => {
    return (
        <div>
            <Nav />
            <Login />
        </div>
    )
}

export default App;