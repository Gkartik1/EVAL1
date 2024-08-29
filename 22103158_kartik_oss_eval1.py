
attendance_list = []

def mark_present(student_name: str):
  
    if student_name not in attendance_list:
        attendance_list.append(student_name)
        print(f"{student_name} has been marked as present.")
    else:
        print(f"{student_name} is already marked as present.")

def remove_student(student_name: str):
    
    if student_name in attendance_list:
        attendance_list.remove(student_name)
        print(f"{student_name} has been removed from the attendance list.")
    else:
        print(f"{student_name} is not in the attendance list.")

def is_present(student_name: str) -> bool:
    """Check if a student is marked as present."""
    return student_name in attendance_list

def display_attendance():
    
    if attendance_list:
        print("Students present today:")
        for student in attendance_list:
            print(f"- {student}")
    else:
        print("No students are present today.")


if __name__ == "__main__":
    # Mark some students as present
    mark_present("kartik")
    mark_present("rahul")
    mark_present("vivek")

    # Check if students are present
    print(f"Is kartik present? {'Yes' if is_present('kartik') else 'No'}")
    print(f"Is rahul present? {'Yes' if is_present('rahul') else 'No'}")

    # Display the attendance
    display_attendance()

    # Remove a student and display the updated attendance
    remove_student("vivek")
    display_attendance()
