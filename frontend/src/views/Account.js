import React, {useEffect, useState} from 'react';
import {Link, useNavigate} from "react-router-dom";

const Account = () => {
    const [userData, setUserData] = useState(null);
    const navigate = useNavigate();
    useEffect(() => {
        const fetchUserData = async () => {
            try {
                const response = await fetch('/api/get_user_data/');
                const data = await response.json();
                setUserData(data);
            } catch (error) {
                console.error('Error fetching user data:', error);
            }
        };
        fetchUserData();
    }, []);
    const handleEditDataClick = () => {
        // Navigate to the "/edit-user-data" route when the button is clicked
        navigate('/edit-user-data');
        window.location.reload();
    };
    return (
        <div className="container mt-5 flex">

            <div className="d-flex justify-content-between align-items-center mb-4">
                <h5>User Data</h5>
                <button type="submit" className="btn btn-primary"
                        onClick={handleEditDataClick}>Edit Data</button>
            </div>
            <hr></hr>
            {userData && (
                <div className="card">
                    <div className="card-body">
                        <div className="row">
                            <div className="col-sm-3">
                                <h6 className="mb-0">Username</h6>
                            </div>
                            <div className="col-sm-9">
                                <p className="text-muted mb-0">{userData.username}</p>
                            </div>
                        </div>
                        <hr></hr>
                        <div className="row">
                            <div className="col-sm-3">
                                <p className="mb-0">First name</p>
                            </div>
                            <div className="col-sm-9">
                                <p className="text-muted mb-0">{userData.first_name}</p>
                            </div>
                        </div>
                        <hr></hr>
                        <div className="row">
                            <div className="col-sm-3">
                                <p className="mb-0">Last name</p>
                            </div>
                            <div className="col-sm-9">
                                <p className="text-muted mb-0">{userData.last_name}</p>
                            </div>
                        </div>
                        <hr></hr>
                        <div className="row">
                            <div className="col-sm-3">
                                <p className="mb-0">Email</p>
                            </div>
                            <div className="col-sm-9">
                                <p className="text-muted mb-0">{userData.email}</p>
                            </div>
                        </div>
                        <hr></hr>
                        <div className="row">
                            <div className="col-sm-3">
                                <p className="mb-0">Birthday</p>
                            </div>
                            <div className="col-sm-9">
                                <p className="text-muted mb-0">{userData.birthday}</p>
                            </div>
                        </div>
                        <hr></hr>
                        <div className="row">
                            <div className="col-sm-3">
                                <p className="mb-0">Phone Number</p>
                            </div>
                            <div className="col-sm-9">
                                <p className="text-muted mb-0">{userData.phone_number}</p>
                            </div>
                        </div>
                        <hr></hr>
                        <div className="row">
                            <div className="col-sm-3">
                                <p className="mb-0">Address</p>
                            </div>
                            <div className="col-sm-9">
                                <p className="text-muted mb-0">{userData.address}</p>
                            </div>
                        </div>
                        <hr></hr>
                        <div className="row">
                            <div className="col-sm-3">
                                <p className="mb-0">Building Number</p>
                            </div>
                            <div className="col-sm-9">
                                <p className="text-muted mb-0">{userData.building_number}</p>
                            </div>
                        </div>
                        <hr></hr>
                        <div className="row">
                            <div className="col-sm-3">
                                <p className="mb-0">Postal Code</p>
                            </div>
                            <div className="col-sm-9">
                                <p className="text-muted mb-0">{userData.postal_code}</p>
                            </div>
                        </div>
                        <hr></hr>
                        <div className="row">
                            <div className="col-sm-3">
                                <p className="mb-0">City</p>
                            </div>
                            <div className="col-sm-9">
                                <p className="text-muted mb-0">{userData.city}</p>
                            </div>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
};

export default Account;