-- Create a database table caled "user":

CREATE TABLE user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    hobbies TEXT,
    active BOOLEAN NOT NULL DEFAULT 1
);



INSERT INTO user(
    first_name,
    last_name,
    hobbies
) VALUES (
    "Albert",
    "Lara",
    "Eating"
);
INSERT INTO user(
    first_name,
    last_name,
    hobbies
) VALUES (
    "John",
    "Lara",
    "Fishing"
);
INSERT INTO user(
    first_name,
    last_name,
    hobbies
) VALUES (
    "Tammy",
    "Yo",
    "Comedy"
);