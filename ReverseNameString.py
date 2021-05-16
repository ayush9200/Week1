full_name = ""
def main():
    takeUserName()
    printReversedName()

def takeUserName():
    global full_name
    first_name = input("Enter your first name : ")
    last_name = input("Enter your last name : ")
    full_name = first_name + " " + last_name

def printReversedName():
    reversed_name = ""
    # Executing loop in reversed
    for count in range(len(full_name),0,-1):
        reversed_name = reversed_name + full_name[count-1]
    print(reversed_name)

main()