def main():
    number = get_number()
    meow(number)
    
def get_number():
    while True:
        number = int(input("Enter a number: "))
        if number > 0:
            break
    return number

def meow(number):
    for i in range(number):
        print("meow")
        
main()