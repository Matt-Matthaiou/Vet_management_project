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
    parent_id INT REFERENCES parents(id) ON DELETE CASCADE,
    doctor_id INT REFERENCES doctors(id),
    treatment_notes TEXT
)