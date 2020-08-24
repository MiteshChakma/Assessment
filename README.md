# Problem Statement


Create an APP that stores user data
- Data is composed of first name, last name, address (stree, city, state and zip)
- The app should create the following User types (Parent, Child) The child cannot have an address and Must belong to a parent
- App should have API to:
	Delete user data
	Create user data
	Update user data
- Data can be saved in a file or a DB (which ever is easy)
- Readme file describing how to install/run the application
- The project has to provide a mechanism that tests the application to guarantee that it works properly


# Tools used 

![](https://www.sqlite.org/images/sqlite370_banner.gif)

![](https://www.python.org/static/img/python-logo.png) **version 3.7.7**

![](https://assets.ubuntu.com/v1/8114528b-picto-ubuntu-orange.png)

# IDE


Pycharm or any other IDE of your choice

# Installation


If you have **SQLITE3** installed on your device than skip this part.


Open your terminal and have the following codes run 

    sudo apt-get update 

    sudo apt-get install sqlite3

    sqlite3 --version
    
    sudo apt-get install sqlitebrowser
    
    
# Setting up Sqlite3 and creating database and the table 

Open **SQLite Browser** and create a new database named "USER" on your project directory 
Create a new table name **"USER"**

create fields "First_name" as unique, "last_name" as unique, Street, City, State, "ZIP" , "Parentfirst" and "Type"


# Running the app

Now that you have finished installing the sqlite3, its time to run the application 
Open the pycharm or any other IDE of your choice and run the "test.py" on your IDE

You will have following screen on your command line : 

![](https://github.com/MiteshChakma/Assessment/blob/master/s1.png)

Chooose your option and Voila you are done

**check if your entry got included on your database** 

![](https://github.com/MiteshChakma/Assessment/blob/master/s1.1.png)

**Note: same process goes for detele user or update user**
