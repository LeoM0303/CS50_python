from hello import hello

def test_hello():
    assert hello("Leo") == "Hello Leo"
    assert hello() == "Hello World"