-- Create Table Teachers
CREATE TABLE teachers (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    first_name varchar(25) NOT NULL,
    last_name varchar(50),
    school varchar(50) NOT NULL,
    hire_date date,
    salary numeric
    );
    
-- Insert Data
-- With Param ID
INSERT INTO teachers (id,first_name, last_name, school, hire_date, salary)
    VALUES (1,'Janet', 'Smith', 'MIT', '2011-10-30', 36200),
           (2,'Lee', 'Reynolds', 'MIT', '1993-05-22', 65000),
           (3,'Samuel', 'Cole', 'Cambridge University', '2005-08-01', 43500),
           (4,'Samantha', 'Bush', 'Cambridge University', '2011-10-30', 36200),
           (5,'Betty', 'Diaz', 'Cambridge University', '2005-08-30', 43500),
           (6,'Kathleen', 'Roush', 'MIT', '2010-10-22', 38500),
           (7,'James', 'Diaz', 'Harvard University', '2003-07-18', 61000),
           (8,'Zack', 'Smith', 'Harvard University', '2000-12-29', 55500),
           (9,'Luis', 'Gonzales', 'Standford University', '2002-12-01', 50000),
           (10,'Frank', 'Abbers', 'Standford University', '1999-01-30', 66000);
           
-- Without Param ID
INSERT INTO teachers (first_name, last_name, school, hire_date, salary)
    VALUES ('Samuel', 'Abbers', 'Standford University', '2006-01-30', 32000),
           ('Jessica', 'Abbers', 'Standford University', '2005-01-30', 33000),
           ('Tom', 'Massi', 'Harvard University', '1999-09-09', 39500),
           ('Esteban', 'Brown', 'MIT', '2007-01-30', 36000),
           ('Carlos', 'Alonso', 'Standford University', '2001-01-30', 44000);
           
-- Create Table Courses
CREATE TABLE courses (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name varchar(20),
    teachers_id INT,
    total_students INT
    );
    
-- Insert Data
INSERT INTO courses (name, teachers_id, total_students)
    VALUES  ('Calculus', 2, 20),
            ('Physics', 2, 10),
            ('Calculus', 1, 30),
            ('Computer Science', 1, 20),
            ('Politic', 13, 15),
            ('Algebra', 2, 10),
            ('Algebra', 13, 30),
            ('Computer Science', 10, 35),
            ('Life Science', 11, 20),
            ('Chemistry', 9, 22),
            ('Chemistry', 8, 16),
            ('Calculus', 5, 19),
            ('Politic', 4, 17),
            ('Biology', 6, 22),
            ('Physics', 3, 29),
            ('Biology', 8, 28),
            ('Calculus', 12, 34),
            ('Physics', 13, 34),
            ('Biology', 14, 25),
            ('Calculus', 15, 20);
            
-- Cases
/*
C.1 Group By
Cases :
Case 1 : Who is the teacher with the highest salary for each university ?
Case 2 : Who is the teacher with the highest salary from Standford University ?
*/

-- the teacher with the highest salary for each university
SELECT first_name, last_name, school, MAX(salary) as 'highest salary'
FROM teachers
GROUP BY school;

-- the teacher with the highest salary from Standford University
SELECT first_name, last_name, school, MAX(salary) as 'highest salary'
FROM teachers
WHERE school = 'Standford University'
GROUP BY school;

/*
C.2. Join
Cases :
Case 1 : Display all courses with teacher's identity
Case 2 : Display how many courses per universities
Case 3 : Display how many total_students per teachers
Case 4 : Display how many courses per teachers
*/

-- Display all courses with teacher's identity
SELECT courses.name as 'course name', teachers.first_name, 
teachers.last_name, teachers.school, teachers.hire_date,
teachers.salary
FROM teachers
JOIN courses ON teachers.id = courses.teachers_id;

-- Display how many courses per universities
SELECT teachers.school, COUNT(courses.name) AS 'course count'
FROM teachers
JOIN courses ON teachers.id = courses.teachers_id
GROUP BY school;

-- Display how many total_students per teachers
SELECT teachers.first_name, teachers.last_name, SUM(courses.total_students) AS 'total student'
FROM teachers
JOIN courses ON teachers.id = courses.teachers_id
GROUP BY teachers.first_name;

-- Display how many courses per teachers
SELECT teachers.first_name, teachers.last_name, COUNT(courses.name) AS 'courses'
FROM teachers
JOIN courses ON teachers.id = courses.teachers_id
GROUP BY teachers.first_name;