from dog import Dog
import io
import sys
import types

class TestDog:
    '''Dog in dog.py'''

    def test_is_class(self):
        '''is a class with the name "Dog"'''
        fido = Dog("Fido", 3)
        assert(type(fido) == Dog)

    def test_is_method(self):
        '''is an instance method'''
        fido = Dog("Fido", 3)
        assert(type(fido.bark) == types.MethodType)

    def test_prints_woof(self):
        '''prints "Woof!"'''
        fido = Dog("Fido", 3)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        fido.bark()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Woof!\n")

    def test_is_method(self):
        '''is an instance method'''
        fido = Dog("Fido", 3)
        assert(type(fido.sit) == types.MethodType)

    def test_prints_the_dog_is_sitting(self):
        '''prints "The dog is sitting."'''
        fido = Dog("Fido", 3)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        fido.sit()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "The dog is sitting.\n")
