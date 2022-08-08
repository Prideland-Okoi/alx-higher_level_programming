# Almost a circle
Project done during **ALX Software Engineering Scholarship 2022** at **Alx Students Education**. It aims to learn about unit testing, serialization, deserialization, JSON, `args` and `kwargs` in **Python**.

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20200907141910/keyword-300x176.PNG" width="600"/>


## Resources
Read or watch:

* [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
* [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
* [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

## Technologies
* Python Scripts are written with Python 3.9.7
* Tested on Ubuntu 20.04 LTS
* Scripts written in Bash 4.4.23(2)

## Files

Inside `models` folder:

| Filename | Description |
| -------- | ----------- |
| `__init__.py` | Script that converts the directory as a package |
| `base.py` | Base class of geometrical instances |
| `rectangle.py` | Class that inherits attributes references from `Base` class |
| `square.py` | Class that inherits attributes references from `Square` class |

Each class contains public/private attributes, class and static methods. Also, these class raise exceptions when is required.

Inside `tests/test_models` folder:

| Filename | Description |
| -------- | ----------- |
| `__init__.py` | Script that converts the directory as a package |
| `test_base.py` | Module that contains unittests to `Base` class |
| `test_rectangle.py` | Module that contains unittests to `Rectangle` class |
| `test_square.py` | Module that contains unittests to `Square` class |
