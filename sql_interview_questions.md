 Important SQL Interview Questions (Verbal Answers)
 1. What is SQL?
 Structured Query Language (SQL) is a standardized programming language used to manage, query, and manipulate relational databases. It allows users to create, read, update, and delete data (CRUD operations) as well as define and control database structures and security.
 2. Difference between DELETE, TRUNCATE and DROP?
 DELETE is a DML command used to remove specific rows based on a condition and can be rolled back if used inside a transaction. TRUNCATE is a DDL command that quickly removes all rows from a table by deallocating pages, resetting identity columns, and cannot be rolled back in most databases. DROP is a DDL command that entirely deletes the table structure along with its data from the database.
 3. What is a Primary Key?
 A primary key is a column or a set of columns that uniquely identifies each row in a database table. It enforces entity integrity by ensuring that the values are unique and not NULL. A table can have only one primary key.
 4. What is a Foreign Key?
 A foreign key is a field (or collection of fields) in one table that uniquely identifies a row of another table. It establishes a parent-child relationship between tables, ensuring referential integrity so that invalid data cannot be inserted into the foreign key column.
 5. Difference between WHERE and HAVING?
 The WHERE clause filters rows before any groupings or aggregations take place (applied to individual rows). The HAVING clause is used to filter groups after aggregate functions (GROUP BY) have been calculated.
 6. Difference between INNER JOIN and LEFT JOIN?
 An INNER JOIN returns only the records that have matching values in both tables. A LEFT JOIN returns all records from the left table, and the matched records from the right table; if there is no match, the result for the right table columns will be NULL.
 7. What is an index?
 An index is a database performance tuning structure associated with a table that speeds up the retrieval of rows. It works similarly to an index at the back of a textbook, allowing the database engine to locate data quickly without scanning the entire table.
 8. What is a composite index?
 A composite index is a multi-column index built on two or more columns of a table. It is particularly useful when queries frequently filter or sort by multiple columns simultaneously, following the leftmost prefix rule.
 9. What is normalization?
 Normalization is the process of structuring a relational database in accordance with a series of normal forms (1NF, 2NF, 3NF, etc.) to reduce data redundancy and improve data integrity. It splits large tables into smaller, related tables and defines relationships between them.
 10. What are ACID properties?
 ACID stands for Atomicity, Consistency, Isolation, and Durability. These are the standard database transaction properties that guarantee reliable processing of database operations, ensuring data integrity even in the event of system failures.
 11. What is a subquery?
 A subquery is a query nested inside another SQL query (such as inside a SELECT, FROM, WHERE, or HAVING clause). It is used to perform operations that rely on intermediate results calculated dynamically from the database.
 12. What is a CTE?
 A Common Table Expression (CTE) is a temporary result set defined within the execution scope of a single SELECT, INSERT, UPDATE, or DELETE statement. Declared using the WITH clause, it improves query readability and can be used as a recursive query structure.
 13. Difference between UNION and UNION ALL?
 UNION combines the result sets of two or more SELECT queries and automatically removes duplicate rows, which requires an internal sorting operation. UNION ALL also combines result sets but retains all duplicates, making it significantly faster because it avoids the overhead of duplicate elimination.
 14. Difference between RANK and DENSE_RANK?
 Both are window functions used to assign ranks to rows within a partition. RANK leaves gaps in ranking numbers when there are ties (e.g., 1, 2, 2, 4), whereas DENSE_RANK assigns consecutive rankings without any gaps (e.g., 1, 2, 2, 3).
 15. What is a window function?
 A window function performs a calculation across a set of table rows that are somehow related to the current row. Unlike aggregate functions, window functions do not collapse rows into a single group; instead, each row retains its individual identity in the output.
 16. What is NULL?
 How do you handle it?NULL represents a missing, unknown, or inapplicable value in a database column, distinct from zero or an empty string. It is handled using specific operators and functions such as IS NULL, IS NOT NULL, COALESCE() (to substitute a default value), and NULLIF().
 17. What is GROUP BY?
 The GROUP BY statement groups rows that have the same values into summary rows, typically used in conjunction with aggregate functions like COUNT, SUM, AVG, MAX, or MIN to analyze data categorically.
 18. What is a database transaction?
 A database transaction is a sequence of one or more SQL operations executed as a single logical unit of work. It must adhere to ACID properties, meaning either all operations succeed and commit, or none of them apply and the changes roll back.
 19. What is an execution plan (EXPLAIN)?
 An execution plan is a roadmap generated by the database query optimizer showing the sequence of steps the database engine will take to execute a SQL statement. Using the EXPLAIN keyword helps identify performance bottlenecks, missing indexes, and costly sequential table scans.
 20. What is a B-tree index?
 A B-tree (Balanced Tree) is the default self-balancing index structure used in most relational databases. It keeps data sorted and allows searches, sequential access, insertions, and deletions in logarithmic time complexity ($O(\log n)$).
 21. What is a stored procedure?
 A stored procedure is a prepared SQL code block saved in the database server that can be reused and executed with parameters. It improves performance by reducing network traffic, pre-compiling execution plans, and centralizing business logic.
 22. What is a deadlock?
 A deadlock occurs when two or more transactions are permanently blocked because each transaction holds a lock on a resource that the other transaction wants to acquire. The database management system resolves this by automatically aborting (rolling back) one of the transactions.
 23. What is the difference between OFFSET and LIMIT?
 LIMIT specifies the maximum number of rows a query should return, restricting the result size. OFFSET specifies the number of rows to skip before starting to return rows from the query results, commonly used together for pagination.
 24. What is database indexing's disadvantage?
 While indexes speed up SELECT queries, they slow down write operations (INSERT, UPDATE, DELETE) because the database engine must update the index structure every time data changes. Additionally, indexes consume extra disk storage space.
 25. How do you optimize a slow SQL query?
 To optimize a slow query, you can examine the execution plan using EXPLAIN, add appropriate indexes on columns used in WHERE, JOIN, and ORDER BY clauses, avoid unnecessary columns or subqueries, rewrite correlated subqueries as joins, and ensure statistics are up to date.