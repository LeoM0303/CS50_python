#generate number from 1 to 100

from random import randint

def main():
    result = flip_num()
    print(f'The result is {result}')
    
def flip_num():
    return randint(1, 100)

main()