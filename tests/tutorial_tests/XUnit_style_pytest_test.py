
class TestClass:

    @classmethod
    def setup_class(cls):
        print("\n=========SetupTestClass=======")

    @classmethod
    def teardown_class(cls):
        print("\n=========TeardownTestClass=======")

### MODULE

    def setup_module(self, module):
        print("setup module")

    def teardown_module(self, module):
        print("tardown module")

### FUNCTION

    def setup_function(self, func):
        print("\n Setting up {}".format(func.__name__))

    def teardown_function(self, func):
        print("\n tearing down {}".format(func.__name__))

### METHODS

    def setup_method(self, method):
        print("\nsetup method {}".format(method.__name__))

    def teardown_method(self, method):
        print("\nteardown method {}".format(method.__name__))

### TESTS

    def test_assert_true(self):
        print("\n Executing test_assert_true")
        assert True
