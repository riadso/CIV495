import pandas as pd
location=pd.read_csv("Data 2/locations.csv")
employees=pd.read_csv("Data 2/employees.csv")

def Q1():
    print(location)
# Q1()
#     LOCATION_ID  ...    COUNTRY_ID
# 0          1000  ...   IT         
# 1          1100  ...   IT         
# 2          1200  ...   JP         
# 3          1300  ...   JP         
# 4          1400  ...   US         
# 5          1500  ...   US         
# 6          1600  ...   US         
# 7          1700  ...   US         
# 8          1800  ...   CA         
# 9          1900  ...   CA         
# 10         2000  ...   CN         
# 11         2100  ...   IN         
# 12         2200  ...   AU         
# 13         2300  ...   SG         
# 14         2400  ...   UK         
# 15         2500  ...   UK         
# 16         2600  ...   UK         
# 17         2700  ...   DE         
# 18         2800  ...   BR         
# 19         2900  ...   CH         
# 20         3000  ...   CH         
# 21         3100  ...   NL         
# 22         3200  ...   MX

# [23 rows x 6 columns]
def Q2():
    print(location['LOCATION_ID'])
# Q2()
# 0     1000
# 1     1100
# 2     1200
# 3     1300
# 4     1400
# 5     1500
# 6     1600
# 7     1700
# 8     1800
# 9     1900
# 10    2000
# 11    2100
# 12    2200
# 13    2300
# 14    2400
# 15    2500
# 16    2600
# 17    2700
# 18    2800
# 19    2900
# 20    3000
# 21    3100
# 22    3200
# Name: LOCATION_ID, dtype: int64

def Q3():
    print(employees[0:7])
# Q3()
#    EMPLOYEE_ID FIRST_NAME  LAST_NAME  ... COMMISSION_PCT MANAGER_ID DEPARTMENT_ID
# 0          100     Steven       King  ...            0.0          0            90
# 1          101      Neena    Kochhar  ...            0.0        100            90
# 2          102        Lex    De Haan  ...            0.0        100            90
# 3          103  Alexander     Hunold  ...            0.0        102            60
# 4          104      Bruce      Ernst  ...            0.0        103            60
# 5          105      David     Austin  ...            0.0        103            60
# 6          106      Valli  Pataballa  ...            0.0        103            60

# [7 rows x 11 columns]

def Q4():
    print(employees['DEPARTMENT_ID'].unique())
# Q4()
# [ 90  60 100  30  50  80   0  10  20  40  70 110]

def Q5():
    print(employees[['FIRST_NAME','LAST_NAME','DEPARTMENT_ID']][employees['LAST_NAME']=="McEwen"])
# Q5()
#    FIRST_NAME LAST_NAME  DEPARTMENT_ID
# 58      Allan    McEwen             80

def Q6():
    for i in range(len(employees)):
        s = employees['FIRST_NAME'][i]
        index=[0]*len(employees)
        if s[0]=="P":
            print(employees[['FIRST_NAME','LAST_NAME','SALARY','DEPARTMENT_ID']].iloc[i])
# Q6()
# FIRST_NAME          Payam
# LAST_NAME        Kaufling
# SALARY               7900
# DEPARTMENT_ID          50
# Name: 22, dtype: object
# FIRST_NAME        Peter
# LAST_NAME        Vargas
# SALARY             2500
# DEPARTMENT_ID        50
# Name: 44, dtype: object
# FIRST_NAME        Peter
# LAST_NAME        Tucker
# SALARY            10000
# DEPARTMENT_ID        80
# Name: 50, dtype: object
# FIRST_NAME       Peter
# LAST_NAME         Hall
# SALARY            9000
# DEPARTMENT_ID       80
# Name: 52, dtype: object
# FIRST_NAME       Patrick
# LAST_NAME          Sully
# SALARY              9500
# DEPARTMENT_ID         80
# Name: 57, dtype: object
# FIRST_NAME        Pat
# LAST_NAME         Fay
# SALARY           6000
# DEPARTMENT_ID      20
# Name: 102, dtype: object

def Q7():
    for i in range(len(employees)):
        s = employees['FIRST_NAME'][i]
        if "M" in s:
            continue
        elif "m" in s:
            continue
        else:
            print(employees[['FIRST_NAME','LAST_NAME','SALARY','DEPARTMENT_ID']].iloc[i])
