import React, { useEffect, useState } from 'react';

const Shop = () => {
    const [courses, setCourses] = useState([]);
    const [error, setError] = useState(null);
    const [purchased, setPurchased] = useState(false);
    const [csrfToken, setCsrfToken] = useState('');


    useEffect(async () => {

        const fetchCourses = async () => {
            try {
                const response = await fetch('/api/get_available_courses/');
                if (!response.ok) {
                    throw new Error('Failed to fetch courses');
                }
                const data = await response.json();
                setCourses(data);
            } catch (error) {
                console.error('Error fetching available courses:', error);
                setError('Failed to fetch courses. Please try again.');
            }
        };
        fetchCourses();

        const fetchCsrfToken = async () => {
            try {
                const response = await fetch('/api/csrf_cookie/');
                if (!response.ok) {
                    throw new Error('Failed to fetch CSRF token');
                }
                // Pobierz CSRF token z ciasteczek odpowiedzi
                const csrfToken = response.headers.get('csrftoken');
                setCsrfToken(csrfToken);
            } catch (error) {
                console.error('Error fetching CSRF token:', error);
            }
        };
        fetchCsrfToken();
    }, []);

    useEffect(() => {
        if (purchased) {
            const timer = setTimeout(() => {
                setPurchased(false);
                window.location.reload(); // Przeładuj stronę
            }, 3000);

            return () => clearTimeout(timer);
        }
    }, [purchased]);

    const handlePurchase = async (courseId) => {
        try {
            const response = await fetch('/api/add_course_to_user/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': document.cookie.match(/csrftoken=([^ ;]+)/)[1]
                },
                body: JSON.stringify({
                    courseId: courseId,
                }),
            });
            if (response.ok) {
                setPurchased(true);
                setTimeout(() => {
                    setPurchased(false);
                }, 3000);// Wyświetl komunikat przez 3 sekundy
            } else {
                setPurchased(false);
            }
        } catch (error) {
            console.error('Error adding course:', error);
        }
    };

    return (
        <div className="container mt-5">
            <h5 className="mb-4">Available Courses</h5>
            <hr />
            {error && <div>Error: {error}</div>}
            {purchased && <div className="alert alert-success">Course added successfully!</div>}
            {courses.length === 0 && !error && <div>No courses available</div>}
            {courses.length > 0 && (
                <div className="row">
                    {courses.map(course => (
                        <div className="col-md-4 mb-3" key={course.course_id}>
                            <div className="card">
                                <div className="card-body">
                                    <h5 className="card-title">{course.description}</h5>
                                    <p className="card-text">Duration: {course.access_duration} days</p>
                                    <p className="card-text">Net price: {course.net_amount} PLN</p>
                                    <p className="card-text">Total price: {course.total_price} PLN</p>
                                    <p className="card-text">Language: {course.language_cd}</p>
                                    <button
                                        className="btn btn-primary"
                                        onClick={() => {
                                            handlePurchase(course.course_id)
                                        }}
                                    >
                                        Purchase
                                    </button>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
};

export default Shop;
