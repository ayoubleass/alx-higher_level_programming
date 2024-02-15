-- Lists all records of the table second_table with a name.
SELECT score, name FROM `second_table` WHERE name <>'' and name IS NOT NULL ORDER BY score DESC;
