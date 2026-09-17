# Doctor and Patient - Python

This is a simple Python program that demonstrates **Inheritance** using a Doctor and Patient example.

The `Person` class is the parent class, while `Doctor` and `Patient` are child classes.

## Classes

### Person

The `Person` class contains:

* Name
* Age

### Doctor

The `Doctor` class inherits from `Person`.

It has an additional:

* Specialization

The `show_role()` function displays the doctor's role and specialization.

### Patient

The `Patient` class also inherits from `Person`.

It has an additional:

* Disease

The `show_role()` function displays the patient's role and disease.

## Example

The program creates a doctor:

```text
Role: Doctor
Specialization: Cardiology
```

And a patient:

```text
Role: Patient
Disease: Fever
```

## Concepts Used

* Python Classes
* Objects
* Inheritance
* Constructors
* `super()`
* Methods

## How to Run

Save the code in a Python file, for example:

```text
main.py
```

Then run:

```bash
python main.py
```

## Author

Muhammad Talha Ijaz
