#STDUENT NAME, EMAIL,NUMBER ... QUIT 

list, lists = {}, {}

while True:
    print("\nMain Menu:")
    print("1. Show student list")
    print("2. Show student details")
    print("3. Add new student")
    print("4. Update student details")
    print("5. Remove a student")
    print("6. Show deleted list")
    print("7. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        print("Students List:")
        print("\n".join(f"ID: {id}, Name: {info[0]}, Email: {info[1]}" for id, info in list.items()) or "empty")
    
    elif choice == "2":
        while (detail_choice := input("\nShow Student Details:\n1. Enter student ID\n2. Quit to main menu\n3. exit quit\nEnter your choice: ")) != "2":
            if detail_choice == "3": exit()
            student_id = input("Enter student ID or press 0 to quit: ")
            if student_id == "0": break
            print(f"ID: {student_id}, Name: {list[student_id][0]}, Email: {list[student_id][1]}, Phone Number: {list[student_id][2]}" if student_id in list else "Invalid ID")
    
    elif choice == "3":
        while (add_choice := input("\nAdd New Student:\n1. Enter student details\n2. Quit to main menu\n3. exit quit\nEnter your choice: ")) != "2":
            if add_choice == "3": exit()
            name = input("Enter student name or press 0 to quit: ")
            if name == '0': break
            email = input("Enter student email or press 0 to quit: ")
            if email == '0': break
            phone_number = input("Enter student phone number or press 0 to quit: ")
            if phone_number == '0': break
            
            if "@" not in email or "." not in email: print("Invalid email"); continue
            if (phone_number.startswith("+") and len(phone_number) != 13) or (not phone_number.startswith("+") and len(phone_number) != 10) or not phone_number.isdigit(): print("Invalid phone number format."); continue
            
            if any(info[1] == email or info[2] == phone_number for info in list.values()): print("already exists."); continue
            
            list[str(len(list) + 1)] = (name, email, phone_number)
            print("Student added sucessfully.")
    
    elif choice == "4":
        while (update_choice := input("\nUpdate Student Details:\n1. Enter student ID to update\n2. Quit to main menu\n3. exit quit\nEnter your choice: ")) != "2":
            if update_choice == "3": exit()
            student_id = input("Enter student ID or press 0 to quit: ")
            if student_id == "0": break
            
            if student_id in list:
                field_choice = input("Which field do you want to update?\n1. Name\n2. Email\n3. Phone Number\n4. Quit\nEnter your choice: ")
                if field_choice == "1":
                    list[student_id] = (input("Enter new name: "), list[student_id][1], list[student_id][2])
                    print("Name updated successfully.")
                elif field_choice == "2":
                    new_email = input("Enter new email: ")
                    if "@" in new_email and "." in new_email:
                        list[student_id] = (list[student_id][0], new_email, list[student_id][2])
                        print("Email updated successfully.")
                    else: print("Invalid email format.")
                elif field_choice == "3":
                    new_phone_number = input("Enter new phone number: ")
                    if (new_phone_number.startswith("+") and len(new_phone_number) == 13) or (not new_phone_number.startswith("+") and len(new_phone_number) == 10) and new_phone_number.isdigit():
                        list[student_id] = (list[student_id][0], list[student_id][1], new_phone_number)
                        print("Phone number updated successfully.")
                elif field_choice == "4": continue
                else: print("Invalid choice")
            else: print("Invalid ID")
    
    elif choice == "5":
        while (remove_choice := input("\nRemove a Student:\n1. Enter student ID to delete\n2. Quit to main menu\n3. exit quit\nEnter your choice: ")) != "2":
            if remove_choice == "3": exit()
            student_id = input("Enter student ID or press 0 to quit: ")
            if student_id == '0': break
            if student_id in list:
                lists[student_id] = list.pop(student_id)
                print("Student removed successfully.")
            else: print("Invalid ID, .")
    
    elif choice == "6":
        print("Deleted Students List:")
        print("\n".join(f"ID: {id}, Name: {info[0]}, Email: {info[1]}" for id, info in lists.items()) or "empty")
    
    elif choice == "7":
        if input("press quit: ").lower() == "quit": break
    
    else: print("Invalid")
