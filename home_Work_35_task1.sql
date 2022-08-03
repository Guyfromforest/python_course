-- SELECT last_name, first_name, department_name
-- FROM employees JOIN department;

-- SELECT last_name, first_name, depart_name, city, state_province
-- FROM employees AS e JOIN departments as d
-- ON e.department_id=d.department_id
-- JOIN locations as L
-- on d.location_id=l.location_id;

-- SELECT e.last_name, e.first_name, d.depart_name, d.department_id
-- FROM employees AS e JOIN departments AS d
-- ON e.department_id = d.department_id
-- AND E.department_id IN(80,40)


-- SELECT * FROM departments

-- SELECT e.first_name AS "Employee Name",
-- M.first_name AS "Mannager name"
-- From employees e
-- JOIN employees M
-- ON e.manager_id = M.employee_id;

-- SELECT job_title, first_name ||" "||last_name AS "Full name" , max_salary-salary AS salary_difference
-- From employees e
-- Join jobs j 
-- on e.job_id = j.job_id;
-- -- or USING NATURAL JOIN

-- SELECT job_title, AVG(SALARY)
-- FROM employees e
-- join jobs j
-- on e.job_id = j.job_id
-- GROUP by job_title;

-- SELECT first_name ||" "|| last_name AS Full_name, salary
-- FROM employees 
-- JOIN departments USING (department_id) 
-- JOIN  locations USING (location_id) 
-- WHERE  city = "London";

-- SELECT department_name, count(department_id)
-- FROM department 
-- NATURAL JOIN employees(не вирішив)


