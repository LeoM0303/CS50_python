#randon list from 1 to 100

from random import shuffle 

dataset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def main():
    result = mix_list()
    print(f'The result is {result}')
    
def mix_list():
    for result in dataset:
        shuffle(dataset)
        return dataset

main()
