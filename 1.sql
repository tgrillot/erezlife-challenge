/* docker run -p 5432:5432 --name erldb -e POSTGRES_PASSWORD=isthisasecurepassword? -d postgres 

CREATE TABLE student
(id INTEGER PRIMARY KEY, name TEXT, address TEXT);

CREATE TABLE application
(id INTEGER PRIMARY KEY, student_id INTEGER REFERENCES student (id), score INTEGER);

INSERT INTO student(id,name,address)
VALUES (1,'Bob','1234 asdf')
	,(2,'Alex','2345 l;kj')
	,(3,'Jill','64567 asdfga')
	,(4,'Greg','12356 kgfhk')
	,(5,'Mary','098 aoijeja')
	,(6,'John','097 poasdfl;kj')
	,(7,'Dan','0953 oiasds')
	,(8,'Sue','2134 posdlkj')
	,(9,'Ann','23423 osijdflkj')
	,(10,'Jack','23423 lksdlkj');
	
INSERT INTO application(id,student_id,score)
VALUES (1,1,100),(2,1,100),(3,2,100),(4,3,100),(5,3,100),(6,4,100),(7,4,100),
	(8,4,100),(9,4,100),(10,6,100),(11,6,100),(12,7,100),(13,8,100),(14,8,100),
	(15,8,100),(16,9,100),(17,9,100),(18,10,100),(19,10,100),(20,10,100);*/


SELECT stu.id AS student_id
    ,stu."name" AS student_name
    ,COUNT(app.id) AS total_apps
FROM student stu
    LEFT JOIN application app ON app.student_id = stu.id
GROUP BY stu.id
    ,stu."name";