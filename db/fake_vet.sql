DROP TABLE comments;
DROP TABLE active_cases;
DROP TABLE pets;
DROP TABLE parents;
DROP TABLE doctors;

CREATE TABLE doctors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    phone VARCHAR(255),
    email VARCHAR(255),
    address VARCHAR(255)
);

CREATE TABLE parents (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    phone VARCHAR(255),
    email VARCHAR(255),
    address VARCHAR(255)
);

CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob VARCHAR(255),
    species VARCHAR(255),
    picture VARCHAR(255),
    parent_id INT REFERENCES parents(id) ON DELETE CASCADE,
    doctor_id INT REFERENCES doctors(id)
    
);

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    comment_date DATE,
    comment TEXT,
    doctor_id INT REFERENCES doctors(id),
    pet_id  INT REFERENCES pets(id)

);

CREATE TABLE active_cases (
    id SERIAL PRIMARY KEY,
    description VARCHAR(255),
    emergency BOOLEAN,
    check_in DATE,
    severity INT,
    completed BOOLEAN,
    pet_id INT REFERENCES pets(id),
    doctor_id INT REFERENCES doctors(id)
);