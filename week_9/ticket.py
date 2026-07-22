
# Mapping of priority level -> technician in charge
TECHNICIAN_MAP = {
    "High": "Sami",
    "Medium": "Amal",
    "Low": "Lebron"
}


def create_ticket():
    """
    Collects ticket details from the user, validates the priority level,
    and returns all the information needed to display the ticket.
    """
    print("=== IT Helpdesk Ticket ===")

    student_name = input("Student Name : ")
    student_id = input("Student ID : ")
    issue = input("Issue : ")
    location = input("Location : ")

    # Keep asking until a valid priority is entered
    while True:
        priority = input("Priority (High/Medium/Low): ").strip().capitalize()
        if priority in TECHNICIAN_MAP:
            break
        print("Invalid priority. Please enter High, Medium, or Low.")

    # Assign technician based on priority level
    technician = TECHNICIAN_MAP[priority]
    status = "Pending"

    # Return everything the main program / display module needs
    return student_name, student_id, issue, location, priority, technician, status