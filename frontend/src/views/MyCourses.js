import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

const MyCourses = () => {
    const [userCourses, setUserCourses] = useState([]);
    const [error, setError] = useState(null);
    const navigate = useNavigate();
    const [csrfToken, setCsrfToken] = useState('');

    useEffect(() => {

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
        const fetchUserCourses = async () => {
            try {
                const response = await fetch('/api/get_user_courses/');
                if (!response.ok) {
                    throw new Error('Failed to fetch user courses');
                }
                const data = await response.json();
                setUserCourses(data);
            } catch (error) {
                console.error('Error fetching user courses:', error);
                setError('Failed to fetch user courses. Please try again.');
            }
        };
        fetchUserCourses();
    }, []);

    const handleDetails = (courseId) => {
         navigate(`/details/${courseId}`);
    };

    const handleDelete = async (courseId) => {
        const confirmDelete = window.confirm('Are you sure you want to delete this course?');
        if (confirmDelete) {
            try {
                const response = await fetch('/api/delete_user_course/', {
                    method: 'DELETE',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': document.cookie.match(/csrftoken=([^ ;]+)/)[1]
                    },
                    body: JSON.stringify({
                        courseId: courseId
                    })
                });
                if (response.ok) {
                    // Usunięto pomyślnie, odśwież listę kursów
                    const updatedUserCourses = userCourses.filter(course => course.course_id !== courseId);
                    setUserCourses(updatedUserCourses);
                } else {
                    console.error('Failed to delete course');
                }
            } catch (error) {
                console.error('Error deleting course:', error);
            }
        }
    };

    return (
        <div className="container mt-5">
            <h5 className="mb-4">My Courses</h5>
            <hr />
            {error && <div>Error: {error}</div>}
            {userCourses.length === 0 && !error && <div>No courses available</div>}
            {userCourses.length > 0 && (
                <div className="row">
                    {userCourses.map(course => (
                        <div className="col-md-4 mb-3" key={course.course_id}>
                            <div className="card">
                                <div className="card-body">
                                    <h5 className="card-title">{course.description}</h5>
                                    <p className="card-text">Duration: {course.access_duration} days</p>
                                    <p className="card-text">Price: {course.net_amount} PLN</p>
                                    <p className="card-text">Language: {course.language_cd}</p>
                                    <button
                                        className="btn btn-primary"
                                        onClick={() => handleDetails(course.course_id)}
                                    >
                                        Details
                                    </button>
                                    <button
                                        className="btn btn-danger"
                                        style={{ marginLeft: '5px' }}
                                        onClick={() => handleDelete(course.course_id)}
                                    >
                                        Delete
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

export default MyCourses;
