from hi import hello

def test_hello():
    assert hello("leo") == "Hello Leo"

    assert hello() == "Hello World"