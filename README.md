```# AirBnB clone - The console

https://raw.githubusercontent.com/DaisyGeraldine/holbertonschool-AirBnB_clone/master/AirBnB%20clone%20).png

#  First step: Write a command interpreter to manage your AirBnB objects.

This is the first step towards creating the first complete web app - the AirBnB clone.

Each task is linked:

A main class (called BaseModel) is established to handle initialization, serialization and deserialization of future instances, a simple serialization / deserialization flow will be created: Instance <-> Dictionary <-> JSON string <-> file, will be created all classes used for AirBnB (User, State, City, Place ...) that inherit from BaseModel, the first abstracted storage engine of the project will be created: file storage.

All unit tests will be created to validate all our classes and storage engine.

#  Let's go! 🤖

[![The console](http://img.youtube.com/vi/p00ES-5K4C8/0.jpg)](http://www.youtube.com/watch?v=p00ES-5K4C8 "AirBnB The Console")

#  Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

How to create a Python package

How to create a command interpreter in Python using the cmd module

What is Unit testing and how to implement it in a large project

How to serialize and deserialize a Class

How to write and read a JSON file

How to manage datetime

What is an UUID

What is *args and how to use it

What is **kwargs and how to use it

How to handle named arguments in a function

#  Execution

Your shell should work like this in interactive mode:

``` python

$ ./console.py

(hbnb) help

Documented commands (type help <topic>):

========================================

EOF help quit

(hbnb)

(hbnb)

(hbnb) quit

$

```

#  Execute program called _console.py_

Cotains:

- prompt: (hbnb)

- quit: exit the program

- help: keep it updated

- create: creates a new instance of BaseModel

- show: prints the string representation of an instance based on the class name and id

- destroy: deletes an instance based on the class name and id

- all: prints all string representation of all instances based or not on the class name

- update: updates an instance based on the class name and id by adding or updating attribute

``` python

root at DESKTOP-JID01TK in ~/projects/holbertonschool-AirBnB_clone on master*
$ ./console.py
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel Holberton
** no instance found **
(hbnb) create BaseModel
17cb3169-76aa-4555-84b0-cad452aa0657
(hbnb) all BaseModel
["[BaseModel] (17cb3169-76aa-4555-84b0-cad452aa0657) {'id': '17cb3169-76aa-4555-84b0-cad452aa0657', 'created_at': datetime.datetime(2022, 10, 16, 20, 18, 52, 751490), 'updated_at': datetime.datetime(2022, 10, 16, 20, 18, 52, 751631)}"]
(hbnb) show BaseModel 17cb3169-76aa-4555-84b0-cad452aa0657
[BaseModel] (17cb3169-76aa-4555-84b0-cad452aa0657) {'id': '17cb3169-76aa-4555-84b0-cad452aa0657', 'created_at': datetime.datetime(2022, 10, 16, 20, 18, 52, 751490), 'updated_at': datetime.datetime(2022, 10, 16, 20, 18, 52, 751631)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 17cb3169-76aa-4555-84b0-cad452aa0657 first_name "Betty"
(hbnb) show BaseModel 17cb3169-76aa-4555-84b0-cad452aa0657
[BaseModel] (17cb3169-76aa-4555-84b0-cad452aa0657) {'id': '17cb3169-76aa-4555-84b0-cad452aa0657', 'created_at': datetime.datetime(2022, 10, 16, 20, 18, 52, 751490), 'updated_at': datetime.datetime(2022, 10, 16, 20, 19, 40, 633113), 'first_name': '"Betty"'}
(hbnb) create BaseModel
9e44f2fb-941f-4a21-a493-c8bfeef04d8f
(hbnb) all BaseModel
['[BaseModel] (17cb3169-76aa-4555-84b0-cad452aa0657) {\'id\': \'17cb3169-76aa-4555-84b0-cad452aa0657\', \'created_at\': datetime.datetime(2022, 10, 16, 20, 18, 52, 751490), \'updated_at\': datetime.datetime(2022, 10, 16, 20, 19, 40, 633113), \'first_name\': \'"Betty"\'}']
['[BaseModel] (17cb3169-76aa-4555-84b0-cad452aa0657) {\'id\': \'17cb3169-76aa-4555-84b0-cad452aa0657\', \'created_at\': datetime.datetime(2022, 10, 16, 20, 18, 52, 751490), \'updated_at\': datetime.datetime(2022, 10, 16, 20, 19, 40, 633113), \'first_name\': \'"Betty"\'}', "[BaseModel] (9e44f2fb-941f-4a21-a493-c8bfeef04d8f) {'id': '9e44f2fb-941f-4a21-a493-c8bfeef04d8f', 'created_at': datetime.datetime(2022, 10, 16, 20, 19, 54, 596489), 'updated_at': datetime.datetime(2022, 10, 16, 20, 19, 54, 596699)}"]
(hbnb) destroy BaseModel 17cb3169-76aa-4555-84b0-cad452aa0657
(hbnb) show BaseModel 17cb3169-76aa-4555-84b0-cad452aa0657
** no instance found **
(hbnb)
```
![enter image description here](https://raw.githubusercontent.com/DaisyGeraldine/holbertonschool-AirBnB_clone/master/jsoncrack.com_1.png)


# Deployment 📦

### Final Product

![enter image description here](https://raw.githubusercontent.com/DaisyGeraldine/holbertonschool-AirBnB_clone/master/readme.png)

# Authors :books:

* **Daisy Chipana** - *AirBnB Clone - The Console* - [Daisy Chipana](https://github.com/[DaisyGeraldine](https://github.com/DaisyGeraldine))✒️

* **Juan Ticse** - *AirBnB Clone - The Console* - [Juan Ticse](https://github.com/JPTicse)✒️

* **Julian Zea** - *AirBnB Clone - The Console* - [Julian Zea](https://github.com/JulianZea)✒️
---
