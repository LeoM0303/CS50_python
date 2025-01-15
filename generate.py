#radome.choice(['heads', 'tails'])

from random import choice

def main():
    result  = get_rand()
    print(f'The result is {result}')
    
def get_rand():
    return choice(['heads', 'tails'])

main()