import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",  
    database="employeedb"
)
cursor = conn.cursor()

# Function to add employee
def add_employee():
    name = input("Enter name: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")
    address = input("Enter address: ")
    post = input("Enter post: ")
    salary = float(input("Enter salary: "))
    query = "INSERT INTO employees (name, email, phone, address, post, salary) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (name, email, phone, address, post, salary)
    cursor.execute(query, values)
    conn.commit()
    print("✅ Employee added successfully!")

# Function to display all records
def display_employees():
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Function to update employee details
def update_employee():
    emp_id = input("Enter employee ID to update: ")
    email = input("Enter new email: ")
    phone = input("Enter new phone: ")
    address = input("Enter new address: ")
    query = "UPDATE employees SET email=%s, phone=%s, address=%s WHERE id=%s"
    values = (email, phone, address, emp_id)
    cursor.execute(query, values)
    conn.commit()
    print("✅ Employee updated successfully!")

# Function to promote employee
def promote_employee():
    emp_id = input("Enter employee ID to promote: ")
    increment = float(input("Enter salary increment: "))
    query = "UPDATE employees SET salary = salary + %s WHERE id = %s"
    values = (increment, emp_id)
    cursor.execute(query, values)
    conn.commit()
    print("✅ Employee promoted successfully!")

# Function to delete employee
def delete_employee():
    emp_id = input("Enter employee ID to delete: ")
    query = "DELETE FROM employees WHERE id = %s"
    cursor.execute(query, (emp_id,))
    conn.commit()
    print("✅ Employee deleted successfully!")

# Function to search employee
def search_employee():
    emp_id = input("Enter employee ID to search: ")
    query = "SELECT * FROM employees WHERE id = %s"
    cursor.execute(query, (emp_id,))
    row = cursor.fetchone()
    if row:
        print("Employee Details:", row)
    else:
        print("❌ Employee not found.")

# Menu-driven interface
def menu():
    while True:
        print("\n====== Employee Management System ======")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Update Employee")
        print("4. Promote Employee")
        print("5. Delete Employee")
        print("6. Search Employee")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            display_employees()
        elif choice == '3':
            update_employee()
        elif choice == '4':
            promote_employee()
        elif choice == '5':
            delete_employee()
        elif choice == '6':
            search_employee()
        elif choice == '7':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

menu()

# Close the connection at the end
cursor.close()
conn.close()
