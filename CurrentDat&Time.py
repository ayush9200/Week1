from datetime import datetime
def main():
    printCurrentDateTime()

def printCurrentDateTime():
    date = datetime.now().date()
    time = datetime.now().time()
    time = time.strftime("%H:%M:%S")
    print(f'Today date is {date} and time is {time}')

main()