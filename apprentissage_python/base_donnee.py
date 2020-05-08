#coding:utf-8
import sqlite3
# Connection à la base de données 
connection = sqlite3.connect('base.db')

cursor = connection.cursor()
username = ('Harrys',)
cursor.execute('SELECT * FROM users where user_name = ?',username)
print(cursor.fetchone)


# Fermeture de la base de donnée 
connection.close()