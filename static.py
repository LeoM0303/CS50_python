import statistics

dataset = [1,2,3,4,5,6,7,]
    
def main():
    result = get_static()
    print(f'Your result - {result}')

def get_static():
    return statistics.mean(dataset)

main()