import unittest
from main import app, handle_input, get_initial_description

# ANSI escape code for green text
GREEN = '\033[92m'
RESET = '\033[0m'

class TestHandleInput(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def print_test_passed(self, message):
        print(f"{GREEN}Test passed: {message}{RESET}")

    def test_initial_description(self):
        print("Testing the initial description...")
        initial_description = get_initial_description()
        self.assertIn("Welcome to the Text-Based Adventure Game!", initial_description)
        self.print_test_passed("Testing the initial description...")

    def test_quit_action(self):
        print("Testing the 'quit' action...")
        response = handle_input('quit')
        self.assertEqual(response, "Game over. You quit the game. You Failed to find the Treasure")
        self.print_test_passed("Testing the 'quit' action")

    def test_inventory_action(self):
        print("Testing the 'inventory' action...")
        response = handle_input('inventory')
        self.assertEqual(response, "You are carrying: ")
        self.print_test_passed("Testing the 'inventory' action")

    def test_invalid_action(self):
        print("Testing an invalid action...")
        response = handle_input('invalid')
        self.assertEqual(response, "No Rooms here. Try again.")
        self.print_test_passed("Testing an invalid action")

    def test_index(self):
        print("Testing the index route...")
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.print_test_passed("Testing the index route...")



if __name__ == '__main__':
    unittest.main()
