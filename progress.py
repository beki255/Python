HRMS = "file.txt"  # File to store all entities IN HRMS
def load_data():
    data = {
        "Department": [],
        "Client": [],
        "Employee": [],
        "Position": [],
        "Allowance": [],
        "SalaryScale": [],
        "Vehicle": [],
        "Attendance": [],
        "Department_Client": [],
        "Employee_Position": [],
        "Users": []  
    }
    try:
        with open(HRMS, "r") as file:
            lines = file.readlines()
            entity = ""
            for line in lines:
                if not line.strip():
                    continue
                if line.startswith("=== "):
                    entity = line.strip()[4:]
                else:
                    fields = line.strip().split(',')
                    data[entity].append(fields)
    except FileNotFoundError:
        return data
    return data

def save_data(data):
    with open(HRMS, "w") as file:
        for entity, records in data.items():
            file.write(f"=== {entity}\n")
            for record in records:
                file.write(','.join(record) + '\n')

def insert_data(entity, fields):
    data = load_data()
    data[entity].append(fields)
    save_data(data)
    print(f"Data inserted into {entity}.")

def display_data():
    data = load_data()
    for entity, records in data.items():
        print(f"\n{entity}:")
        if records:
            print(f"{' | '.join(records[0])}")  
            print('--' * 56)  
            for record in records[1:]:
                print(f"{' | '.join(record)}")
        else:
            print("No data available.")

def update_data(entity, index, new_fields):
    data = load_data()
    entity_lower = entity.lower()
    matching_entity = None
    for ent in data.keys():
        if ent.lower() == entity_lower:
            matching_entity = ent
            break
    if matching_entity and 0 <= index < len(data[matching_entity]):
        data[matching_entity][index] = new_fields
        save_data(data)
        print(f"Data in {matching_entity} updated.")
    else:
        print("Invalid entity or index.")

def delete_data(entity, index):
    data = load_data()
    entity_lower = entity.lower()
    matching_entity = None
    for ent in data.keys():
        if ent.lower() == entity_lower:
            matching_entity = ent
            break
    if matching_entity and 0 <= index < len(data[matching_entity]):
        data[matching_entity].pop(index)
        save_data(data)
        print(f"Data in {matching_entity} deleted.")
    else:
        print("Invalid entity or index.")

def input_data(entity):
    if entity == "Department":
        print("\n=========================================")
        print("Enter Department data:")
        department_id = input("DepartmentId: ")
        department_name = input("DepartmentName: ")
        department_description = input("DepartmentDescription: ")
        fields = [department_id, department_name, department_description]
        insert_data(entity, fields)
        
    elif entity == "Client":
        print("\n=========================================")
        print("Enter Client data:")
        client_id = input("ClientId: ")
        client_name = input("ClientName: ")
        contact_person = input("ContactPerson: ")
        email = input("Email: ")
        phone = input("Phone: ")
        address = input("Address: ")
        city = input("City: ")
        state = input("State: ")
        postcode = input("PostCode: ")
        fields = [client_id, client_name, contact_person, email, phone, address, city, state, postcode]
        insert_data(entity, fields)
        
    elif entity == "Employee":
        print("\n=========================================")
        print("Enter Employee data:")
        employee_id = input("EmployeeId: ")
        ss_number = input("SSNumber: ")
        first_name = input("FirstName: ")
        middle_name = input("MiddleName: ")
        last_name = input("LastName: ")
        gender = input("Gender (Male/Female/): ")
        dob = input("DOB (YYYY-MM-DD): ")
        email = input("Email: ")
        mobile = input("Mobile: ")
        address_line = input("AddressLine: ")
        city = input("City: ")
        state = input("State: ")
        postcode = input("PostCode: ")
        department_id = input("DepartmentId: ")
        fields = [employee_id, ss_number, first_name, last_name, middle_name, gender, dob, email, mobile, address_line, city, state, postcode, department_id]
        insert_data(entity, fields)
        
    elif entity == "Position":
        print("\n=========================================")
        print("Enter Position data:")
        position_id = input("PositionId: ")
        position_name = input("PositionName: ")
        position_description = input("PositionDescription: ")
        details = input("Details: ")
        fields = [position_id, position_name, position_description, details]
        insert_data(entity, fields)
        
    elif entity == "Allowance":
        print("\n=========================================")
        print("Enter Allowance data:")
        allowance_id = input("AllowanceId: ")
        allowance_name = input("AllowanceName: ")
        allowance_description = input("AllowanceDescription: ")
        amount = input("Amount: ")
        position_id = input("PositionId: ")
        fields = [allowance_id, allowance_name, allowance_description, amount, position_id]
        insert_data(entity, fields)
        
    elif entity == "SalaryScale":
        print("\n=========================================")
        print("Enter SalaryScale data:")
        salary_scale_code = input("SalaryScaleCode: ")
        salary_scale_name = input("SalaryScaleName: ")
        salary_scale_description = input("SalaryScaleDescription: ")
        minimum_salary = input("MinimumSalary: ")
        maximum_salary = input("MaximumSalary: ")
        position_id = input("PositionId: ")
        fields = [salary_scale_code, salary_scale_name, salary_scale_description, minimum_salary, maximum_salary, position_id]
        insert_data(entity, fields)
        
    elif entity == "Vehicle":
        print("\n=========================================")
        print("Enter Vehicle data:")
        vehicle_id = input("VehicleId: ")
        vin = input("VIN: ")
        registration_no = input("RegistrationNo: ")
        year = input("Year: ")
        make = input("Make: ")
        model = input("Model: ")
        color = input("Color: ")
        position_id = input("PositionId: ")
        fields = [vehicle_id, vin, registration_no, year, make, model, color, position_id]
        insert_data(entity, fields)
        
    elif entity == "Attendance":
        print("\n=========================================")
        print("Enter Attendance data:")
        attendance_id = input("AttendanceId: ")
        employee_id = input("EmployeeId: ")
        date = input("Date (YYYY-MM-DD): ")
        time_in = input("TimeIn: ")
        time_out = input("TimeOut: ")
        status = input("Status (Present/Absent/Late): ")
        fields = [attendance_id, employee_id, date, time_in, time_out, status]
        insert_data(entity, fields)
        
    elif entity == "Department_Client":
        print("\n=========================================")
        print("Enter Department_Client data:")
        department_id = input("DepartmentId: ")
        client_id = input("ClientId: ")
        fields = [department_id, client_id]
        insert_data(entity, fields)
        
    elif entity == "Employee_Position":
        print("\n=========================================")
        print("Enter Employee_Position data:")
        employee_id = input("EmployeeId: ")
        position_id = input("PositionId: ")
        fields = [employee_id, position_id]
        insert_data(entity, fields)

