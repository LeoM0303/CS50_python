#radome.choice(['heads', 'tails'])

from random import choice

data_base = ['heads', 'tails', 'ears', 'nose', 'eyes', 'mouth']

def main():
    result  = get_rand()
    print(f'The result is {result}')
    
def get_rand():
    return choice(data_base)

main()