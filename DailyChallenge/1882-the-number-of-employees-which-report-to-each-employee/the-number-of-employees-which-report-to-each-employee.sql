# Write your MySQL query statement below
select m.employee_id, m.name, COUNT(e.employee_id) as reports_count, ROUND(AVG(e.age)) as average_age
from Employees e
join Employees m
where e.reports_to = m.employee_id
group by m.employee_id, m.name
order by m.employee_id;