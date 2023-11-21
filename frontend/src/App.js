import React from 'react';
import './App.css'
import Navbar from "./components/Navbar";
import Account from "./views/Account";
import {Route, Routes} from 'react-router-dom';
import Register from "./views/Register";
import Shop from "./views/Shop";
import MyCourses from "./views/MyCourses";
import Details from "./views/Details";
function App() {
    return (

        <div className="App">
            <div>
                <Navbar/>
            </div>
            <div>
                <Routes>
                    <Route exact path="" element={<Shop/>}/>
                    <Route exact path="my-courses" element={<MyCourses/>}/>
                    <Route exact path="account" element={<Account/>}/>
                    <Route exact path="shop" element={<Shop/>}/>
                    <Route exact path="register" element={<Register/>}/>
                    <Route exact path="details/:courseId" element={<Details/>}/>
                    />
                </Routes>
            </div>
        </div>

    );
}

export default App;
