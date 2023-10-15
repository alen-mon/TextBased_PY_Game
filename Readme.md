# Text-Based PY Adventure Game

## Description

This repository contains a simple text-based adventure game implemented in Python using the Flask web framework. In this game, players navigate through different rooms, solve puzzles, and collect items to progress through the story and find hidden treasures. The game offers an interactive and engaging experience where players can explore various scenarios and make decisions to win.

## Features

- Explore different rooms with unique descriptions.
- Collect and manage items in your inventory.
- Solve puzzles and unlock doors.
- Experience an interactive storyline.
- Enjoy a classic text-based adventure game in a web-based format.

This project serves as a fun example of creating text-based games with web interactions using Flask, making it a great starting point for those interested in game development and web programming.

![Game Screenshot](img.png)


# Testing Module Documentation

## Introduction

This Module provides an overview of the testing module for the Flask-based text-based adventure game project. The testing module includes a set of unit tests to ensure that the application functions correctly.**

## Running Tests

To run the tests for this project, follow these steps:

1. Ensure that you have Python and the required dependencies installed.

2. Navigate to the project directory containing the testing module and the Flask application.

3. Open a terminal or command prompt.

4. Run the following command to execute the tests:

    ```bash
    python run_tests.py
    ```

5. Or Contrarily run the Unit_Test_Cases.py to only run the test case validation**
6. The tests will be executed, and the results will be displayed in the terminal.

## Test Cases

### TestHandleInput

This test class contains test cases for various actions and functionalities within the game.

#### `test_initial_description`

- **Description**: Test the initial description displayed when the game starts.
- **Expected Outcome**: The test checks if the initial description contains the welcome message.
- **Command**: `python run_tests.py`

#### `test_quit_action`

- **Description**: Test the 'quit' action.
- **Expected Outcome**: The test verifies that the 'quit' action ends the game with a specific message.
- **Command**: `python run_tests.py`

#### `test_inventory_action`

- **Description**: Test the 'inventory' action.
- **Expected Outcome**: The test checks if the 'inventory' action displays the player's inventory.
- **Command**: `python run_tests.py`

#### `test_invalid_action`

- **Description**: Test an invalid action.
- **Expected Outcome**: The test ensures that an invalid action is handled and returns the appropriate response.
- **Command**: `python run_tests.py`

#### `test_index`

- **Description**: Test the index route.
- **Expected Outcome**: The test checks if the index route returns a 200 status code.
- **Command**: `python run_tests.py`

## Test Results

After running the tests, the results will be displayed in the terminal. Each test case will be indicated as "Test passed" or "Test failed." If a test fails, the reason for the failure will be provided in the terminal output.

## Interpretation of Results

- "Test passed": Indicates that the test case has passed successfully, and the associated functionality is working as expected.

- "Test failed": Indicates that the test case has failed, and there is an issue with the associated functionality. Review the error message in the terminal output to diagnose the problem.

## Screenshots 

 - **(Run with Test Debug Log screenshot)**

**![](https://lh5.googleusercontent.com/0EINhRNLB5Ni4pIkijku0CIxfe-H4r3mduYbrtjdccIslwbJ4lg2qvw44DUvwKnZZP6DG1NCs5HAOKypj2O1-8MxjonbfcJ_zkR2FSqng4p0bmfiPx0v9BmlMCCzY4apvdoagQwQGEITqsYcY435U1o)**

 - **(Unit_Test standalone Debug Log screenshot)**

**![](https://lh4.googleusercontent.com/9AKFif0CG0_57ya-jWll40bSbG573Ax_C3WqnRGuns12SpO7wKSyLMfRm_McYTceUn6z2NLVGFE-XZ3h6UGGDbxa01QNkLoLt53uWrkIxdF9LW0b7k0o-duqW1hwgsqS6w0C71J0x_js2SGWpAH_AKY)**

## Conclusion

This module is a critical part of ensuring reliable functioning and development of this app. These tests are designed to ensure the reliability and functionality of the Flask-based text-based adventure game project. Regularly running and maintaining these tests help us identify and address issues during runtime and release.


