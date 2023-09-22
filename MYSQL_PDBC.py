import MySQLdb as mdb

# connect() method is used to make connection between python and mysql
# connect method takes 4arguments
# 1) user = 'root', 2) passwrod='root', 3) host='localhost'/'127.0.0.1, 4)db = 'database_name'
# connection method return connection class object

conn = mdb.connect(user='root',password='root',host='localhost',db='pdbc_mysql')

# cursor() method is used to create cursor class object,  this method is parsent inside connection class

curs = conn.cursor()


# execute method is used to fire sql commands from python
#It is present inside cursor class
# Create database PDBC_mysql

#curs.execute('create database PDBC_mysql')

# show all databases
#curs.execute('show databases')

#  create table

new_table = ''' create table `pdbc_mysql`.`order`
            (`oid` int, `product_id` int, `product_name` varchar(30), `qty` int, `price` float, primary key(`oid`))'''

product_table = ''' create table `product`(`pid` int, `product_name` varchar(30), primary key(`pid`))'''
#curs.execute(product_table)

#curs.execute('show tables')

#Insert data into order table

#order1 = ''' insert into `order` (`oid`, `product_id`,`product_name`,`qty`,`price`) values(7,1,'basketball',1,300.0)'''


#curs.execute(order1)
select_order = ''' select * from `order`'''
# fetch all data from order table
curs.execute('select * from `order`')

# describe order table
curs.execute("desc `product`")

#update the resources

#order_update = ''' update `order` set `price` = 400 where `oid`=1'''
#curs.execute(order_update)

#Delete record

curs.execute("delete from `order` where `oid`=1")
curs.execute('select * from `order`')

for i in curs:
    print(i)

conn.commit()

conn.close()
