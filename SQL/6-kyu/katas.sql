-- 1.
-- For this challenge you need to create a simple SELECT statement that will return all columns from the people table,
-- and join to the sales table so that you can return the COUNT of all sales and RANK each person by their sale_count.

-- people table schema
--     id
--     name

-- sales table schema
--     id
--     people_id
--     sale
--     price

-- You should return all people fields as well as the sale count as "sale_count" and the rank as "sale_rank".

select
  p.id,
  p.name,
  count(s.sale) as sale_count,
  rank() over(order by count(s.sale) desc) as sale_rank
from people p join sales s on p.id=s.people_id
group by p.id;


-- 2.
-- For this challenge you need to create a UNION statement, there are two tables ussales and eusales the parent company
--  tracks each sale at its respective location in each table, you must all filter the sale price so it only returns rows with
--  a sale greater than 50.00. You have been tasked with combining that data for future analysis. Order by location (US before EU), then by id.

-- (us/eu)sales table schema
--     id
--     name
--     price
--     card_name
--     card_number
--     transaction_date

-- resultant table schema
--     location (EU for eusales and US for ussales)
--     id
--     name
--     price (greater than 50.00)
--     card_name
--     card_number
--     transaction_date

select res.* from
(
  select 'US' as location, us.*
  from ussales us

  union all

  select 'EU' as location, eu.*
  from eusales eu
) as res

where price > 50;


-- 3.
-- For this challenge you need to create a simple HAVING statement, you want to count how many people
-- have the same age and return the groups with 10 or more people who have that age.

-- people table schema
--     id
--     name
--     age

-- return table schema
--     age
--     total_people

select age, count(*) as total_people
from people
group by age
having count(*) >= 10;


-- 4.
-- For this challenge you need to create a SELECT statement, this statement must have NULL handling, using COALESCE and NULLIF.

-- If name is an empty string, you must replace with '[product name not found]'.

-- If card_name is an empty string, you must replace with '[card name not found]'.

-- If no price is specified (i.e. price is NULL), or if the price is 50 or less, you must discard the row.

-- eusales table schema
--     id
--     name
--     price
--     card_name
--     card_number
--     transaction_date

-- resultant table schema
--     id
--     name
--     price (greater than 50.00)
--     card_name
--     card_number
--     transaction_date

select
  id,
  coalesce(nullif(name, ''), '[product name not found]') as name,
  price,
  coalesce(nullif(card_name, '') , '[card name not found]') as card_name,
  card_number,
  transaction_date
from eusales
where price > 50


