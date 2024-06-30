# Write your MySQL query statement below
select e.employee_id, e.department_id
from employee e 
where primary_flag='Y' 
or e.employee_id in (
select f.employee_id from employee f
group by f.employee_id
having count(f.department_id)=1 );