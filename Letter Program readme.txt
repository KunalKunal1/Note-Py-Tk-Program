Before Running this program make a sql database.
You can follow below steps to make one.
1. Create a database with a name.

2. Then  create below table you can modify or add new columns as per your need.

3. 
CREATE TABLE notes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    note_text TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

4. 
If error occurs, you need to change sql mode.
use below code,

SELECT @@sql_mode;

5. If you see NO_ZERO_DATE or STRICT_TRANS_TABLES in the output, you might want to remove them temporarily to allow the default value to be set. You can change the SQL mode for the current session with:

SET sql_mode = '';

6. To see your sql username and localhost:

SELECT User, Host FROM mysql.user;
