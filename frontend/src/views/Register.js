import React, {useEffect, useState} from 'react';
import {useNavigate} from 'react-router-dom';

const Register = ({mode}) => {
    const navigate = useNavigate();
    const [errors, setErrors] = useState(null);
    const [message, setMessage] = useState(null);
    const [userData, setUserData] = useState(null);


    const [formData, setFormData] = useState({
        username: '',
        first_name: '',
        last_name: '',
        email: '',
        password1: '',
        password2: '',
        birthday: '',
        phone_number: '',
        address: '',
        building_number: '',
        postal_code: '',
        city: '',
    });
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
        fetchUserData()
    }, []);

    useEffect(() => {
        if (userData) {
            setFormData({
                username: userData.username,
                first_name: userData.first_name,
                last_name: userData.last_name,
                email: userData.email,
                birthday: userData.birthday,
                phone_number: userData.phone_number,
                address: userData.address,
                building_number: userData.building_number,
                postal_code: userData.postal_code,
                city: userData.city,
            })
        }
    }, [userData]);

    const [csrfToken, setCsrfToken] = useState('');
    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value,
        });
    };
    const invalidForm = (formData) => {
        return formData.password1.length < 8 ||
            formData.password2 !== formData.password1
    };
    const handleSubmit = async (e) => {
        e.preventDefault();
        const fetchCsrfToken = async () => {
            try {
                const response = await fetch('/api/csrf_cookie/');
                if (!response.ok) {
                    throw new Error('Failed to fetch CSRF token');
                }

                const csrfToken = response.headers.get('csrftoken');
                setCsrfToken(csrfToken);
            } catch (error) {
                console.error('Error fetching CSRF token:', error);
            }
        };
        fetchCsrfToken();

        if (mode === 'add') {
            try {
                const response = await fetch('/api/register', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrfToken
                    },
                    body: JSON.stringify(formData),
                });
                if (response.ok) {
                    const data = await response.json();
                    setMessage(data.message)
                    navigate('/login/')
                    window.location.reload(false);
                } else {
                    const data = await response.json();
                    setErrors(data.errors);
                }
            } catch (error) {
                console.error('Some problems in registration process:', error);
            }
        } else {
            formData.password1 = undefined
            formData.password2 = undefined
            try {
                const response = await fetch('/api/edit-user-data', {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': document.cookie.match(/csrftoken=([^ ;]+)/)[1]
                    },
                    body: JSON.stringify(formData),
                });
                if (response.ok) {
                    const data = await response.json();
                    setMessage(data.message)
                    navigate('/account')
                    window.location.reload();
                } else {
                    const data = await response.json();
                    setErrors(data.errors);
                }
            } catch (error) {
                console.error('Some problems in registration process:', error);
            }
        }
    };

    return (
        <div className="container mt-5">
            {mode === 'add' ? (<h1>Registration</h1>) : (<h1>Edit data</h1>)}
            <form onSubmit={handleSubmit}>
                <div className="card">
                    <div className="card-body">
                        <div className="row">
                            <div className="col-6">
                                <div className="mb-3">
                                    <label htmlFor="username" className="form-label">Username:</label>
                                    <input
                                        type="text"
                                        className="form-control"
                                        id="username"
                                        name="username"
                                        value={formData.username}
                                        onChange={handleChange}
                                        required
                                    />
                                </div>
                            </div>

                            <div className="col-6">
                                <div className="mb-3">
                                    <label htmlFor="first_name" className="form-label">First Name:</label>
                                    <input
                                        type="text"
                                        className="form-control"
                                        id="first_name"
                                        name="first_name"
                                        value={formData.first_name}
                                        onChange={handleChange}
                                        required
                                    />
                                </div>
                            </div>
                        </div>
                        <div className="row">
                            <div className="col-6">
                                <div className="mb-3">
                                    <label htmlFor="last_name" className="form-label">Last Name:</label>
                                    <input
                                        type="text"
                                        className="form-control"
                                        id="last_name"
                                        name="last_name"
                                        value={formData.last_name}
                                        onChange={handleChange}
                                        required
                                    />
                                </div>
                            </div>
                            <div className="col-6">
                                <div className="mb-3">
                                    <label htmlFor="email" className="form-label">Email:</label>
                                    <input
                                        type="text"
                                        className="form-control"
                                        id="email"
                                        name="email"
                                        value={formData.email}
                                        onChange={handleChange}
                                        required
                                    />
                                </div>
                            </div>
                        </div>
                        <div className="row">
                            <div className="col-6">
                                <div className="mb-3">
                                    <label htmlFor="birthday" className="form-label">Birthday:</label>
                                    <input
                                        type="date"
                                        className="form-control"
                                        id="birthday"
                                        name="birthday"
                                        value={formData.birthday}
                                        onChange={handleChange}
                                        required
                                    />
                                </div>
                            </div>
                            <div className="col-6">
                                <div className="mb-3">
                                    <label htmlFor="phone_number" className="form-label">Phone number:</label>
                                    <input
                                        type="text"
                                        className="form-control"
                                        id="phone_number"
                                        name="phone_number"
                                        value={formData.phone_number}
                                        onChange={handleChange}
                                        required
                                    />
                                </div>
                            </div>
                        </div>
                        <div className="row">
                            <div className="col-6">
                                <div className="mb-3">
                                    <label htmlFor="address" className="form-label">Address:</label>
                                    <input
                                        type="text"
                                        className="form-control"
                                        id="address"
                                        name="address"
                                        value={formData.address}
                                        onChange={handleChange}
                                        required
                                    />
                                </div>
                            </div>
                            <div className="col-6">
                                <div className="mb-3">
                                    <label htmlFor="building_number" className="form-label">Building Number:</label>
                                    <input
                                        type="text"
                                        className="form-control"
                                        id="building_number"
                                        name="building_number"
                                        value={formData.building_number}
                                        onChange={handleChange}
                                        required
                                    />
                                </div>
                            </div>
                        </div>
                        <div className="row">
                            <div className="col-6">
                                <div className="mb-3">
                                    <label htmlFor="postal_code" className="form-label">Postal code:</label>
                                    <input
                                        type="postal"
                                        className="form-control"
                                        id="postal_code"
                                        name="postal_code"
                                        value={formData.postal_code}
                                        onChange={handleChange}
                                        required
                                    />
                                </div>
                            </div>
                            <div className="col-6">
                                <div className="mb-3">
                                    <label htmlFor="city" className="form-label">City:</label>
                                    <input
                                        type="text"
                                        className="form-control"
                                        id="city"
                                        name="city"
                                        value={formData.city}
                                        onChange={handleChange}
                                        required
                                    />
                                </div>
                            </div>
                        </div>
                        {mode === 'add' ? (
                            <div className="row">
                                <div className="col-6">
                                    <div className="mb-3">
                                        <label htmlFor="password" className="form-label">Password:</label>
                                        <input
                                            type="password"
                                            className="form-control"
                                            id="password1"
                                            name="password1"
                                            value={formData.password1}
                                            onChange={handleChange}
                                            required
                                        />
                                        {formData.password1.length > 0 && formData.password1.length < 8 && (
                                            <div className="text-danger">This password is too short. It must contain at
                                                least 8
                                                characters</div>
                                        )}
                                    </div>
                                </div>
                                <div className="col-6">
                                    <div className="mb-3">
                                        <label htmlFor="confirmPassword" className="form-label">Confirm
                                            Password:</label>
                                        <input
                                            type="password"
                                            className="form-control"
                                            id="password2"
                                            name="password2"
                                            value={formData.password2}
                                            onChange={handleChange}
                                            required
                                        />
                                        {formData.password2 !== formData.password1 && (
                                            <div className="text-danger">Confirmed password and password field must be
                                                the
                                                same</div>
                                        )}
                                    </div>
                                </div>
                            </div>
                        ) : null}
                        <div className="row">
                            <div className="col-6">
                                {mode === 'add' ?
                                    (<button type="submit" className="btn btn-primary"
                                             disabled={invalidForm(formData)}>Register
                                    </button>) :
                                    (<button type="submit" className="btn btn-primary">
                                        Edit
                                    </button>)}
                            </div>

                        </div>
                    </div>
                </div>

            </form>
            {errors && (
                <div className="text-danger">
                    {Object.values(errors).map((error, index) => (
                        <p key={index}>{error}</p>
                    ))}
                </div>
            )}

            {message && <div className="text-success">{message}</div>}
        </div>
    );
};

export default Register;