#Python Module: Module4


from datetime import date,datetime,timedelta
import mysql.connector


def UpdateRecord():
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="Payroll")
        mycursor=mydb.cursor()
        eno=int(input("Enter Employee Number to be Updated: "))
        sql="select * from EmployeeDetails where empno=%s"
        val=(eno,)
        #mycursor.execute(sql,val)
        print("Enter New Record")
        ename=input("Enter Employee Name: ")
        ejob=input("Enter Employee Job: ")
        ebasic=int(input("Enter Basic Salary: "))
        if ejob.upper()=="OFFICER":
            eda=ebasic*0.5
            ehra=ebasic*0.35
            etax=ebasic*0.2
        elif ejob.upper()=="MANAGER":
            eda=ebasic*0.45
            ehra=ebasic*0.30
            etax=ebasic*0.15
        else:
            eda=ebasic*0.40
            ehra=ebasic*0.25
            etax=ebasic*0.1
        

        egross=ebasic+eda+ehra+etax
        enet=egross-etax
        #rec=(eno,ename,ejob,ebasic,eda,ehra,egross,etax,enet)
            
        sql="update EmployeeDetails set ename=%s,job=%s,basicsalary=%s ,DA=%s, HRA=%s, grosssalary=%s, tax=%s, netsalary=%s where empno=%s"
        val=(ename,ejob,ebasic,eda,ehra,egross,etax,enet,eno)
        mycursor.execute(sql,val)

        
        sql2="update EmployeeDetails set ename=%s,job=%s,basicsalary=%s where empno=%s"
        val2=(ename,ejob,ebasic,eno)
        mycursor.execute(sql2,val2)
        mydb.commit()
        mycursor.close()
        mydb.close()
        print("Records Updated Successfully..........")

    except Exception as ex:
        print("Something went wrong",ex)
        
    mydb.close()

