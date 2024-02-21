# Write your MySQL query statement below
SELECT activity_date as day, COUNT(distinct user_id) as active_users
FROM Activity
WHERE activity_type is not null and activity_date BETWEEN '2019-06-28' AND '2019-07-27'
group by activity_date;