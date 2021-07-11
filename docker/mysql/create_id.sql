CREATE USER 'datarize'@'%' IDENTIFIED WITH mysql_native_password BY 'datarize123';

GRANT ALL PRIVILEGES ON *.* TO 'datarize'@'%' ;

FLUSH privileges;

-- GRANT ALL PRIVILEGES ON *.* to datarize@localhost IDENTIFIED BY 'datarize123' WITH GRANT OPTION;