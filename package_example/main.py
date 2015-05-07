# Import a package
import example_package

# We will now run the test_function from the example package twice (the same function in different namespaces)
print("Will now run test_function twice (see code comments for why)")
example_package.test_function()
example_package.functions.test_function()

# This verifies that the functions are indeed exactly the same
assert example_package.test_function is example_package.functions.test_function


# Import a file
import another_file

print("Will now run function do_something in another_file.py")
another_file.do_something()
