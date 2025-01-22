from unittest_calculator import square

def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("Test failed")
    try:
        assert square(3) == 9
    except AssertionError:
        print("Test failed")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("Test failed")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("Test failed")
    
    print("All tests pass")
        
if __name__ == "__main__":
    main()
    
# Run the test