# Q7()
# FIRST_NAME       Steven
# LAST_NAME          King
# SALARY            24000
# DEPARTMENT_ID        90
# Name: 0, dtype: object
# FIRST_NAME         Neena
# LAST_NAME        Kochhar
# SALARY             17000
# DEPARTMENT_ID         90
# Name: 1, dtype: object
# FIRST_NAME           Lex
# LAST_NAME        De Haan
# SALARY             17000
# DEPARTMENT_ID         90
# Name: 2, dtype: object
# FIRST_NAME       Alexander
# LAST_NAME           Hunold
# SALARY                9000
# DEPARTMENT_ID           60
# Name: 3, dtype: object
# FIRST_NAME       Bruce
# LAST_NAME        Ernst
# SALARY            6000
# DEPARTMENT_ID       60
# Name: 4, dtype: object
# FIRST_NAME        David
# LAST_NAME        Austin
# SALARY             4800
# DEPARTMENT_ID        60
# Name: 5, dtype: object
# FIRST_NAME           Valli
# LAST_NAME        Pataballa
# SALARY                4800
# DEPARTMENT_ID           60
# Name: 6, dtype: object
# FIRST_NAME         Diana
# LAST_NAME        Lorentz
# SALARY              4200
# DEPARTMENT_ID         60
# Name: 7, dtype: object
# FIRST_NAME           Nancy
# LAST_NAME        Greenberg
# SALARY               12008
# DEPARTMENT_ID          100
# Name: 8, dtype: object
# FIRST_NAME       Daniel
# LAST_NAME        Faviet
# SALARY             9000
# DEPARTMENT_ID       100
# Name: 9, dtype: object
# FIRST_NAME       John
# LAST_NAME        Chen
# SALARY           8200
# DEPARTMENT_ID     100
# Name: 10, dtype: object
# FIRST_NAME       Luis
# LAST_NAME        Popp
# SALARY           6900
# DEPARTMENT_ID     100
# Name: 13, dtype: object
# FIRST_NAME            Den
# LAST_NAME        Raphaely
# SALARY              11000
# DEPARTMENT_ID          30
# Name: 14, dtype: object
# FIRST_NAME       Alexander
# LAST_NAME             Khoo
# SALARY                3100
# DEPARTMENT_ID           30
# Name: 15, dtype: object
# FIRST_NAME       Shelli
# LAST_NAME         Baida
# SALARY             2900
# DEPARTMENT_ID        30
# Name: 16, dtype: object
# FIRST_NAME        Sigal
# LAST_NAME        Tobias
# SALARY             2800
# DEPARTMENT_ID        30
# Name: 17, dtype: object
# FIRST_NAME          Guy
# LAST_NAME        Himuro
# SALARY             2600
# DEPARTMENT_ID        30
# Name: 18, dtype: object
# FIRST_NAME            Karen
# LAST_NAME        Colmenares
# SALARY                 2500
# DEPARTMENT_ID            30
# Name: 19, dtype: object
# FIRST_NAME        Shanta
# LAST_NAME        Vollman
# SALARY              6500
# DEPARTMENT_ID         50
# Name: 23, dtype: object
# FIRST_NAME         Kevin
# LAST_NAME        Mourgos
# SALARY              5800
# DEPARTMENT_ID         50
# Name: 24, dtype: object
# FIRST_NAME       Julia
# LAST_NAME        Nayer
# SALARY            3200
# DEPARTMENT_ID       50
# Name: 25, dtype: object
# FIRST_NAME             Irene
# LAST_NAME        Mikkilineni
# SALARY                  2700
# DEPARTMENT_ID             50
# Name: 26, dtype: object
# FIRST_NAME       Steven
# LAST_NAME        Markle
# SALARY             2200
# DEPARTMENT_ID        50
# Name: 28, dtype: object
# FIRST_NAME        Laura
# LAST_NAME        Bissot
# SALARY             3300
# DEPARTMENT_ID        50
# Name: 29, dtype: object
# FIRST_NAME          TJ
# LAST_NAME        Olson
# SALARY            2100
# DEPARTMENT_ID       50
# Name: 32, dtype: object
# FIRST_NAME        Jason
# LAST_NAME        Mallin
# SALARY             3300
# DEPARTMENT_ID        50
# Name: 33, dtype: object
# FIRST_NAME         Ki
# LAST_NAME         Gee
# SALARY           2400
# DEPARTMENT_ID      50
# Name: 35, dtype: object
# FIRST_NAME            Hazel
# LAST_NAME        Philtanker
# SALARY                 2200
# DEPARTMENT_ID            50
# Name: 36, dtype: object
# FIRST_NAME       Renske
# LAST_NAME        Ladwig
# SALARY             3600
# DEPARTMENT_ID        50
# Name: 37, dtype: object
# FIRST_NAME       Stephen
# LAST_NAME         Stiles
# SALARY              3200
# DEPARTMENT_ID         50
# Name: 38, dtype: object
# FIRST_NAME       John
# LAST_NAME         Seo
# SALARY           2700
# DEPARTMENT_ID      50
# Name: 39, dtype: object
# FIRST_NAME       Joshua
# LAST_NAME         Patel
# SALARY             2500
# DEPARTMENT_ID        50
# Name: 40, dtype: object
# FIRST_NAME       Trenna
# LAST_NAME          Rajs
# SALARY             3500
# DEPARTMENT_ID        50
# Name: 41, dtype: object
# FIRST_NAME       Curtis
# LAST_NAME        Davies
# SALARY             3100
# DEPARTMENT_ID        50
# Name: 42, dtype: object
# FIRST_NAME       Randall
# LAST_NAME          Matos
# SALARY              2600
# DEPARTMENT_ID         50
# Name: 43, dtype: object
# FIRST_NAME        Peter
# LAST_NAME        Vargas
# SALARY             2500
# DEPARTMENT_ID        50
# Name: 44, dtype: object
# FIRST_NAME          John
# LAST_NAME        Russell
# SALARY             14000
# DEPARTMENT_ID         80
# Name: 45, dtype: object
# FIRST_NAME          Karen
# LAST_NAME        Partners
# SALARY              13500
# DEPARTMENT_ID          80
# Name: 46, dtype: object
# FIRST_NAME         Alberto
# LAST_NAME        Errazuriz
# SALARY               12000
# DEPARTMENT_ID           80
# Name: 47, dtype: object
# FIRST_NAME          Gerald
# LAST_NAME        Cambrault
# SALARY               11000
# DEPARTMENT_ID           80
# Name: 48, dtype: object
# FIRST_NAME         Eleni
# LAST_NAME        Zlotkey
# SALARY             10500
# DEPARTMENT_ID         80
# Name: 49, dtype: object
# FIRST_NAME        Peter
# LAST_NAME        Tucker
# SALARY            10000
# DEPARTMENT_ID        80
# Name: 50, dtype: object
# FIRST_NAME           David
# LAST_NAME        Bernstein
# SALARY                9500
# DEPARTMENT_ID           80
# Name: 51, dtype: object
# FIRST_NAME       Peter
# LAST_NAME         Hall
# SALARY            9000
# DEPARTMENT_ID       80
# Name: 52, dtype: object
# FIRST_NAME       Christopher
# LAST_NAME              Olsen
# SALARY                  8000
# DEPARTMENT_ID             80
# Name: 53, dtype: object
# FIRST_NAME         Nanette
# LAST_NAME        Cambrault
# SALARY                7500
# DEPARTMENT_ID           80
# Name: 54, dtype: object
# FIRST_NAME        Oliver
# LAST_NAME        Tuvault
# SALARY              7000
# DEPARTMENT_ID         80
# Name: 55, dtype: object
# FIRST_NAME       Janette
# LAST_NAME           King
# SALARY             10000
# DEPARTMENT_ID         80
# Name: 56, dtype: object
# FIRST_NAME       Patrick
# LAST_NAME          Sully
# SALARY              9500
# DEPARTMENT_ID         80
# Name: 57, dtype: object
# FIRST_NAME        Allan
# LAST_NAME        McEwen
# SALARY             9000
# DEPARTMENT_ID        80
# Name: 58, dtype: object
# FIRST_NAME       Lindsey
# LAST_NAME          Smith
# SALARY              8000
# DEPARTMENT_ID         80
# Name: 59, dtype: object
# FIRST_NAME       Louise
# LAST_NAME         Doran
# SALARY             7500
# DEPARTMENT_ID        80
# Name: 60, dtype: object
# FIRST_NAME       Sarath
# LAST_NAME        Sewall
# SALARY             7000
# DEPARTMENT_ID        80
# Name: 61, dtype: object
# FIRST_NAME         Clara
# LAST_NAME        Vishney
# SALARY             10500
# DEPARTMENT_ID         80
# Name: 62, dtype: object
# FIRST_NAME       Danielle
# LAST_NAME          Greene
# SALARY               9500
# DEPARTMENT_ID          80
# Name: 63, dtype: object
# FIRST_NAME       David
# LAST_NAME          Lee
# SALARY            6800
# DEPARTMENT_ID       80
# Name: 65, dtype: object
# FIRST_NAME       Sundar
# LAST_NAME          Ande
# SALARY             6400
# DEPARTMENT_ID        80
# Name: 66, dtype: object
# FIRST_NAME        Lisa
# LAST_NAME         Ozer
# SALARY           11500
# DEPARTMENT_ID       80
# Name: 68, dtype: object
# FIRST_NAME       Harrison
# LAST_NAME           Bloom
# SALARY              10000
# DEPARTMENT_ID          80
# Name: 69, dtype: object
# FIRST_NAME       Tayler
# LAST_NAME           Fox
# SALARY             9600
# DEPARTMENT_ID        80
# Name: 70, dtype: object
# FIRST_NAME       Elizabeth
# LAST_NAME            Bates
# SALARY                7300
# DEPARTMENT_ID           80
# Name: 72, dtype: object
# FIRST_NAME       Sundita
# LAST_NAME          Kumar
# SALARY              6100
# DEPARTMENT_ID         80
# Name: 73, dtype: object
# FIRST_NAME       Ellen
# LAST_NAME         Abel
# SALARY           11000
# DEPARTMENT_ID       80
# Name: 74, dtype: object
# FIRST_NAME       Alyssa
# LAST_NAME        Hutton
# SALARY             8800
# DEPARTMENT_ID        80
# Name: 75, dtype: object
# FIRST_NAME       Jonathon
# LAST_NAME          Taylor
# SALARY               8600
# DEPARTMENT_ID          80
# Name: 76, dtype: object
# FIRST_NAME             Jack
# LAST_NAME        Livingston
# SALARY                 8400
# DEPARTMENT_ID            80
# Name: 77, dtype: object
# FIRST_NAME       Charles
# LAST_NAME        Johnson
# SALARY              6200
# DEPARTMENT_ID         80
# Name: 79, dtype: object
# FIRST_NAME       Winston
# LAST_NAME         Taylor
# SALARY              3200
# DEPARTMENT_ID         50
# Name: 80, dtype: object
# FIRST_NAME         Jean
# LAST_NAME        Fleaur
# SALARY             3100
# DEPARTMENT_ID        50
# Name: 81, dtype: object
# FIRST_NAME       Girard
# LAST_NAME         Geoni
# SALARY             2800
# DEPARTMENT_ID        50
# Name: 83, dtype: object
# FIRST_NAME        Nandita
# LAST_NAME        Sarchand
# SALARY               4200
# DEPARTMENT_ID          50
# Name: 84, dtype: object
# FIRST_NAME       Alexis
# LAST_NAME          Bull
# SALARY             4100
# DEPARTMENT_ID        50
# Name: 85, dtype: object
# FIRST_NAME           Julia
# LAST_NAME        Dellinger
# SALARY                3400
# DEPARTMENT_ID           50
# Name: 86, dtype: object
# FIRST_NAME       Anthony
# LAST_NAME         Cabrio
# SALARY              3000
# DEPARTMENT_ID         50
# Name: 87, dtype: object
# FIRST_NAME       Kelly
# LAST_NAME        Chung
# SALARY            3800
# DEPARTMENT_ID       50
# Name: 88, dtype: object
# FIRST_NAME       Jennifer
# LAST_NAME           Dilly
# SALARY               3600
# DEPARTMENT_ID          50
# Name: 89, dtype: object
# FIRST_NAME       Randall
# LAST_NAME        Perkins
# SALARY              2500
# DEPARTMENT_ID         50
# Name: 91, dtype: object
# FIRST_NAME       Sarah
# LAST_NAME         Bell
# SALARY            4000
# DEPARTMENT_ID       50
# Name: 92, dtype: object
# FIRST_NAME       Britney
# LAST_NAME        Everett
# SALARY              3900
# DEPARTMENT_ID         50
# Name: 93, dtype: object
# FIRST_NAME       Vance
# LAST_NAME        Jones
# SALARY            2800
# DEPARTMENT_ID       50
# Name: 95, dtype: object
# FIRST_NAME       Alana
# LAST_NAME        Walsh
# SALARY            3100
# DEPARTMENT_ID       50
# Name: 96, dtype: object
# FIRST_NAME        Kevin
# LAST_NAME        Feeney
# SALARY             3000
# DEPARTMENT_ID        50
# Name: 97, dtype: object
# FIRST_NAME         Donald
# LAST_NAME        OConnell
# SALARY               2600
# DEPARTMENT_ID          50
# Name: 98, dtype: object
# FIRST_NAME       Douglas
# LAST_NAME          Grant
# SALARY              2600
# DEPARTMENT_ID         50
# Name: 99, dtype: object
# FIRST_NAME       Jennifer
# LAST_NAME          Whalen
# SALARY               4400
# DEPARTMENT_ID          10
# Name: 100, dtype: object
# FIRST_NAME        Pat
# LAST_NAME         Fay
# SALARY           6000
# DEPARTMENT_ID      20
# Name: 102, dtype: object
# FIRST_NAME        Susan
# LAST_NAME        Mavris
# SALARY             6500
# DEPARTMENT_ID        40
# Name: 103, dtype: object
# FIRST_NAME       Shelley
# LAST_NAME        Higgins
# SALARY             12008
# DEPARTMENT_ID        110
# Name: 105, dtype: object

