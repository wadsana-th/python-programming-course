"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""

# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("", 0, "", "")  # name, age, city, country
    hobbies = []
    
  choies = input("Whay do you want to do?(1: display,2: add hobby,3: remove hoby,4:)")
  
    # Your code here
    if choice == "1":
        # display all info
        print("Name:",person[0])
        print("Age:",person[1])
        print("City:",person[2])
        print("Country:",person[3])
        print("hobbies:",hobbies)

    elif choice == "2":
    # append hobby
    hobby = input("What is your new hobbies:")
    hobbyies.append['hobby']

    elif choice == "3":
    # remove hobby
    hobbyies.pop()

elif choicce == "4":
    #edit age
    person_list = list(person)
    aeg = input("How old are you?:") #("Wadsana",'19' "Choburi", "th")
    person_list[1] = age
    person = input("")

if __name__ == "__main__":
    personal_info_manager()

