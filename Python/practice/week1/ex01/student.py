def check_is_user_student():
        """
        Asks the user for if they are a student or not.
        If user answers "yes" the function returns True, 
        otherwise False.
        """
        while True:
            answer = input("Are you a student? ")
            if answer.lower() == "yes":
                return True
            elif answer.lower() == "no":
                return False


def main():
    """
    Asks for user's age, their student status 
    and decides eligibilty for a discount. 
    """
    age = int(input("How old are you? "))
    student_status = check_is_user_student()

    if (age < 25 and student_status) or age >= 65:
        print("You quality for a discount")
    else:
        print("You do not qualify for a discount")



if __name__ == "__main__":
     main()