def Q8():
    print(employees.sort_values('DEPARTMENT_ID'))
# Q8()
#      EMPLOYEE_ID FIRST_NAME   LAST_NAME  ... COMMISSION_PCT MANAGER_ID DEPARTMENT_ID
# 78           178  Kimberely       Grant  ...           0.15        149             0
# 100          200   Jennifer      Whalen  ...           0.00        101            10
# 101          201    Michael   Hartstein  ...           0.00        100            20
# 102          202        Pat         Fay  ...           0.00        201            20
# 19           119      Karen  Colmenares  ...           0.00        114            30
# ..           ...        ...         ...  ...            ...        ...           ...
# 10           110       John        Chen  ...           0.00        108           100
# 9            109     Daniel      Faviet  ...           0.00        108           100
# 8            108      Nancy   Greenberg  ...           0.00        101           100
# 105          205    Shelley     Higgins  ...           0.00        101           110
# 106          206    William       Gietz  ...           0.00        205           110

# [107 rows x 11 columns]

def Q9():
    print(employees.sort_values('FIRST_NAME', ascending=False))
# Q9()
#      EMPLOYEE_ID FIRST_NAME  LAST_NAME  ... COMMISSION_PCT MANAGER_ID DEPARTMENT_ID
# 80           180    Winston     Taylor  ...           0.00        120            50
# 106          206    William      Gietz  ...           0.00        205           110
# 71           171    William      Smith  ...           0.15        148            80
# 95           195      Vance      Jones  ...           0.00        123            50
# 6            106      Valli  Pataballa  ...           0.00        103            60
# ..           ...        ...        ...  ...            ...        ...           ...
# 15           115  Alexander       Khoo  ...           0.00        114            30
# 3            103  Alexander     Hunold  ...           0.00        102            60
# 47           147    Alberto  Errazuriz  ...           0.30        100            80
# 96           196      Alana      Walsh  ...           0.00        124            50
# 21           121       Adam      Fripp  ...           0.00        100            50

