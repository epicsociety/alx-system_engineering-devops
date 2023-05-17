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
