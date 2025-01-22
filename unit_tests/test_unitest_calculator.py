from unittest_calculator import square

def main():
    test_square()

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16
    assert square(5) == 25
    
    print("All tests pass")
        
if __name__ == "__main__":
    main()
    
# Run the test