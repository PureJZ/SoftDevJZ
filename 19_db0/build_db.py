#Jackie Zeng, Wen Zhang, Yinwei Zhang
#SoftDev
#19 skeleton/stub :: SQLITE3 BASICS
#Oct 2024

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

def populate(csv_file, table):
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        headers = reader.fieldnames #First row of csv file
        sq_instruction = "CREATE TABLE " + table + "("
        # CREATE TABLE NewTable(

        for header in headers:
            sq_instruction += header + " TEXT, "
        #CREATE TABLE NewTable(name TEXT, age TEXT, id TEXT,_

        sq_instruction = sq_instruction[:-2] + ")"
        #CREATE TABLE NewTable(name TEXT, age TEXT, id TEXT)

        c.execute(sq_instruction)
        for row in reader:
            sq_instruction = "INSERT INTO " + table + " VALUES ("
            #INSERT INTO NewTable VALUES(
            for header in headers:
                sq_instruction += "'" + row[header] + "', "
                #INSERT INTO NewTable VALUES('name', 'age', 'id',_
            sq_instruction = sq_instruction[:-2] + ")"
            #INSERT INTO NewTable VALUES('name', 'age', 'id')
            c.execute(sq_instruction)
            #Finished insertion here


populate("students.csv", "students")
populate("courses.csv", "courses")

#==========================================================

db.commit() #save changes
db.close()  #close database
