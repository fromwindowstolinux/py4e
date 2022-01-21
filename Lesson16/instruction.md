# Autograder: Single Table SQL

If you don't already have it, install the SQLite Browser from http://sqlitebrowser.org/.

Then, create a SQLITE database or use an existing database and create a table in the database called "Ages":

```
CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
)
```

Then make sure the table is empty by deleting any rows that you previously inserted, and insert these rows and only these rows with the following commands:

```
DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Cassy', 37);
INSERT INTO Ages (name, age) VALUES ('Jayden', 30);
INSERT INTO Ages (name, age) VALUES ('Luk', 31);
INSERT INTO Ages (name, age) VALUES ('Eonan', 24);
INSERT INTO Ages (name, age) VALUES ('Reagan', 13);
```

Once the inserts are done, run the following SQL command:

```
SELECT hex(name || age) AS X FROM Ages ORDER BY X
```

Find the first row in the resulting record set and enter the long string that looks like 53656C696E613333.

Note: This assignment must be done using SQLite - in particular, the SELECT query above will not work in any other database. So you cannot use MySQL or Oracle for this assignment.

![Imgur](https://imgur.com/0xrXSew.png)

# Autograder: Counting Email in a Database

Counting Organizations.

This application will read the mailbox data (mbox.txt) and count the number of email messages per organization (i.e. domain name of the email address) using a database with the following schema to maintain the counts.

```
CREATE TABLE Counts (org TEXT, count INTEGER)
```

When you have run the program on **mbox.txt** upload the resulting database file above for grading.

If you run the program multiple times in testing or with different files, make sure to empty out the data before each run.

You can use this code as a starting point for your application: http://www.py4e.com/code3/emaildb.py.

The data file for this application is the same as in previous assignments: http://www.py4e.com/code3/mbox.txt.

Because the sample code is using an **UPDATE** statement and committing the results to the database as each record is read in the loop, it might take as long as a few minutes to process all the data. The commit insists on completely writing all the data to disk every time it is called.

The program can be speeded up greatly by moving the commit operation outside of the loop. In any database program, there is a balance between the number of operations you execute between commits and the importance of not losing the results of operations that have not yet been committed.

![Imgur](https://imgur.com/6Hlh0Vy.png)

# Autograder: Many Students in Many Courses

This application will read roster data in JSON format, parse the file, and then produce an SQLite database that contains a User, Course, and Member table and populate the tables from the data file.

You can base your solution on this code: http://www.py4e.com/code3/roster/roster.py - this code is incomplete as you need to modify the program to store the role column in the Member table to complete the assignment.

Each student gets their own file for the assignment. Download this file and save it as roster_data.json. Move the downloaded file into the same folder as your roster.py program.

Once you have made the necessary changes to the program and it has been run successfully reading the above JSON data, run the following SQL command:

```
SELECT User.name,Course.title, Member.role FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;
```

The output should look as follows:

```
Zeeshan|si310|0
Zarah|si363|0
```

Once that query gives the correct data, run this query:

```
SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1;
```

You should get one row with a string that looks like XYZZY53656C696E613333.

![Imgur](https://imgur.com/Yq5K1id.jpg)