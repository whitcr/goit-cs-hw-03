
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);


CREATE TABLE status (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);


INSERT INTO status (name) VALUES
    ('new'),
    ('in progress'),
    ('completed');


CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    status_id INTEGER NOT NULL REFERENCES status(id),
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE
);

--________________________________________________________________

SELECT  * FROM tasks
JOIN users ON tasks.user_id = users.id
WHERE users.id = 1;

SELECT  * FROM tasks
JOIN status ON tasks.status_id = status.id
WHERE status.name = 'new';

UPDATE tasks
SET status_id = (SELECT id FROM status WHERE name = 'in progress')
WHERE id = 1;

SELECT  * FROM users
WHERE users.id NOT IN (
    SELECT DISTINCT user_id FROM tasks
);

INSERT INTO tasks (title, description, status_id, user_id)
VALUES ('Нове завдання', 'Опис нового завдання', 1, 1);

SELECT  * FROM tasks
JOIN status ON tasks.status_id = status.id
WHERE status.name != 'completed';

DELETE FROM tasks WHERE id = 1;

SELECT * FROM users WHERE email LIKE '%@gmail.com';

UPDATE users SET fullname = 'Денис' WHERE id = 1;

SELECT status.name, COUNT(tasks.id)  
FROM status
LEFT JOIN tasks ON tasks.status_id = status.id
GROUP BY status.name;

SELECT  * FROM tasks
JOIN users ON tasks.user_id = users.id
WHERE users.email LIKE '%@gmail.com';

SELECT * FROM tasks WHERE description IS NULL;

SELECT users.fullname, tasks.title
FROM users
INNER JOIN tasks ON users.id = tasks.user_id
INNER JOIN status ON tasks.status_id = status.id
WHERE status.name = 'in progress';

SELECT users.fullname, COUNT(tasks.id) 
FROM users
LEFT JOIN tasks ON users.id = tasks.user_id
GROUP BY users.fullname;