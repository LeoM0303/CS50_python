def main():
    student = get_young()
    print(f"{student['name'].capitalize()} from {student['home'].capitalize()} lives in a young house.")

def get_young():
    student = {}
    student["name"] = input("Enter student name: ")
    student["home"] = input("Enter student hometown: ")
    return student

if __name__ == "__main__":
    main()