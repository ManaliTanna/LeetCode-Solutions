# Write your MySQL query statement below
select e.employee_id 
from Employees e
where e.salary < 30000 and 
e.manager_id not in(select m.employee_id from employees m)
order by e.employee_id