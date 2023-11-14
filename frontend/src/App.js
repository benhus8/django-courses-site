import React from 'react';
import './App.css'
import Navbar from "./components/Navbar";
import Account from "./views/Account";
import {Route, Routes} from 'react-router-dom';
import Register from "./views/Register";
import Shop from "./views/Shop";

function App() {
    return (

        <div className="App">
            <div>
                <Navbar/>
            </div>
            <div>
                <Routes>
                    <Route exact path="" element={<Account/>}/>
                    <Route exact path="account" element={<Account/>}/>
                    <Route exact path="shop" element={<Shop/>}/>
                    <Route exact path="register" element={<Register/>}/>
                    />
                </Routes>
            </div>
        </div>

    );
}

export default App;
