# IT Helpdesk Ticket Registration System

## Purpose of the Application
This application was built for the IT Support team of City University Malaysia.
This program lets a student (or staff member) register a ticket by entering
their details, describing the issue (such as unable to log in LMS, WIFI
connection problem), and selecting a priority level. The ticket is then
automatically assigned to the correct technician and displayed in a clear,
readable format.

## Tech Stack
1. Language: Python 3
2. Modules: Built-in input()/print() only
3. Structure: Modular design split across three files:
   - main.py – program entry point
   - ticket.py – collects ticket details and assigns a technician
   - display.py – formats and displays the final ticket

## How to Use
1. Make sure Python 3 is installed on your machine.
2. Open a terminal and navigate to the week_9 directory.
3. Run the program:

python3 main.py

4. When prompted, enter the following information:
Student Name
Student ID
Issue
Location
Priority (High / Medium / Low)
5. The program will validate the priority level and automatically assign a technician based on it:
High → Sami
Medium → Amal
Low → Lebron
6. A formatted ticket summary will be printed showing the ticket details, assigned technician, and status (Pending).

## Demonstration
_Attach a screen recording (video/GIF) here showing the application running from start to finish._

## Demo to follow 
## Demonstration
  [Click here to watch the demo video](demo2.mp4)
