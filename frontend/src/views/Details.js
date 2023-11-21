import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

const Details = () => {
    const { courseId } = useParams();
    const [courseTitle, setCourseTitle] = useState('');
    const [subjects, setSubjects] = useState([]);
    const [lessonsMap, setLessonsMap] = useState(new Map());
    const [selectedSubject, setSelectedSubject] = useState(null);

    const fetchCourseTitle = async () => {
        try {
            const response = await fetch(`/api/get_course_title/${courseId}`);
            if (!response.ok) {
                throw new Error('Failed to fetch course title');
            }
            const data = await response.json();
            setCourseTitle(data.title);
        } catch (error) {
            console.error('Error fetching course title:', error);
        }
    };

    const fetchSubjects = async () => {
        try {
            const response = await fetch(`/api/get_course_subjects/${courseId}`);
            if (!response.ok) {
                throw new Error('Failed to fetch subjects');
            }
            const data = await response.json();
            setSubjects(data);
        } catch (error) {
            console.error('Error fetching subjects:', error);
        }
    };

    const fetchLessons = async (subjectId) => {
        try {
            const response = await fetch(`/api/get_subject_lessons/${courseId}/${subjectId}`);
            if (!response.ok) {
                throw new Error('Failed to fetch lessons');
            }
            const data = await response.json();
            const newLessonsMap = new Map(lessonsMap);
            newLessonsMap.set(subjectId, data);
            setLessonsMap(newLessonsMap);
        } catch (error) {
            console.error('Error fetching lessons:', error);
        }
    };

    useEffect(() => {
        fetchCourseTitle();
        fetchSubjects();
    }, []);

    const handleSubjectClick = async (subjectId) => {
        setSelectedSubject(subjectId);
        if (!lessonsMap.get(subjectId)) {
            fetchLessons(subjectId);
        }
    };

    return (
        <div className="container mt-5">
            <div className="details">
                <h5 className="mb-4">{courseTitle}</h5>
                <hr />
                <div className="subjects">
                    <ul className="list-group">
                        {subjects.map((subject) => (
                            <li key={subject.id} className="list-group-item">
                                <button
                                    className={`btn btn-link ${selectedSubject === subject.id ? 'active' : ''}`}
                                    onClick={() => handleSubjectClick(subject.id)}
                                >
                                    {subject.title}
                                </button>
                                {selectedSubject === subject.id && (
                                    <ul className="list-group mt-2">
                                        {lessonsMap.get(subject.id)?.map((lesson) => (
                                            <li key={lesson.id} className="list-group-item">{lesson.description}</li>
                                        ))}
                                    </ul>
                                )}
                            </li>
                        ))}
                    </ul>
                </div>
            </div>
        </div>
    );
};

export default Details;
