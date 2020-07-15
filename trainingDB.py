import mysql.connector
import os
os.system('cls')

global name,address,search,x,initDecision

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="", # Your Database password here
  database="myPythondatabase" # Your Database name here
)

print(mydb)

mycursor = mydb.cursor()

print("-----------------------------Welcome to Python Database App--------------------------")




def save():
    name=input("please enter your name   ")
    print("                            ")
    address=input("please enter your Address   ")

    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = (name,address)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
    defDecision()



def searchQ():
    search=input("please enter a word you are searching for   ")
    
    sql = "SELECT * FROM customers WHERE name LIKE %s OR address LIKE %s"
    adr = ('%' + search + '%','%' + search + '%')

    mycursor.execute(sql, adr)
    
    myresult = mycursor.fetchall()
    
    for x in myresult:
      print(x)
    decision=input(" Do you want to redifine Using result ID? Type Y for Yes or N for NO ")
    if decision=='Y' or decision=='y':
      rId=input("Enter the ID of your specific Search  ")
      sql = "SELECT * FROM customers WHERE id = %s "
      adr = (rId,)
      mycursor.execute(sql, adr)
      myresult = mycursor.fetchall()
      for x in myresult:
        print(x)
      
      edit=input(" Do you want to Edit the record? Y for Yes, N for No")
      if edit=='Y' or edit=='y':
         
          
          address=input("please enter the new Address   ")

          sql="UPDATE customers SET address = %s WHERE id = %s "
          adr = (address,rId,)
          mycursor.execute(sql, adr)
          mydb.commit()
          print(mycursor.rowcount, "record Updated.")

      else:
          defDecision()
          
      defDecision()
    else:
        print(" End of current search ")
        defDecision()



def defDecision():
    initDecision=input(" Type N to save new record, S to search for a record ")

    if initDecision=='N' or initDecision=='n':
        save()
    elif initDecision=='S' or initDecision=='s':
        searchQ()
    else:
        print(" Invalid Entry ")
        defDecision()



defDecision()
