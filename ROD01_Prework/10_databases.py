"""
DATABASES
=========

Applications used to efficiently store and share data.

Used by: banks, companies, websites(Youtube, Spotify)

Before databases, large volumes of data were stored in hierarchies of files
and folders similar to storing data in our personal computers.

The first databases, referred to as navigational databases, where created in
the 1960s.

In the 1970s a new type of databases were created based on the relational
model.
Most used databases are:
- MySQL
- PostgresSQL
- SQLite
- ORACLE
- SQL Server

Relational Databases store data in so-called "relations" (tables). A
relation is a set of rows that share a common set of columns.

One of the reasons for the popularity of databases is the approachable
language that is used to populate them. This language is called SQL.
It can be used to CREATE, MODIFY, DELETE tables, ADD, DELETE, MODIFY rows in a
table, search for rows that satisfy certain conditions in one or more
tables. Simple SQL queries read almost like plain english:

SELECT NAME FROM CLIENTS WHERE SURNAME = 'Smith'

In the last 10 years, databases not using the Relational Model have
increased in popularity. Although they differ significantly in the approach
to data storage, they are collectively referred to as NoSQL. One of the
characteristics shared by NoSQL databases is the less rigid form of data
they store compared to relational databases.

e.g.
- mongoDB
- redis
- cassandra
- HBASE
"""