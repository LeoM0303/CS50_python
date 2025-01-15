#radome.choice(['heads', 'tails'])

import random

def main():
    get_rand()
    
def get_rand():
    coin = random.choice(['heads', 'tails'])
    print(coin)

main()