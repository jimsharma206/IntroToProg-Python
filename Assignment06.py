# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <James Sharma>,<09/04/2024>,<Assignment 06>
# ------------------------------------------------------------------------------------------ #

import json  # Required for file operations

# Define Constants
MENU: str = '''\n
---- Course Registration Program ----

  Select from the following menu:

    1. Register a Student for a Course

    2. Show current data

    3. Save data to a file and display saved data

    4. Exit the program

-----------------------------------------\n'''
FILE_NAME: str = "Enrollments.json"


class FileProcessor:
    """  Performs File Processing Tasks """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list) -> list:
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param student_data: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        try:
            with open(file_name, "r") as file:
                student_data = json.load(file)
        except FileNotFoundError:
            print(f"File {file_name} not found. Starting with an empty list.")
        except Exception as e:
            print(f"An error occurred while loading data from file: {e}")
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list) -> None:
        """ Writes data from a list of dictionary rows to a File and displays it

        :param file_name: (string) with name of file:
        :param student_data: (list) you want to save to file:
        :return: nothing
        """
        try:
            with open(file_name, "w") as file:
                json.dump(student_data, file)
            print("Data successfully saved to file.")
            
            # Displaying the saved data
            print("Data saved in the file:")
            for student in student_data:
                print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['Course']}")
        except Exception as e:
            print("-- Technical Error Message --")
            print("Built-In Python error info:")
            print(e, e.__doc__, type(e), sep='\n')


class IO:
    """ Performs Input and Output Tasks """

    @staticmethod
    def output_menu(menu: str) -> str:
        """ Displays a menu of choices to the user

        :param menu: (string) the menu string to display:
        :return: nothing
        """
        print(menu)
        menu_choice = input("Please choose an option (1, 2, 3, or 4): ")
        print() 
        return menu_choice

    @staticmethod
    def input_student_data(student_data: list) -> list:
        """ Gets data for a new student

        :param student_data: (list) you want filled with input data:
        :return: (list) with new student data added
        """
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

            student = {"FirstName": student_first_name, "LastName": student_last_name, "Course": course_name}
            student_data.append(student)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        return student_data

    @staticmethod
    def output_student_courses(student_data: list) -> None:
        """ Shows the current student courses

        :param student_data: (list) of dictionaries with student data:
        :return: nothing
        """
        print("-" * 50)
        for student in student_data:
            print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['Course']}")
        print("-" * 50)


# Main Body of Script  ---------------------------------------------------- #

# Load existing data from file
students = []  # Represents a table of student data as a list of dictionaries
students = FileProcessor.read_data_from_file(FILE_NAME, students)

# Main Program Loop
while True:
    menu_choice = IO.output_menu(MENU)

    # Input user data
    if menu_choice == "1":
        students = IO.input_student_data(students)

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(students)

    # Save the data to a file and display saved data
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(FILE_NAME, students)

    # Stop the loop
    elif menu_choice == "4":
        print("Program Ended")
        break

    else:
        print("Please only choose option 1, 2, 3, or 4")


