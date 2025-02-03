def main():
    student = get_young()
    print(f"{student[0].capitalize()} from {student[1].capitalize()} lives in a young house.")

def get_young():
    student = {}
    student["name"] = input("Enter student name: ")
    student["home"] = input("Enter student hometown: ")
    return student["name"], student["home"]

if __name__ == "__main__":
    main()