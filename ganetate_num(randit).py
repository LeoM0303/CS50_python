#generate number from 1 to 100

from random import randint

dataset = list(range(1, 101))
def main():
    result = flip_num()
    print(f'The result is {result}')
    
def flip_num():
    return randint(dataset[0], dataset[-1])

main()