--  1.
-- For this challenge you need to create a simple SELECT statement.
-- Your task is to calculate the MIN, MEDIAN and MAX scores of the students from the results table

select min(score) as min, percentile_cont(0.5) within group(order by score) as median, max(score) as max
from student
left outer join result on(student.id=result.student_id)


-- 2.
-- Given the schema presented below write a query, which uses a LATERAL join,
-- that returns two most viewed posts for every category.

-- Order the result set by:
--     category name alphabetically
--     number of post views largest to lowest
--     post id lowest to largest

-- Note:
-- Some categories may have less than two or no posts at all.
-- Two or more posts within the category can be tied by (have the same)
-- the number of views. Use post id as a tie breaker - a post with a lower id gets a higher rank.

select c.id as category_id, c.category, p.title, p.views, p.id as post_id
from categories c left outer join lateral
  (select title, views, id
  from posts
  where posts.category_id=c.id
  order by views desc
  fetch first 2 rows only) as p
on true
order by c.category asc, p.views desc, p.id asc


-- 3.
-- For this challenge you need to PIVOT data. You have two tables, products and details.
-- Your task is to pivot the rows in products to produce a table of products which have
-- rows of their detail. Group and Order by the name of the Product.

CREATE EXTENSION tablefunc;

select *
from crosstab(
'select
  name,
  detail,
  count(*)
from products p join details d on(p.id=d.product_id)
group by name, detail
order by name')
as ct ("name" text, "bad" bigint, "good" bigint, "ok" bigint);


-- 4.
-- Given film_actor and film tables from the DVD Rental sample database find all movies both
-- Sidney Crowe (actor_id = 105) and Salma Nolte (actor_id = 122) cast in together
-- and order the result set alphabetically.

select title
from
  (select film_id from film_actor where actor_id=122
  union all
  select film_id from film_actor where actor_id=105) as f
inner join film using(film_id)
group by film_id
having count(film_id) > 1
order by title asc;


-- 5
-- Given a posts table that contains a created_at timestamp column write a query that
-- returns date (without time component), a number of posts for a given date and a running
-- (cumulative) total number of posts up until a given date. The resulting set should be
-- ordered chronologically by date.

select date(created_at) date, count(*) count, cast(sum(count(*)) over(order by date(created_at)) as int) as total
from posts
group by date(created_at)
order by date(created_at)


-- 6.
-- You are a data analyst at a prestigious UK university. As part of the university's
-- ongoing efforts to understand student performance and provide effective learning support,
-- you've been tasked with analyzing the course scores of students over the academic year 2022-2023.
-- Universities in the UK follow a trimester system, with each year split into three terms.

-- Your task is to identify students who have shown consistent improvement in their course scores over
-- the three trimesters. The university is particularly interested in these students to understand and
-- potentially replicate their success.

select
  id as student_id,
  name,
  concat (
    'Michaelmas (', avgs.m_avg, '), ', 'Lent (', avgs.l_avg, '), ', 'Summer (', avgs.s_avg, ')'
    ) as trimesters_avg_scores,
  case when avgs.m_avg < avgs.l_avg and avgs.l_avg < avgs.s_avg then true else false end as consistent_improvement
from students s
join (
  select
      student_id,
      round(avg(case when course_date between '2022-10-01' and '2022-12-31' then score end), 2) as m_avg,
      round(avg(case when course_date between '2023-01-01' and '2023-03-31' then score end), 2) as l_avg,
      round(avg(case when course_date between '2023-04-01' and '2023-06-30' then score end), 2) as s_avg
   from courses
   group by student_id
  ) as avgs on avgs.student_id = s.id
group by id, name, avgs.m_avg, avgs.l_avg, avgs.s_avg
order by id desc;







