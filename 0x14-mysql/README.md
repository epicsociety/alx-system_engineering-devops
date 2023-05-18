# installing mysql on both web-01 and web-02

## steps followed

To install mysql version 5.7, the following alx-provided resource is the best guide:
[Source](https://intranet.alxswe.com/concepts/100002)

## Create a MySQL user named holberton_user  with the host name set to localhost and the password projectcorrection280hbtn. 
> This will allow us to access the replication status on both servers

```
mysql -u root -p

CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
```

## Creating a database with at least one table and one row in your primary MySQL server (web-01) to replicate from
> This is per alx instructions:

```
mysql -u root -p
CREATE DATABASE tyrell_corp;
USE tyrell_corp;
CREATE TABLE nexus6 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255));
INSERT INTO nexus6 (name) VALUES ('Entry 1');
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
```

## Creating a new user for the replica server
> new user should be replica_user, with the host name set to %, and can have whatevr password you’d like

```
mysql -u root -p
CREATE USER 'replica_user'@'%' IDENTIFIED BY 'your_password';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
```

## Setting up replication for the MySQL database named "tyrell_corp" with the primary hosted on web-01 and the replica hosted on web-02
> These instructions are as precise as possible

> ### Update the MySQL Primary Configuration (web-01)

- a. Open the MySQL configuration file for editing. The file is typically located at /etc/mysql/mysql.conf.d/mysqld.cnf or /etc/my.cnf.
- b. Locate the bind-address parameter in the configuration file and comment it out by adding a '#' symbol at the beginning of the line. This allows MySQL to listen on all available network interfaces.
- c. Add the following configuration options at the end of the file to enable replication:
   
   ``` 
   server-id = 1
   log_bin = /var/log/mysql/mysql-bin.log
   binlog_do_db = tyrell_corp 
   ```
> The server-id uniquely identifies the primary server. The log_bin option enables binary logging, which is necessary for replication. The binlog_do_db option specifies the database to be replicated.
- d. Save the changes to the configuration file.
- e. Restart the MySQL service to apply the changes:
  ```
  sudo service mysql restart
  ```
  
**Update the MySQL Replica Configuration (web-02):**
---
- a. Open the MySQL configuration file for editing, which should be the same as the primary server.
- b. Locate the bind-address parameter in the configuration file and ensure it is set to the IP address or hostname of web-02. This specifies the network interface on which MySQL should listen.
- c. Add the following configuration options at the end of the file to enable replication:
 ```server-id = 2
 relay_log = /var/log/mysql/mysql-relay-bin.log
 read_only = 1
 ```       
> The server-id uniquely identifies the replica server. The relay_log option specifies the location of the relay log, which stores replicated events on the replica. The read_only option ensures that the replica is not writable to prevent accidental data modifications.
- d. Save the changes to the configuration file.
- e. Restart the MySQL service to apply the changes:  
   ```
   sudo service mysql restart
   ```     
**Grant Replication Privileges on Primary:**
---
- a. Log in to the primary MySQL server (web-01) as a user with administrative privileges, such as the 'root' user.
- b. Run the following commands to grant replication privileges to the replica:    
  ```
  GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'web-02' IDENTIFIED BY 'replica_password';
  FLUSH PRIVILEGES;
  ```    
>  Replace 'replica_user' with the desired username for replication on the replica server, and 'replica_password' with the corresponding password.
### Retrieve Primary Log File and Position: 
- a. Log in to the primary MySQL server (web-01).
- b. Run the following command to obtain the current log file and position information   
   ```
   SHOW MASTER STATUS;
   ```     
- c. Take note of the values for the File and Position fields. You will need these values to configure the replica.
**Configure Replication on the Replica:**
---
- a. Log in to the replica MySQL server (web-02) as a user with administrative privileges, such as the 'root' user.
- b. Run the following command to configure replication on the replica:
  ```
  CHANGE MASTER TO MASTER_HOST='web-01', MASTER_USER='replica_user', MASTER_PASSWORD='replica_password', MASTER_LOG_FILE='log_file_from_primary',
  MASTER_LOG_POS=log_position_from_primary; 
  ```
> Replace `'web-01'` with the IP address or hostname of the primary server. Replace `'replica_user'` and `'replica_password'` with the username and password specified in the previous step. Replace `'log_file_from_primary'` and `'log_position_from_primary'` with the values obtained from the `SHOW MASTER STATUS` command on the primary server.
- c. Start the replication process:
```
START SLAVE;
```
- d. Verify the replication status by running:
```
SHOW SLAVE STATUS \G;
```
> Look for the `Slave_IO_Running` and `Slave_SQL_Running` fields in the output. Both should display 'Yes', indicating that replication is functioning correctly.

**Allow MySQL Port (3306) through UFW:**
---
- a. If UFW (Uncomplicated Firewall) is enabled on both web-01 and web-02, you need to allow incoming connections on the MySQL port (3306) for replication.
- b. Run the following command on both web-01 and web-02 to enable MySQL connections:
```
sudo ufw allow 3306
```
- c. Verify that UFW allows connections on port 3306 by running:
```
sudo ufw status
```
