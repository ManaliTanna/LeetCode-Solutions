# Write your MySQL query statement below
select r.contest_id, ROUND(count(r.user_id)/(select count(distinct user_id) from users)*100,2) as percentage
from users u, register r
where u.user_id = r.user_id
group by r.contest_id
order by percentage desc, contest_id asc