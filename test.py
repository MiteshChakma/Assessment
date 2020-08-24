import sqlite3
def remove_user(fname):
    try:
        conn = sqlite3.connect('user')
    except Exception as e:
        print("db not connected")

    cursor = conn.cursor()
    cursor.execute("DELETE FROM USER WHERE First_name = ?", (fname,) )
    conn.commit()
    cursor.close()


def update_user(fname, uname):
    try:
        conn = sqlite3.connect('user')
    except Exception as e:
        print("db not connected")

    cursor = conn.cursor()
    cursor.execute("UPDATE USER SET First_name= ? WHERE First_name = ?",(uname, fname))
    conn.commit()
    cursor.close()



def add_user(fname, lname, typ, *num):
    first_name = fname
    last_name = lname
    type = typ
    try:
        conn = sqlite3.connect('user')
    except Exception as e:
        print("db not connected")

    cursor = conn.cursor()
    if (type == "Child"):
        parentfirst, *m = num
        cursor.execute(
            "INSERT INTO USER ('First_name', 'Last_name', 'Street','City', 'State', 'ZIP','Parentfirst','Type')values (?,?,?,?,?,?,?,?)",
            (
                first_name,
                last_name,
                None,
                None,
                None,
                None,
                parentfirst,
                type
            ))
        # cursor.commit()
        conn.commit()
        cursor.close()
    else:
        street, city, state, zip = num
    # select = cursor.execute("select * from USER")
    # print(select)

        cursor.execute(
            "INSERT INTO USER ('First_name', 'Last_name', 'Street','City', 'State', 'ZIP','Parentfirst','Type')values (?,?,?,?,?,?,?,?)",
            (
                first_name,
                last_name,
                street,
                city,
                state,
                zip,
                None,
                type
            ))
        # cursor.commit()
        conn.commit()
        cursor.close()
        #check if there is any user named similer with pfn.


#add_user("mr", "sn", "Parent","10", "dhaka", "dhaka", "1230")
#add_user("mr", "cln", "Child", "fn")
#remove_user("fn")
#update_user("mr", "change")
if __name__ == "__main__":
    print("Add Parent : 1")
    print("Add Child : 2")
    print("remove user by first name : 3")
    print("update users firstname : 4")
    i = int(input("query:",))
    if (i == 1):
        Type = "Parent"
        print("input parents info:")
        firstname = str(input("firstname: ", ))
        lastname = str( input("lastname: ", ))
        street = str( input("street: ", ))
        city = str( input("City: ", ))
        state = str( input("State: ", ))
        zip = str(input("zip: ", ))

        add_user(firstname, lastname, Type, street, city, state, zip)
        print("added successfully")
    elif (i == 2):
        Type = "Child"
        print("input childs info:")
        firstname = str(input("firstname: ", ))
        lastname = str(input("lastname: ", ))
        parentfirstname = str(input("parents first name: ", ))
        add_user(firstname, lastname,Type, parentfirstname)
        print("added successfully")
    elif(i == 3):
        print("Firstname of the users firstname to be removed.")
        firstname = str(input("firstname of the user: ", ))
        remove_user(firstname)
        print("user removed")
    elif(i==4 ):
        current_firstname = str(input('input the first name of the user to be updated',))
        update_name = str(input('input the updates  first name: ', ))
        update_user(current_firstname,update_name)
        print("user updated")
    else:
        print("Invalid input")

