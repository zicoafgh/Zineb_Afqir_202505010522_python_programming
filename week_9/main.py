
from ticket import create_ticket
from display import display_ticket


def main():
    # Create a new ticket by collecting details from the user
    student_name, student_id, issue, location, priority, technician, status = create_ticket()

    # Check that all required fields were provided before displaying
    if student_name and student_id and issue and location and priority:
        display_ticket(student_name, student_id, issue, location, priority, technician, status)
    else:
        print("Error: Missing required ticket information.")


if __name__ == "__main__":
    main()