# [107 rows x 11 columns]

def Q10():
    print(employees[['FIRST_NAME','LAST_NAME','SALARY','MANAGER_ID']][employees['MANAGER_ID']==0])
# Q10()
#   FIRST_NAME LAST_NAME  SALARY  MANAGER_ID
# 0     Steven      King   24000           0

def Q11():
    print(employees[['FIRST_NAME','LAST_NAME','SALARY','MANAGER_ID']][employees['MANAGER_ID'].notna()])
# Q11()
#  FIRST_NAME LAST_NAME  SALARY  MANAGER_ID
# 0     Steven      King   24000           0
#     FIRST_NAME LAST_NAME  SALARY  MANAGER_ID
# 0       Steven      King   24000           0
# 1        Neena   Kochhar   17000         100
# 2          Lex   De Haan   17000         100
# 3    Alexander    Hunold    9000         102
# 4        Bruce     Ernst    6000         103
# ..         ...       ...     ...         ...
# 102        Pat       Fay    6000         201
# 103      Susan    Mavris    6500         101
# 104    Hermann      Baer   10000         101
# 105    Shelley   Higgins   12008         101
# 106    William     Gietz    8300         205

# [107 rows x 4 columns]

def Q12():
    print(employees[['FIRST_NAME','LAST_NAME','SALARY','DEPARTMENT_ID']][employees['DEPARTMENT_ID']==70])
    print(employees[['FIRST_NAME','LAST_NAME','SALARY','DEPARTMENT_ID']][employees['DEPARTMENT_ID']==90])
# Q12()
#     FIRST_NAME LAST_NAME  SALARY  DEPARTMENT_ID
# 104    Hermann      Baer   10000             70
#   FIRST_NAME LAST_NAME  SALARY  DEPARTMENT_ID
# 0     Steven      King   24000             90
# 1      Neena   Kochhar   17000             90
# 2        Lex   De Haan   17000             90