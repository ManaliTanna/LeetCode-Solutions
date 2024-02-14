# Write your MySQL query statement below
select customer_id, count(*) as count_no_trans 
from Visits v
Left outer join Transactions t 
on v.visit_id = t.visit_id
where transaction_id is null
group by customer_id
