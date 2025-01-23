import statistics

def main():
    dataset = int(input('Enter a list of numbers: '))
    dataset = [int(x) for x in dataset.split()]
    result = get_static(dataset)
    print(f'Your result - {result}')

def get_static(dataset):
    return statistics.mean(dataset)

main()