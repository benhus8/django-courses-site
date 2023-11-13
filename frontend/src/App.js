import React from 'react';
import './App.css'
import Navbar from "./components/Navbar";
import Account from "./views/Account";
import {Route, Routes, Link} from 'react-router-dom';

function App() {
    return (

        <div className="App">
            {/*<Navbar/>*/}
            <div>
                    <Routes>
                        <Route exact path="" element={<Navbar/>}/>
                        <Route exact path="/account" element={<Account/>}/>
                        <Route exact path="shop" element={<Account/>}/>
                    </Routes>
            </div>
        </div>

    );
}

export default App;
