
choice = "Y"

# Use loop condition to keep the user choice open 
while choice == "Y":

    # Ask the user to enter three marks of his quizzes
    quiz_1 = float(input("Enter Quiz 1 mark: "))
    quiz_2 = float(input("Enter Quiz 2 mark: "))
    quiz_3 = float(input("Enter Quiz 3 mark: "))

    # Average Calculation
    
    average = (quiz_1 + quiz_2 + quiz_3)/ 3

    # Check if the student passes or fails
    if average >= 50:
        print("Congratulations, You've passed")
    else:
        print("Unfortunately, you've failed.")

    # Ask the user if he wants to continue or not
    choice = input("Continue? Select Y/N: ").upper()

print("Program Ended")