def sign_up():
    data = load_data()
    print("Enter the following details to sign up:")
    username = input("Username: ")
    password = input("Password: ")
    for user in data["Users"]:
        if user[0] == username:
            print("User already exists. Please try logging in.")
            return None
    data["Users"].append([username, password])
    save_data(data)
    print("User registered successfully!")
    return username

def log_in():
    data = load_data()
    print("Enter the following details to log in:")
    username = input("Username: ")
    password = input("Password: ")
    for user in data["Users"]:
        if user[0] == username and user[1] == password:
            print(f"Welcome back, {username}!")
            return username
    print("Invalid username or password. Please try again.")
    return None

def main():
    while True:
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print("Welcome to the human resourse Management System")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print("1. Sign Up")
        print("2. Log In")
        print("3. Exit")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        choice = input("Choose an option: ")
        if choice == '1':
            sign_up()
        elif choice == '2':
            user = log_in()
            if user:
                while True:
                    print("\nSelect an operation:")
                    print("1. Insert data")
                    print("2. Display all data")
                    print("3. Update data")
                    print("4. Delete data")
                    print("5. Logout")
                    operation = input("Choose an operation: ")
                    if operation == '1':
                        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                        print("\nChoose an entity to insert data:")
                        print("1. Department")
                        print("2. Client")
                        print("3. Employee")
                        print("4. Position")
                        print("5. Allowance")
                        print("6. SalaryScale")
                        print("7. Vehicle")
                        print("8. Attendance")
                        print("9. Department_Client")
                        print("10. Employee_Position")
                        entity_choice = input("Enter the number of the entity: ")
                        entities = ["Department", "Client", "Employee", "Position", "Allowance", "SalaryScale", "Vehicle", "Attendance", "Department_Client", "Employee_Position"]
                        if entity_choice.isdigit() and int(entity_choice) in range(1, 11):
                            input_data(entities[int(entity_choice) - 1])
                        else:
                            print("Invalid choice.")
                    elif operation == '2':
                        display_data()
                    elif operation == '3':
                        entity = input("Enter the entity to update: ")
                        index = int(input("Enter the index of the record to update: "))
                        new_fields = input("Enter the new fields  respectively (comma-separated): ").split(',')
                        update_data(entity, index, new_fields)
                    elif operation == '4':
                        entity = input("Enter the entity to delete data from: ")
                        index = int(input("Enter the index of the record to delete: "))
                        delete_data(entity, index)
                    elif operation == '5':
                        print("Logging out...")
                        break
                    else:
                        print("Invalid operation.")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
# END OF THE CODE 