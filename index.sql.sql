CREATE TABLE Tasks (
	id INT PRIMARY KEY,
    title VARCHAR(100) NOT NUll,
    Statuss VARCHAR(100) NOT NUll,
    due VARCHAR(100) NOT NUll
);

INSERT INTO Tasks (title,Statuss, due)
VALUES ('Buy groceries', 'pending', '2024-04-15'),
('Submit report' , 'done' ,'2024-04-10' ),
('Go jogging' , 'pending' ,'2024-04-12' ),
('Bokk flight' , 'done' ,'2024-04-8' );

SELECT * FROM Tasks WHERE title='Go jogging';
UPDATE Tasks SET Statuss = 'done' WHERE id=1;
DELETE FROM tasks WHERE id='2';
SELECT * FROM Tasks WHERE due <'2024-10-02';
SELECT Statuss, COUNT(id) AS nb FROM tasks GROUP BY Statuss;