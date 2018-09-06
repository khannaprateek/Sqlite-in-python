from sqlite3 import *
#q1
print("Question 1")
print()
try:
    con = connect('Studnets.db')
    print("Students Database has been created")
#q2
    print("Question 2")
    print()    
    mylist=[]
    for i in range(1,11):
        name=input("Enter your name")
        while(1):
            marks=int(input("Enter your marks"))
            if 0<=marks<=100:
                break;
            else:
                print("Please enter your marks between the range(0-100)")
        my=(name,marks)
        mylist.append(my)
    print("Question 3")
    print()
    cur=con.cursor()
    query='create table students(Name varchar(50),Marks double(3,1));'
    cur.execute(query)
    print("Students table has been created")
    print()
    query = 'Insert into students(Name,Marks) values (?,?);'
    cur.executemany(query,mylist)
    query = 'select Name from students where Marks >80;'
    cur.execute(query)
    data = cur.fetchall()
    print("Values has been added to the table")
    print()
    print("Question 4")
    print()
    print("Studnets with marks more than 80 are:")
    if len(data) is 0:
        print("There are no Student with marks grater than 80")
    else:
        for Name in data:
            print(Name[0])
    

finally:
    con.close()
    print('DONE!!')
