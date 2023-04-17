import pandas as pd
location=pd.read_csv("Data 2/locations.csv")
employees=pd.read_csv("Data 2/employees.csv")

def Q1():
    print(location['records'])
Q1()

def Q2():
    print(locations['location id'])
Q2()

def Q3():
    for i in range(7):
        print(employee['records'][i])
Q3()

def Q4():
    print(employees['department id'].unique())
Q4()

def Q5():
    print(employees[['first name'],['last name'],['department number']][employees['last name']=="McEwen"])
Q5()

def Q6():
    for i in range(length(employees)):
        s = employees['first name'][i]
        if s[0]=="P":
            print(employees[['first name'],['last name'],['salary'],['deparmtent number']][i]+"/n")
Q6()

def Q7():
    for i in range(length(employees)):
        s = employees['last name']
        if "M" in s:
            print(employees[['first name'],['last name'],['salary'],['deparmtent number']][i]+"/n")
Q7()

def Q8():
    print(employees.sort_values('department number', axis=1))
Q8()

def Q9():
    print(employees.sort_values('first name', axis=1, ascending=False))
Q9()

def Q10():
    print(employees[['first name'],['last name'],['salary'],['manager id']][employees['manager is']==0])
Q10()

def Q11():
    print(employees[['first name'],['last name'],['salary'],['manager id']][employees['manager id'].notna()])
Q11()

def Q12():
    print(employees[['first name'],['last name'],['salary'],['department number']][employees['department number']==70])
    print(employees[['first name'],['last name'],['salary'],['department number']][employees['department number']==90])
Q12()