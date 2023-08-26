#### Setting Mysql Server on Linux system
1. sudo apt install mysql-server  ---> installing
2. sudo mysql_secure_installation    ---> configure sample users and remote root logins
3. sudo mysql   ---> open sql prompt
4. ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Password@321'; ---> ALTER USER command to change the root user’s authentication method to one that uses a password.
5. exit
6. mysql -u root -p   ---> change the root user’s authentication method back to the default, auth_socket.To authenticate as the root MySQL user using a password
7. ALTER USER 'root'@'localhost' IDENTIFIED WITH auth_socket;     --->  the default authentication method
8. CREATE USER 'username'@'host' IDENTIFIED WITH authentication_plugin BY 'password'; ---> create new user
9. GRANT PRIVILEGE ON database.table TO 'username'@'host';  ---> granting user privileges 

src: https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04
