import random

def usernamegenerator(fullname):
    nameparts = fullname.split()
    if len(nameparts) <2:
        return "Please enter a fullname(first and last name)"

    firstname = nameparts[0].lower()
    lastname = nameparts[-1].lower()

    username1 = firstname + lastname
    username2 = lastname + firstname

    randum = random.randint(1000,9999)

    username3 = firstname + str(randum)
    username4 = lastname + firstname +str(randum)

    usernames = [username1,username2,username3,username4]

    return random.choice(usernames)


        
        
    


while True:
    fullname = input("Enter your fullname(or type exit to quit)")

    if fullname.lower() == "exit":
        break

    username = usernamegenerator(fullname)
    print(username)
    print("-"*40)