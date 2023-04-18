import pandas as pd
location=pd.read_csv("Data 2/locations.csv")
employees=pd.read_csv("Data 2/employees.csv")

def Q1():
    print(location)
Q1()

def Q2():
    print(location['LOCATION_ID'])
Q2()

def Q3():
    select = employees[0:7]
    return select
Q3()

def Q4():
    print(employees['DEPARTMENT_ID'].unique())
Q4()

def Q5():
    print(employees[['FIRST_NAME','LAST_NAME','DEPARTMENT_ID']][employees['LAST_NAME']=="McEwen"])
Q5()

def Q6():
    for i in range(len(employees)):
        s = employees['FIRST_NAME'][i]
        index=[0]*len(employees)
        if s[0]=="P":
            print(employees[['FIRST_NAME','LAST_NAME','SALARY','DEPARTMENT_ID']].iloc[i])
Q6()

def Q7():
    for i in range(len(employees)):
        s = employees['FIRST_NAME'][i]
        if "M" in s:
            continue
        elif "m" in s:
            continue
        else:
            print(employees[['FIRST_NAME','LAST_NAME','SALARY','DEPARTMENT_ID']].iloc[i])
Q7()

def Q8():
    print(employees.sort_values('DEPARTMENT_ID'))
Q8()

def Q9():
    print(employees.sort_values('FIRST_NAME', ascending=False))
Q9()

def Q10():
    print(employees[['FIRST_NAME','LAST_NAME','SALARY','MANAGER_ID']][employees['MANAGER_ID']==0])
Q10()

def Q11():
    print(employees[['FIRST_NAME','LAST_NAME','SALARY','MANAGER_ID']][employees['MANAGER_ID'].notna()])
Q11()

def Q12():
    print(employees[['FIRST_NAME','LAST_NAME','SALARY','DEPARTMENT_ID']][employees['DEPARTMENT_ID']==70])
    print(employees[['FIRST_NAME','LAST_NAME','SALARY','DEPARTMENT_ID']][employees['DEPARTMENT_ID']==90])
Q12()