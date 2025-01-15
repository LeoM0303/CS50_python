#radome.choice(['heads', 'tails'])

import random

def main():
    result  = get_rand()
    print(f'The result is {result}')
    
def get_rand():
    return random.choice(['heads', 'tails'])

main()