-- Tabela główna kursów
CREATE TABLE main_course (
    course_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    description VARCHAR(1000) NOT NULL,
    access_duration INTEGER NOT NULL,
    net_amount NUMERIC(6,2) NOT NULL,
    vat NUMERIC(3,2) NOT NULL,
    language_cd VARCHAR(2) NOT NULL
);

-- Tabela główna użytkowników
CREATE TABLE main_user (
    user_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    birthday DATE NOT NULL,
    phone_number VARCHAR(12),
    address VARCHAR(100) NOT NULL,
    building_number VARCHAR(10),
    postal_code VARCHAR(6) NOT NULL,
    city VARCHAR(10) NOT NULL
);

-- Tabela łącząca kursy i użytkowników
CREATE TABLE IF NOT EXISTS main_user_course (
    user_course_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    course_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    CONSTRAINT fk_course FOREIGN KEY (course_id) REFERENCES main_course(course_id),
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES main_user(user_id)
);

-- Tabela zasobów (np. obrazków)
CREATE TABLE IF NOT EXISTS main_asset (
    asset_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    image BYTEA
);

-- Tabela egzaminów
CREATE TABLE IF NOT EXISTS main_exam (
    exam_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    score INTEGER NOT NULL,
    max_score INTEGER NOT NULL,
    passed BOOLEAN NOT NULL DEFAULT FALSE
);

-- Tabela łącząca użytkowników i egzaminy
CREATE TABLE IF NOT EXISTS main_user_exam (
    user_exam_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    exam_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    CONSTRAINT fk_exam FOREIGN KEY (exam_id) REFERENCES main_exam(exam_id),
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES main_user(user_id)
);

-- Tabela pytań egzaminacyjnych
CREATE TABLE IF NOT EXISTS main_exam_question (
    exam_question_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    asset_id INTEGER NOT NULL,
    description VARCHAR(1000) NOT NULL,
    CONSTRAINT fk_asset FOREIGN KEY (asset_id) REFERENCES main_asset(asset_id)
);

-- Tabela odpowiedzi na pytania egzaminacyjne
CREATE TABLE IF NOT EXISTS main_exam_question_answer (
    answer_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    exam_question_id INTEGER NOT NULL,
    asset_id INTEGER NOT NULL,
    description VARCHAR(1000) NOT NULL,
    correct BOOLEAN NOT NULL,
    CONSTRAINT fk_question FOREIGN KEY (exam_question_id) REFERENCES main_exam_question(exam_question_id),
    CONSTRAINT fk_asset FOREIGN KEY (asset_id) REFERENCES main_asset(asset_id)
);

-- Tabela łącząca egzaminy i pytania egzaminacyjne
CREATE TABLE IF NOT EXISTS main_exam_exam_question (
    exam_exam_question_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    exam_id INTEGER NOT NULL,
    exam_question_id INTEGER NOT NULL,
    CONSTRAINT fk_exam FOREIGN KEY (exam_id) REFERENCES main_exam(exam_id),
    CONSTRAINT fk_exam_question FOREIGN KEY (exam_question_id) REFERENCES main_exam_question(exam_question_id)
);

-- Tabela przedmiotów
CREATE TABLE IF NOT EXISTS main_subject (
    subject_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    course_id INTEGER NOT NULL,
    title VARCHAR(100) NOT NULL,
    seqence VARCHAR(1000) NOT NULL,
    CONSTRAINT fk_course FOREIGN KEY (course_id) REFERENCES main_course(course_id)
);

-- Tabela lekcji
CREATE TABLE IF NOT EXISTS main_lesson (
    lesson_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    subject_id INTEGER NOT NULL,
    seqence VARCHAR(1000),
    short_description VARCHAR(100),
    description VARCHAR(1000),
    CONSTRAINT fk_subject FOREIGN KEY (subject_id) REFERENCES main_subject(subject_id)
);

-- Tabela zawartości lekcji
CREATE TABLE IF NOT EXISTS main_lesson_content (
    lesson_content_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    lesson_id INTEGER NOT NULL,
    asset_id INTEGER NOT NULL,
    seqence VARCHAR(1000),
    content_type VARCHAR(100),
    CONSTRAINT fk_lesson FOREIGN KEY (lesson_id) REFERENCES main_lesson(lesson_id),
    CONSTRAINT fk_asset FOREIGN KEY (asset_id) REFERENCES main_asset(asset_id)
);

-- Tabela certyfikatów
CREATE TABLE IF NOT EXISTS main_certificate (
    certificate_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    course_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    date_from DATE NOT NULL,
    date_to DATE,
    certificate_pdf_path VARCHAR(100),
    title VARCHAR(100) NOT NULL,
    description VARCHAR(100) NOT NULL,
    CONSTRAINT fk_course FOREIGN KEY (course_id) REFERENCES main_course(course_id),
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES main_user(user_id)
);

-- Tabela mentorów
CREATE TABLE IF NOT EXISTS main_mentor (
    mentor_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    birthday DATE NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone_number VARCHAR(12)
);

-- Dodanie kolumny mentor_id do tabeli main_course
ALTER TABLE main_course ADD COLUMN mentor_id INTEGER NOT NULL;

-- Dodanie klucza obcego do kolumny mentor_id w tabeli main_course
ALTER TABLE main_course ADD CONSTRAINT fk_mentor FOREIGN KEY (mentor_id) REFERENCES main_mentor(mentor_id);

-- Funkcja zwracająca cene z podatkiem
CREATE OR REPLACE FUNCTION calculate_total_price(vId INTEGER)
RETURN NUMERIC IS
  total_price NUMERIC;
BEGIN
  SELECT net_amount * (1 + vat) INTO total_price
  FROM main_course 
  WHERE course_id = vId;
  
  RETURN total_price;
END;


-- Procedura usuwająca kurs użytkownika
CREATE OR REPLACE PROCEDURE delete_main_user_course(cId INTEGER, uId INTEGER) IS
BEGIN
  DELETE FROM main_user_course WHERE course_id = cId AND user_id = uId;
  COMMIT;
END;

-- Indeks wspomagajacy wyszukiwanie po użytkownikach
CREATE INDEX idx_username ON main_user(first_name);