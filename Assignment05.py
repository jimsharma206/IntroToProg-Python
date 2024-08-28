# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <James Sharma>,<08/28/2024>, <Assignment 05>
# ------------------------------------------------------------------------------------------ #



# Define Constants
MENU: str = '''---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
-----------------------------------------'''
FILE_NAME: str = "Enrollments.csv"

# Variables
student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
csv_data: str = ""
file = None
menu_choice: str = ""
student_data: list = []  # Represents one row of student data as a list
students: list = []  # Represents a table of student data as a list of lists

# Load existing data from file
try:
    with open(FILE_NAME, "r") as file:
        for line in file:
            # Split each line by comma and strip newline characters
            student_data = line.strip().split(',')
            students.append(student_data)
    print("Data loaded successfully from the file.")
except FileNotFoundError:
    print(f"File {FILE_NAME} not found. Starting with an empty list.")
except Exception as e:
    print(f"An error occurred while loading data from file: {e}")

# Main Program Loop
while True:
    print(MENU)
    menu_choice = input("Please choose an option (1, 2, 3, or 4): ")

    # Input user data
    if menu_choice == "1":
        try:
            student_first_name = input("Enter the student's first name: ")
            if not all(x.isalpha() or x == '-' for x in student_first_name):
                raise ValueError("First name must only contain letters and hyphens.")
            
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("Last name must be a valid string.")

            course_name = input("Please enter the name of the course: ")
            if not all(x.isalpha() or x.isspace() for x in course_name):
               raise ValueError("Course name must only contain letters and spaces.")

            # Append the student data as a list to the students list
            students.append([student_first_name, student_last_name, course_name])
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    # Present the current data
    elif menu_choice == "2":
        print("-" * 50)
        for student in students:
            print(f"Student {student[0]} {student[1]} is enrolled in {student[2]}")
        print("-" * 50)

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            for student in students:
                csv_data = f"{student[0]},{student[1]},{student[2]}\n"
                file.write(csv_data)
            print("Data successfully saved to file.")
        except TypeError as e:
            print("Please check that the data is a valid string.")
            print("-- Technical Error Message --")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("-- Technical Error Message --")
            print("Built-In Python error info:")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file and not file.closed:
                file.close()
                print("File has been closed.")
    
    # Stop the loop
    elif menu_choice == "4":
        print("Program Ended")
        break

    else:
        print("Please only choose option 1, 2, 3, or 4")
