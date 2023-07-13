-- 1.
-- Terminal game move function
-- In this game, the hero moves from left to right.
-- The player rolls the dice and moves the number of spaces indicated by the dice two times.
-- In SQL, you will be given a table moves with columns position and roll.
-- Return a table which uses the current position of the hero and the roll (1-6) and returns the new position in a column res.
select position as pos, roll, (position + roll * 2) as res
from moves


-- 2.
-- This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.
select number, case when number % 2 = 0 then number * 8 else number * 9 end as res
from multiplication

-- 3.
-- You are a border guard sitting on the Canadian border. You were given a list of travelers who have arrived at your gate today.
-- You know that American, Mexican, and Canadian citizens don't need visas, so they can just continue their trips.
-- You don't need to check their passports for visas! You only need to check the passports of citizens of all other countries!

-- Select names, and countries of origin of all the travelers, excluding anyone from Canada, Mexico, or The US.

-- travelers table schema
--     name
--     country

-- NOTE: The United States is written as 'USA' in the table.
select name, country
from travelers
where country not in ('USA', 'Canada', 'Mexico')


-- 4.
-- In your application, there is a section for adults only.
-- You need to get a list of names and ages of users from the users table, who are 18 years old or older.

-- users table schema
--     name
--     age
select name, age
from users
where age >= 18


-- 5.
-- You received an invitation to an amazing party. Now you need to write an insert statement to add yourself to the table of participants.

-- participants table schema
--  name (string)
--  age (integer)
--  attending (boolean)

-- NOTES:
-- Since alcohol will be served, you can only attend if you are 21 or older
-- You can't attend if the attending column returns anything but true

INSERT INTO participants VALUES ('My name', 21, true);

SELECT * FROM participants;


-- 6.
-- You are working for a local school, and you are responsible for collecting tuition from students.
-- You have a list of all students, some of them have already paid tution and some haven't.
-- Write a select statement to get a list of all students who haven't paid their tuition yet.
-- The list should include all the data available about these students.

-- students table schema
--  name (string)
--  age (integer)
--  semester (integer)
--  mentor (string)
--  tuition_received (Boolean)

select name, age, semester, mentor, tuition_received
from students
where tuition_received = false;


-- 7.



-- 8.



-- 9.



-- 10.



