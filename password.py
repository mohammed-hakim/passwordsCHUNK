import sqlite3
import string as st
import random


special = '#' + '$' + '%' + '&'
n = len(st.ascii_letters) + len(st.digits) + len(special) - 1
chars = st.ascii_letters + st.digits + special
all_chars = list(chars)


def gen_pass():
    word = ''
    for i in range(20):
        word += all_chars[random.randint(0, n)]
    return word


def get_data():
    try:
        db = sqlite3.connect("app.db")
        cr = db.cursor()

        cr.execute("select * from accounts order by id desc ")
        result = cr.fetchall()
        print('\n all the accounts \n')
        for x in range(len(result)):
            print(f"{result[x][0]}  ==>  << {result[x][1]} >>")
    except sqlite3.Error as er:
        print("error", er)
    finally:
        db.close()


def insert(a, b):
    try:
        db = sqlite3.connect("app.db")
        cr = db.cursor()
        cr.execute(
            "CREATE TABLE IF NOT EXISTS accounts(id TEXT, pass TEXT)")
        cr.execute(f"INSERT INTO accounts(id, pass) values('{a}','{b}')")
    except sqlite3.Error as er:
        print("error", er)
    finally:
        print('\n account added successfully ! ')
        db.commit()
        db.close()


def up_data(a, b):
    try:
        db = sqlite3.connect("app.db")
        cr = db.cursor()
        cr.execute(f"UPDATE accounts set pass = '{b}'where id = '{a}'")
    except sqlite3.Error as er:
        print("error", er)
    finally:
        print('\n account updated successfully ! ')
        db.commit()
        db.close()


def delete(a):
    try:
        db = sqlite3.connect("app.db")
        cr = db.cursor()
        cr.execute(f"DELETE from accounts where id = '{a}'")
    except sqlite3.Error as er:
        print("error", er)
    finally:
        print('\n account deleted successfully ! ')
        db.commit()
        db.close()


def clear():
    try:
        db = sqlite3.connect("app.db")
        cr = db.cursor()
        cr.execute(f"DELETE FROM accounts")
    except sqlite3.Error as er:
        print("error", er)
    finally:
        print('\n db cleared successfully ! ')
        db.commit()
        db.close()

pp = '\n hey , what do you want to do with passwords ? \n type [CL] for all the comads : '
print(pp)

while True:
    print('='*50)
    arr1 = ['get' , 'g']
    arr2 = ['up' , 'u']
    arr3 = ['clear' , 'c']
    arr4 = ['delete' , 'd']
    arr5 = ['new' , 'n']
    big = '[new | n] - [get | g] - [delete | d] - [clear | c]'
    f = str(big)
    x = input(f'\n type a comand : ')
    arr = ['new' , 'n']
    if(x in arr5):
        a = input('\n the account : ')
        b = input('\n [rand/custom] password ? ')
        if(b == 'custom' or b == 'C'):
            c = input('\n the password : ')
            b = c
        else:
            b = gen_pass()
        insert(a, b)
    if(x.lower() == 'cl'):
        print(f)    
    elif (x in arr1):
        get_data()
    elif (x in arr2):
        a = input('\n the account : ')
        b = input('\n [rand/custom] password ? ')
        if(b == '\n custom' or 'C'):
            c = input('\n the password : ')
            b = c
        else:
            b = gen_pass()
        up_data(a, b)
    elif (x in arr4):
        a = input('\n the account : ')
        delete(a)
    elif (x in arr3):
        clear()
