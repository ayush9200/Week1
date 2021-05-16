radius = 0.0
def main():
    take_user_input()
    print_circle_area()

def take_user_input():
    global radius
    radius = float(input("Please enter radius of circle : "))

def calculate_area():
    # Calculating area of circle by multiplying radius with 3.14(pie value)
    area = 2 * (3.14 * radius)
    return area

def print_circle_area():
    print(f'Circle area is : {calculate_area()}')

main()