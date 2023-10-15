import unittest
from main import app  # Import your Flask app
from Unit_Test_Cases import TestHandleInput  # Import your test class

if __name__ == '__main__':
    # Create a test suite
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestHandleInput)

    # Run the tests
    test_result = unittest.TextTestRunner(verbosity=2).run(test_suite)

    # Check if the tests were successful
    if test_result.wasSuccessful():
        # If tests passed, start the Flask application
        app.run(debug=True)
