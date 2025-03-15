from models import Admin
from database import DatabaseHandler, excel_available
import os

def display_menu():
    """Display the main menu options."""
    print("\n===== Student Management System =====")
    print("1. Add a student")
    print("2. View all students")
    print("3. Update a student's information")
    print("4. Remove a student")
    print("5. Search for a student")  # Bonus feature
    print("6. Export data")  # Modified to include Excel export
    print("7. Save and exit")
    print("=====================================")

def get_valid_input(prompt, input_type=str, validation_func=None):
    """Get and validate user input."""
    while True:
        try:
            user_input = input_type(input(prompt))
            if validation_func and not validation_func(user_input):
                print("Invalid input. Please try again.")
                continue
            return user_input
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")

def add_student_menu(admin):
    """Menu for adding a new student."""
    print("\n--- Adding a New Student ---")
    
    name = get_valid_input("Enter student name: ")
    age = get_valid_input("Enter student age: ", int, lambda x: x > 0)
    gender = get_valid_input("Enter student gender: ")
    student_id = get_valid_input("Enter student ID: ")
    
    result = admin.add_student(name, age, gender, student_id)
    print(result)

def update_student_menu(admin):
    """Menu for updating a student's information."""
    print("\n--- Updating Student Information ---")
    
    student_id = get_valid_input("Enter student ID to update: ")
    student = admin.find_student_by_id(student_id)
    
    if not student:
        print(f"No student found with ID {student_id}.")
        return
    
    print(f"Updating information for {student.name} (ID: {student_id})")
    print("Leave blank to keep current value")
    
    name = input(f"Enter new name (current: {student.name}): ")
    
    age_str = input(f"Enter new age (current: {student.age}): ")
    age = int(age_str) if age_str and age_str.isdigit() else None
    
    gender = input(f"Enter new gender (current: {student.gender}): ")
    
    # Handle courses
    print(f"Current courses: {', '.join(student.courses) if student.courses else 'None'}")
    course_action = get_valid_input("Do you want to (1) Add a course or (2) Remove a course or (3) Skip? ", 
                                   int, lambda x: x in [1, 2, 3])
    
    if course_action == 1:
        course = get_valid_input("Enter course name to add: ")
        print(student.enroll_course(course))
    elif course_action == 2:
        if not student.courses:
            print("No courses to remove.")
        else:
            course = get_valid_input("Enter course name to remove: ")
            print(student.remove_course(course))
    
    result = admin.update_student(student_id, name if name else None, 
                               age if age_str else None, 
                               gender if gender else None)
    print(result)

def remove_student_menu(admin):
    """Menu for removing a student."""
    print("\n--- Removing a Student ---")
    
    student_id = get_valid_input("Enter student ID to remove: ")
    
    # Confirm deletion
    confirm = get_valid_input(f"Are you sure you want to remove student with ID {student_id}? (y/n): ")
    if confirm.lower() != 'y':
        print("Operation cancelled.")
        return
    
    result = admin.delete_student(student_id)
    print(result)

def search_student_menu(admin):
    """Menu for searching for students."""
    print("\n--- Search for Students ---")
    
    query = get_valid_input("Enter name or ID to search: ")
    result = admin.search_students(query)
    print(result)

def export_data_menu(admin):
    """Menu for exporting student data."""
    print("\n--- Export Student Data ---")
    
    # Check if there are students to export
    if not admin.students:
        print("No students to export. Please add students first.")
        return
    
    print("1. Export to CSV")
    if excel_available:
        print("2. Export to Excel")
    
    max_choice = 2 if excel_available else 1
    choice = get_valid_input(f"Enter your choice (1-{max_choice}): ", int, lambda x: 1 <= x <= max_choice)
    
    if choice == 1:
        # CSV export
        filename = get_valid_input("Enter CSV filename (default: students.csv): ")
        if not filename:
            filename = "students.csv"
        elif not filename.endswith('.csv'):
            filename += '.csv'
        
        result = admin.db_handler.export_to_csv(admin.students, filename)
        print(result)
        print(f"\nNote: The file is saved in the directory: {os.getcwd()}")
    elif choice == 2 and excel_available:
        # Excel export
        filename = get_valid_input("Enter Excel filename (default: students.xlsx): ")
        if not filename:
            filename = "students.xlsx"
        elif not filename.endswith('.xlsx'):
            filename += '.xlsx'
        
        result = admin.db_handler.export_to_excel(admin.students, filename)
        print(result)
        print(f"\nNote: The file is saved in the directory: {os.getcwd()}")

def main():
    """Main function to run the Student Management System."""
    print("Welcome to the Student Management System!")
    print(f"Current working directory: {os.getcwd()}")
    
    # Initialize the database handler and admin
    db_handler = DatabaseHandler()
    admin = Admin(db_handler)
    
    while True:
        display_menu()
        
        choice = get_valid_input("Enter your choice (1-7): ", int, lambda x: 1 <= x <= 7)
        
        if choice == 1:
            add_student_menu(admin)
        elif choice == 2:
            print("\n--- All Students ---")
            print(admin.view_students())
        elif choice == 3:
            update_student_menu(admin)
        elif choice == 4:
            remove_student_menu(admin)
        elif choice == 5:
            search_student_menu(admin)
        elif choice == 6:
            export_data_menu(admin)
        elif choice == 7:
            admin.save_students()
            print("Data saved. Exiting the program...")
            break

if __name__ == "__main__":
    main()