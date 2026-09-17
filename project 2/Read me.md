# Person Student Teacher - Python

This is a simple Python program based on **Inheritance**.

In this program, `Person` is the parent class. `Student` and `Teacher` are child classes that inherit from `Person`.

## Classes

### Person

The `Person` class contains:

* Name
* Age
* `show_info()` function

### Student

The `Student` class inherits from `Person`.

It also has:

* Roll No
* Program

It uses `super()` to call the constructor and `show_info()` function of the parent class.

### Teacher

The `Teacher` class also inherits from `Person`.

It has:

* Teacher ID
* Subject

It also uses `super()` to use the properties and function of the `Person` class.

## Example

The program creates one student:

```text
Name: Ali Raza
Age: 18
Roll No: 1001
Program: ICS
```

And one teacher:

```text
Name: Ahmed Khan
Age: 35
Teacher ID: 501
Subject: Computer Science
```

## Concepts Used

* Python Classes
* Objects
* Inheritance
* Method Overriding
* `super()`
* Constructors

## How to Run

Save the program as:

```text
main.py
```

Then run:

```bash
python main.py
```

## Author

Muhammad Talha Ijaz
