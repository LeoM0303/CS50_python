#randon list from 1 to 100

from random import shuffle 

dataset = list(range(1, 101))

def main():
    result = mix_list()
    print(f'The result is {result}')
    
def mix_list():
    