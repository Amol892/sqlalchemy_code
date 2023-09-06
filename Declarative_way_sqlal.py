#Declarative way

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker,declarative_base
import sqlalchemy
from sqlalchemy_utils import database_exists,create_database


#define database url
DB_URL = "mysql://root:root@127.0.0.1:3306/sqla"

#start Engine
ENG=create_engine(DB_URL)


#Create database automatically
if not database_exists(ENG.url):
    create_database(ENG.url)

# Create a declarative base

Base = declarative_base()

#If we want to create table we have to define class
class Student(Base):

    __tablename__ = 'stu_info'  # Name of the database table

    roll = Column(Integer, primary_key=True)
    name = Column(String(50))
    marks = Column(Float)
    
    def __init__(self,roll,name,marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def __str__(self):
        return f'\n Student Information'\
               f'\n Roll : {self.roll}'\
               f'\n Name : {self.name}'\
               f'\n Mark : {self.marks}'
        

#Create table in database

Base.metadata.create_all(ENG)

#Create session class to execute data manipulation queries like add,delete,update,create new resources into database tables.

session = sessionmaker(bind=ENG)

sess = session() # session object creation

'''
#data addition query:
s1=Student(1,'amol',98)
s2=Student(2,'rohit',95)
s3=Student(3,'sujit',92)
to add single object- sess.add(s1)
to add multiple objects - sess.add_all([s1,s2,s3])

#data updatation query
sess.query(Student).filter(Student.roll==1).update({Student.marks:93})

#delete query
-to delete perticular data
sess.query(Student).filter(Student.roll==2).delete()
-to delete all records
sess.query(Student).delete()

#data Retrive query
-retrive specified record
sess.query(Student).filter(Student.roll==3)
-retrive all records
sess.query(Student)
'''

print('___Menu___')
print('1.Insert data\n2.Display data\n3.Update data\n4.Delete data\n5.Exit')


while True:
    choice = int(input('Enter your choice'))
    #add data
    if choice == 1:
        num = int(input('Enter number of instance of Table'))

        if num == 1 or num>1:
            class_name = globals()[(input('Enter class name:'))]
            
            s_list =  []
            for i in range(num):
                s_obj = class_name(int(input('Enter roll number')),input('Enter student name'),float(input('Enter Mark')))
                s_list.append(s_obj)
            sess.add_all(s_list)
            sess.commit()
            sess.close()
            print('Data successfully added')
        else:
            print('Number should be greater than zero')

    elif choice == 2:
        #Retrive data
        roll_num = int(input('Enter roll number/Enter 0 form all data'))

        if roll_num == 0:
            class_name = globals()[(input('Enter class name:'))]
            s_obj = sess.query(class_name)
            for i in s_obj:
                print(i)
            sess.close()
        elif roll_num>0:
            class_name = globals()[(input('Enter class name:'))]
            s_obj = sess.query(class_name).filter(class_name.roll==roll_num)
            for i in s_obj:
                print(i)
            sess.close()
        else:
            print('Enter positive number')

    elif choice == 3:

        #Update data

        roll_num = int(input('Enter roll number'))

        if roll_num >0:
            class_name = globals()[(input('Enter class name:'))]
            field_list = class_name.__table__.columns.keys()
            field_name = input('Enter field name')
            field_value = input('Enter field value')
            
            
            if field_name == 'name':
                sess.query(class_name).filter(class_name.roll==roll_num).update({class_name.name:field_value})
                sess.commit()
                sess.close()
                print('Data successfully updated')
                
            elif field_name == 'marks':
                sess.query(class_name).filter(class_name.roll==roll_num).update({class_name.marks:float(field_value)})
                sess.commit()
                sess.close()
                print('Data successfully updated')
            else:
                print('Enter valid field name')

            
        else:
            print('Enter positive number')

    elif choice == 4:
        # Delete data
        roll_num = int(input('Enter roll number/Enter 0 form all data'))
        if roll_num == 0:
            class_name = globals()[(input('Enter class name:'))]
            sess.query(class_name).delete()
            sess.commit()
            sess.close()
            print('Data successfully deleted')
        elif roll_num>0:
            class_name = globals()[(input('Enter class name:'))]
            sess.query(class_name).filter(class_name.roll==roll_num).delete()
            sess.commit()
            sess.close()
            print('Data successfully deleted')
            
        else:
            print('Enter positive number')
    
    elif choice == 5:
        break
    else:
        print('Enter valid choice')















