# AirBnB_clone

<br><br>
# About
This project is the first stage of creating an AirBNB clone for Holberton's Higher Level Programming course. In this project we build a custom command-line interface for data management using all the skills we've learned in Python.
<br><br>
# Console
The console is the command line interace which allows user to create allowed classes, delete classes, and add attributes to classes. This console works in both interactive and non-interacive mode.


# How to use <br>
## Interactive Mode

First launch the console:

```
/AirBnb_clone$ ./console.py
```

Once launced you will be presented with a new (hbnb) prompt ready to accept commands.

Example:<br>
```
(hbnb) create BaseModel
```

## Non-Interacive Mode<br>

To use in non-interactive mode echo the commands and pipe it to console.py

Example:<br>
```
AirBnb_clone$ echo "create BaseModel" | ./console.py
```

# Commands

## help -- shows help
### Usage:
For a list of documented commands:<br>
> help

For help about a specific command<br>
> help 'command'

Example:<br>
```
(hbnb) help create
```

## create -- create an allowed class
### Usage:
> create 'class name'<br>

Example:<br>
```
(hbnb) create BaseModel
```

## destroy -- delete a specific instance of a class
### Usage:
> destroy 'class name' 'ID'<br>

Example:<br>
```
(hbnb) destroy BaseModel 4b109f3d-0f26-4f12-bd70-59c236afb7ed
```

## show -- print a string representation of an object
### Usage:
> show 'class name' 'ID'<br>

Example:<br>
```
(hbnb) show BaseModel 4b109f3d-0f26-4f12-bd70-59c236afb7ed
```

## all -- print a string representation of all objects or all objects of a specific class
### Usage:
To show all objects:<br>
> all

To show objects of a specific class<br>
> all 'class name'

Example:<br>
```
(hbnb) all BaseModel
```

## update -- update an instance
### Usage:
> update 'class name' 'ID' 'attribute' '"attribute value"'

Example:<br>
```
(hbnb) update user x9247f3d-0g51-4f12-bd70-59c236afb7ls email "johndoe@email.com"
```

## quit -- quit the console
### Usage:
> quit

Example:<br>
```
(hbnb) quit
```

## EOF -- quit the console
### Usage:
Press Ctrl + Z on keyboard<br>
<br>

# Classes
## List of allowed classes
```
Amenity
BaseModel
City
Place
Review
State
User
```
<br>

##  Authors:

> Adam Clear: [Github](https://github.com/adamclear)

> Tim Simms: [GitHub](https://github.com/TimSimms84)
