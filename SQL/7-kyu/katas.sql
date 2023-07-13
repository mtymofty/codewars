-- 1.
--  You work at a book store. It's the end of the month, and you need to find out the 5 bestselling books at your store.
--  Use a select statement to list names, authors, and number of copies sold of the 5 books which were sold most.

-- books table schema
--     name
--     author
--     copies_sold

select name, author, copies_sold
from books
order by copies_sold desc
fetch first 5 rows only;


-- 2.
-- Your friends told you that if you keep coding on your computer, you are going to hurt your eyes.
-- They suggested that you go with them to trivia night at the local club.

-- Once you arrive at the club, you realize the true motive behind your friends' invitation.
-- They know that you are a computer nerd, and they want you to query the countries table and get the answers to the trivia questions.

-- Schema of the countries table:

--     country (String)
--     capital (String)
--     continent (String)

-- The first question: from the African countries that start with the character E, get the names of their capitals ordered alphabetically.

-- You should only give the names of the capitals. Any additional information is just noise
-- If you get more than 3, you will be kicked out, for being too smart
-- Also, this database is crowd-sourced, so sometimes Africa is written Africa and in other times Afrika.
select capital
from countries
where continent in ('Africa', 'Afrika')
and country like 'E%'
order by capital asc
fetch first 3 rows only;


-- 3.
-- Given a demographics table in the following format:

-- ** demographics table schema **
--     id
--     name
--     birthday
--     race

-- you need to return the same table where all text fields (name & race) are changed to the bit length of the string.
select id, bit_length(name) as name, birthday, bit_length(race) as race
from demographics


-- 4.
-- Given the following table 'decimals':

-- decimals table schema
--     id
--     number1
--     number2
-- Return a table with a single column towardzero where the values are the result of number1 + number2 truncated towards zero.

select
  case
    when (number1+number2) >= 0 then floor(number1+number2)
    else ceiling(number1+number2)
  end as towardzero
from decimals










