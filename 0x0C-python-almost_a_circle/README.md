# 0x0C-python-almost_a_circle

## Learning Python Classes, Inheritance, and Test Drive Development
Welcome to the ALX "0x0C-python-almost_a_circle" repository! This repository is designed to provide a beginner-friendly approach to understanding Classes and Test Driven Development in Python. Whether you're new to programming or looking to enhance your Python skills, this resource aims to guide you through the fundamentals of TDD in a clear and accessible way.

## Table of Contents
- [Introduction](#introduction)
	- [The Python Test Cases and Unittests](#the-python-test-cases-and-unittests)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Testing is the process of evaluating a system or its component(s) with the intent to find whether it satisfies the specified requirements or not. Testing is executing a system in order to identify any gaps, errors, or missing requirements contrary to the actual requirements. This project directory will give you a basic understanding of software testing, its types, methods, levels, and other related terminologies.

The goal is to create 3 classes:
- Base: The class that acts as the base class for the other classes to inherit from. It is in charge of setting up the ID of each instance. From the perspective of the Base class, we observe hierarchial inheritance.
- Rectangle: A class that inherits from the base class, and defines a rectangle instance. It is inherited by the square class.
- Square: This class inherits from Rectangle, exhibiting multilevel inheritance.

And then write unittests using python's unittests library to test our code!

### The Python Test Cases and Unittests
We mainly focus on unittests in this project.

**The Rules are:**

- All test files should be inside a folder `tests`
- All modules should be documented: python3 -c 'print(__import__("my_module").__doc__)'
- All classes should be documented: python3 -c 'print(__import__("my_module").MyClass.__doc__)'
- All functions (inside and outside a class) should be documented: python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'

## Getting Started

To get started with this learning resource, follow these steps:

Clone the Repository:
```bash
git clone https://github.com/mo7amedElfadil/alx-higher_level_programming.git
```
Explore the Content:
Navigate through the provided examples and exercises in the repository.
The file tree is:
0x0c-python-almost_a_circle
├── .gitignore
├── LICENSE
├── models
│   ├── base.py
│   ├── __init__.py
│   ├── rectangle.py
│   └── square.py
├── README.md
└── tests
    ├── __init__.py
    └── test_models
        ├── __init__.py
        ├── test_base.py
        ├── test_rectangle.py
        └── test_square.py

Run the Code:
Execute the Python scripts in your preferred development environment to see the modules in action.
The tests are already written but you can try to add to them as well.

Learn by Doing:
Modify the code, experiment with different scenarios and tests.

## Usage

Each Python script in the models directory contains one class, allowing you to focus on specific concepts. Create a main file and import the desired file as a module:
```python
rectangle = __import__('models/rectangle.py')

#or

import models.rectangle as rectangle
```
or the class itself
```python
Rectangle = __import__('models/rectangle.py').Rectangle

#or

from models.rectangle import Rectangle
```
```
And then test them out. Feel free to modify them to deepen your understanding, experiment, break things, and learn from the experience!

You can then run the scripe
```bash
python3 your_script_name.py
```

to run the tests, from the root directory, run:
```bash
python3 -m unittest discover tests
```

## Contributing

If you find issues, have suggestions for improvements, or want to add more examples, contributions are welcome! Fork the repository, make your changes, and submit a pull request.

## License

This repository is licensed under the MIT License - see the LICENSE file for details.

Happy coding and happy learning!




