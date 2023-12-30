<p align="center">
  <a href="" rel="noopener">
 <img width=400px height=200px src="https://www.alxafrica.com/wp-content/uploads/2023/01/7_Do-hard-things-100.jpg" alt="Do hard things"></a>
</p>

<h1 align="center">alx-high_level_programming</h1>


<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub issues](https://img.shields.io/github/issues/mo7amedelfadil/alx-higher_level_programming)
](https://github.com/mo7amedElfadil/alx-higher_level_programming/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/mo7amedelfadil/alx-higher_level_programming)](https://github.com/mo7amedElfadil/alx-higher_level_programming/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> 
    In computer science, a high-level programming language is a programming language with strong abstraction from the details of the computer. In contrast to low-level programming languages, it may use natural language elements, be easier to use, or may automate (or even hide entirely) significant areas of computing systems (e.g. memory management), making the process of developing a program simpler and more understandable than when using a lower-level language. The amount of abstraction provided defines how "high-level" a programming language is.
    <br> 
</p>

## 📝 Table of Contents

- [About](#🧐-about)
- [Getting Started](#🏁-getting-started)
- [Usage](#usage)
- [Authors](#✍️-authors)
- [Acknowledgments](#🎉-acknowledgements)
- [License](#📝-license)

## 🧐 About 
In my journey to be a full-stack web developer, I explore the high-level programming languages with the ALX Africa community. Our first HLPL is Python.

Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.

Lets learn Python!



## 🏁 Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them.

- Python (this project uses Python 3.8)
- Pip
- IDE (e.g. vim, emacs, VSCode, PyCharm, etc.)

### Installing 
![python](img/python_65.png)

A step by step series of examples that tell you how to get a development env running.

Say what the step will be

A Quick Guide for Installing Python on Common Operating Systems

- [Windows](#windows)
- [MacOS](#macos)
- [Linux](#linux)

#### Windows 
![windows](img/windows_65.png)

1. If you have not yet installed Python on your Windows OS, then download and install the latest Python3 installer from [Python Downloads Page](https://www.python.org/downloads/)

    - Make sure to check the box during installation which adds Python to PATH. Labeled something like Add Python 3.X to PATH

2. Once Python is installed, you should be able to open a command window, type python, hit ENTER, and see a Python prompt opened. Type quit() to exit it. You should also be able to run the command pip and see its options. If both of these work, then you are ready to go.

- If you cannot run python or pip from a command prompt, you may need to add the Python installation directory path to the Windows PATH variable
    - The easiest way to do this is to find the new shortcut for Python in your start menu, right-click on the shortcut, and find the folder path for the python.exe file
      - For Python2, this will likely be something like `C:\Python27`
      - For Python3, this will likely be something like `C:\Users\<USERNAME>\AppData\Local\Programs\Python\Python37`
    - Open your Advanced System Settings window, navigate to the "Advanced" tab, and click the "Environment Variables" button
    - Create a new system variable:
      - Variable name: PYTHON_HOME
      - Variable value: <your_python_installation_directory>
    - Now modify the PATH system variable by appending the text ;%PYTHON_HOME%\;%PYTHON_HOME%;%PYTHON_HOME%\Scripts\ to the end of it.
    - Close out your windows, open a command window and make sure you can run the commands python and pip

#### MacOS 
![apple](img/apple_65.png)

MacOS comes with a native version of Python. As of this writing, it comes with a version of Python2, which has been deprecated. In order to use most modern Python applications, you need to install Python3. Python2 and Python3 can coexist on the same machine without problems, and for MacOS it is in fact necessary for this to happen, since MacOS continues to rely on Python2 for some functionality.

There are a couple of ways we can install Python3 on your MacOS operating system:

##### Option 1: Install the official Python release
1. Browse to the [Python Downloads Page](https://www.python.org/downloads/)
2. Click on the "Download Python 3.x.x" button on the page
3. Walk through the steps of the installer wizard to install Python3
4. Once installed, the wizard will open a Finder window with some .command files in it
    - Double-click the Install Certificates.command file and the Update Shell Profile.command file to run each of them
    - Close the windows once they are finished
5. Open your Terminal application and run the command python3 to enter the Python interactive command line. Issue the command quit() to exit. Also make sure PIP (the Python package manager) is installed by issuing the command pip3 -V. It should display the current version of PIP as well as Python (which should be some release of Python3).
6. You're all done. Python is installed and ready to use.

##### Option 2: Install with Homebrew
[Homebrew](https://brew.sh/) is a MacOS Linux-like package manager. Walk through the below steps to install Homebrew and an updated Python interpreter along with it.

1. Open your Terminal application and run: `xcode-select --install`. This will open a window. Click 'Get Xcode' and install it from the app store.
2. Install Homebrew. Run: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
    - You can also find this command on the [Homebrew website](https://brew.sh/)
3. Install latest Python3 with brew install python
4. Once Python is installed, you should be able to open your Terminal application, type python3, hit ENTER, and see a Python 3.X.X prompt opened. Type quit() to exit it. You should also be able to run the command pip3 and see its options. If both of these work, then you are ready to go.

- Here are some additional resources on [Installing Python 3 on Mac OS X](https://docs.python-guide.org/starting/install3/osx/)

#### Linux 
![linux](img/linux_65.png)

- Raspberry Pi OS may need Python and PIP
  - Install them: `sudo apt install -y python3-pip`
- Debian (Ubuntu) distributions may need Python and PIP
  - Update the list of available APT repos with `sudo apt update`
  - Install Python and PIP: `sudo apt install -y python3-pip`
- RHEL (CentOS) distributions usually need PIP
  - Install the EPEL package: `sudo yum install -y epel-release`
  - Install PIP: `sudo yum install -y python3-pip`

## Usage

Each directory in this repository tackles a different topic/concept and there is a linear progression of topics. For each catered usage, please refer to the README.md file in the respective directory.

- Clone the repository: `git clone https://github.com/mo7amedelfadil/alx-higher_level_programming`
- Navigate to the directory: `cd alx-higher_level_programming`
- Navigate to the directory you want to explore: `cd <directory>`
- Run the program: `./<program>` or `python3 <program>`
  - Note most of the programs are modules you can import into your own programs so they won't run on their own. You may have to write your own "main" function to run them. In your main file, you can do the following:
    - `from <module> import <function>`
    - `<function>()`
     or
    - `import <module>` 
    - `<module>.<function>()`
- Run the tests: `python3 -m doctest -v <program>`
**Note:** all modules are documented so you can refer to their documentation by running `python3 -c "help(<module>)"` to figure out what they do.

## ✍️ Authors

- [@mo7amedelfadil](https://github.com/mo7amedelfadil)

## 🎉 Acknowledgements

- [ALX Africa](https://www.alxafrica.com)

## 📝 License

Copyright © 2023 [MIT](LICENSE).
