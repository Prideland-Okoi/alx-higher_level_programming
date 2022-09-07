# MySQL - Introduction
Project done during **ALX Software Engineering Scholarship 2022** at **Alx Educations School**. It aims to learn about databases, relational databases, subqueries, tables, **MySQL** statements and functions.
<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/rtcwz.jpg" width="600px"/>

## Resources
Read or watch:

[What is Database & SQL?](https://www.youtube.com/watch?v=FR4QIeZaPeM)
[A Basic MySQL Tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)
[Basic SQL statements: DDL and DML (no need to read the chapter “Privileges”)](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/ddldml.php)
[Basic queries: SQL and RA](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/queries.php)
[SQL technique: functions](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/functions.php)
[SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)
]What makes the big difference between a backtick and an apostrophe?](https://stackoverflow.com/questions/29402361/what-makes-the-big-difference-between-a-backtick-and-an-apostrophe/29402458)
[MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf)
[MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)

## Technologies
* `MySQL 8.0`
* Tested on Ubuntu 20.04 LTS

## Files

All the following files are scripts of MySQL:

| Filename | Description |
| -------- | ----------- |
| `0-list_databases.sql` | Lists all databases of a MySQL server |
| `1-create_database_if_missing.sql` | Creates the database `hbtn_0c_0` in a MySQL server |
| `2-remove_database.sql` | Deletes the database `hbtn_0c_0` in a MySQL server |
| `3-list_tables.sql` | Lists all the tables of a database in a MySQL server |
| `4-first_table.sql` | Creates a table called `first_table` in the current database |
| `5-full_table.sql` | Prints the full description of the table `first_table` from the database `hbtn_0c_0`  |
| `6-list_values.sql` | Lists all rows of the table `first_table` from the database `hbtn_0c_0` |
| `7-insert_value.sql` | Inserts a new row in the table `first_table` of the database `hbtn_0c_0` |
| `8-count_89.sql` | Displays the number of records with `id=89` in the table `first_table` of the database `hbtn_0c_0` |
| `9-full_creation.sql` | Creates a table `second_table` in the database `hbtn_0c_0` |
| `10-top_score.sql` | Lists all records of the table `second_table` of the database `hbtn_0c_0` |
| `11-best_score.sql` | Lists all records with a `score >= 10` in the table `second_table` of the database `hbtn_0c_0` |
| `12-no_cheating.sql` | Updates the score of Bob to `10` in the table `second_table` |
| `13-change_class.sql` | Removes all records with a `score <= 5` in the table `second_table` of the database `hbtn_0c_0` |
| `14-average.sql` | Computes the score average of all records in the table `second_table` of the database `hbtn_0c_0` |
| `15-groups.sql` | Lists the number of records with the same score in the table `second_table` of the database `hbtn_0c_0` |
| `16-no_link.sql` | Lists all records of the table `second_table` of the database `hbtn_0c_0` |
| `100-move_to_utf8.sql` | Converts `hbtn_0c_0` database to UTF8 (`utf8mb4`, collate `utf8mb4_unicode_ci`)  |
| `101-avg_temperatures.sql` | Displays the average temperature (Fahrenheit) by city ordered by temperature (descending) |
| `102-top_city.sql` | Displays the top 3 of cities temperature during July and August ordered by temperature (descending) |
| `103-max_state.sql` | Displays the max temperature of each state (ordered by State name) |
