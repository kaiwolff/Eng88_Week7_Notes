Keep Project without SQL

Another branch for WITH SQL

Branch out to sql_integrate branch on Kali



SQL SELECT:

SELECT Count - total number of records returned.

E.g. SELECT Count FROM `user_table` WHERE `first_name` = ‘Adam’;

Does not return the record but rather some statistics on the record.

SELECT Max - 
SELECT Min(`user_id`) FROM `user_table`;

The above two return the highest and lowest values of a given field

SELECT Avg - gives average value (might use on something like hours worked, salary, similar).

The outcomes of these look just like a table, where the only field is the requested value

Can also get several values into a table, for example

SELECT Max(`user_id`) as MAX_UID, Min(`user_id`) as MIN_UID FROM `user_table`;

Instead of using fetchall(), which fetches every record that complies with a test, you can return a count instead, which saves a lot of time, and gives back the result as a value.e

IMAGE: examples of code input to update a table and then order by column value




Processing Sequence:




When searching, always try to find a st6andard for what is being searched for re: capital or lowercase letter.
