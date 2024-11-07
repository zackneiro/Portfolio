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
            
            
def print_status_price(age, student_status):
     """
     Printing the price of movie ticket for a user.

     This funtcion making decision of user's total price
     on their age and student status and dislpaying message.

     Args:
        age (int) : The user's age
        student_status (boolean) : The status of user
     """
     prices = {
            "Student" : 10,
            "Children" : 8,
            "Seniors" : 7,
            "Adults" : 12,
    }
     if age < 12:
          print(f"As a {age}-year-old kid, your ticket price is ${prices['Children']}.")
     elif age < 25 and student_status:
        print(f"As a {age}-years-old student, your ticket price is ${prices['Student']}.")
     elif age >= 65:
          print(f"As a {age}-year-old senior, your ticket price is ${prices['Seniors']}.")
     else:
          print(f"As a {age}-year-old adult, your ticket price is ${prices['Adults']}.")
          

def main():
    """
    Asks for user's age, their student status 
    and decides the price of the movie ticket. 
    """
    age = int(input("How old are you? "))
    student_status = check_is_user_student()
    print_status_price(age, student_status)



if __name__ == "__main__":
     main()