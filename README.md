tornado
=======

use python tornado make rest web service, include ORM, use python mysqldb

you should install tornado-3.1 and python-mysqldb

cd tornado-3.1/  
python setup.py build  
sudo python setup.py install  

~make sure tornado can be work

sudo apt-get install python-mysqldb  

open you mysql phpmyadmin and creat a database pay  
CREATE TABLE IF NOT EXISTS `test` (  
  `id` int(11) NOT NULL AUTO_INCREMENT,  
  `name` varchar(20) NOT NULL,  
  `pwd` varchar(32) NOT NULL,  
  PRIMARY KEY (`id`)  
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=4 ;  

INSERT INTO `test` (`id`, `name`, `pwd`) VALUES  
(1, 'python-test', '123456'),  
(2, 'python-test', '123456'),  
(3, 'python-test', '123456');  


usage in ubuntu 13.04  

sudo chmod -R 777 start.sh  
bash ./start.sh start //start tornado  
bash ./start.sh stop //stop tornado  
bash ./start.sh status //tornado status   
bash ./start.sh restart //restart tornado  

main.port just notes tornado port