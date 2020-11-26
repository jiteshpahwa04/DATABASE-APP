import tkinter
from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root=Tk()
root.title("Codemy.com Database app")
root.iconbitmap("icon.ico")

root.geometry("400x400")

#create a database or connect
conn=sqlite3.connect("address_book.db")

#create cursor
c=conn.cursor()

##create table
##c.execute("""CREATE TABLE address(
##            first_name text,
##            last_name text,
##            address text,
##            city text,
##            state text,
##            zipcode integer)""")

#create edit function to edit a record

def update():
    #create a database or connect
    conn=sqlite3.connect("address_book.db")
    #create cursor
    c=conn.cursor()

    record_id=delete_box.get()
    c.execute("""UPDATE address SET
        first_name=:last,
        last_name=:last,
        address=:address,
        city=:city,
        state=:state,
        zipcode=:zipcode

        WHERE oid=:oid""",
              {'first':f_name_editor.get(),
               'last':l_name_editor.get(),
               'address':address_editor.get(),
               'state':state_editor.get(),
               'city':city_editor.get(),
               'zipcode':zipcode_editor.get(),

               'oid':record_id
                })

    
    #commit changes
    conn.commit()
    #close connection
    conn.close()

    editor.destroy()

def edit():
    global editor
    editor=Tk()
    editor.title("Update a record")
    editor.iconbitmap("icon.ico")
    editor.geometry("400x300")
    #create a database or connect
    conn=sqlite3.connect("address_book.db")
    #create cursor
    c=conn.cursor()

    record_id=delete_box.get()
    #query the database
    c.execute("SELECT * FROM address WHERE oid="+record_id)
    records=c.fetchall()
    
        
##    loop the results
##    print_records=''
##    for record in records:
##        print_records+=str(record[0])+" "+str(record[1]) +"\t"+str(record[6])+ "\n"

    # create global variable for text box name
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor
 
    #create text boxes
    f_name_editor=Entry(editor, width=30)
    f_name_editor.grid(row=0,column=1, padx=20,pady=(10,0))

    l_name_editor=Entry(editor, width=30)
    l_name_editor.grid(row=1,column=1)

    address_editor=Entry(editor, width=30)
    address_editor.grid(row=2,column=1)

    city_editor=Entry(editor, width=30)
    city_editor.grid(row=3,column=1)

    state_editor=Entry(editor, width=30)
    state_editor.grid(row=4,column=1)

    zipcode_editor=Entry(editor, width=30)
    zipcode_editor.grid(row=5,column=1)

    #create text box labels
    f_name_label=Label(editor,text="First name")
    f_name_label.grid(row=0,column=0,pady=(10,0))

    l_name_label=Label(editor,text="Last name")
    l_name_label.grid(row=1,column=0)

    address_label=Label(editor,text="Address")
    address_label.grid(row=2,column=0)

    city_label=Label(editor,text="City")
    city_label.grid(row=3,column=0)

    state_label=Label(editor,text="State")
    state_label.grid(row=4,column=0)

    zipcode_label=Label(editor,text="Zipcode")
    zipcode_label.grid(row=5,column=0)

    #loop through results
    for record in records:
        f_name_editor.insert(0,record[0])
        l_name_editor.insert(0,record[1])
        address_editor.insert(0,record[2])
        city_editor.insert(0,record[3])
        state_editor.insert(0,record[4])
        zipcode_editor.insert(0,record[5])

    #create a save button to save the eddited record
    edit_btn=Button(editor, text="Save records",command=update)
    edit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=145)
 



#crteate function to delete a record
def delete():
    #create a database or connect
    conn=sqlite3.connect("address_book.db")
    #create cursor
    c=conn.cursor()

    #delete a record
    c.execute("DELETE FROM address WHERE oid="+delete_box.get())


    #commit changes
    conn.commit()
    #close connection
    conn.close()


#create submit function for database
def submit():
    #create a database or connect
    conn=sqlite3.connect("address_book.db")
    #create cursor
    c=conn.cursor()

    #INsert into table
    c.execute("INSERT INTO address VALUES(:f_name,:l_name,:address,:city,:state,:zipcode)",
            {
                'f_name':f_name.get(),
                'l_name':l_name.get(),
                'address':address.get(),
                'city':city.get(),
                'state':state.get(),
                'zipcode':zipcode.get()})
    
    
    #commit changes
    conn.commit()
    #close connection
    conn.close()

    #clear the text boxes
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)

def query():
    #create a database or connect
    conn=sqlite3.connect("address_book.db")
    #create cursor
    c=conn.cursor()

    #query the database
    c.execute("SELECT *,oid FROM address")
    records=c.fetchall()
##    print(records)

    #loop the results
    print_records=''
    for record in records:
        print_records+=str(record[0])+" "+str(record[1]) +"\t"+str(record[6])+ "\n"

    query_label=Label(root, text=print_records)
    query_label.grid(row=12,column=0,columnspan=2)

    #commit changes
    conn.commit()
    #close connection
    conn.close()

#create text boxes
f_name=Entry(root, width=30)
f_name.grid(row=0,column=1, padx=20,pady=(10,0))

l_name=Entry(root, width=30)
l_name.grid(row=1,column=1)

address=Entry(root, width=30)
address.grid(row=2,column=1)

city=Entry(root, width=30)
city.grid(row=3,column=1)

state=Entry(root, width=30)
state.grid(row=4,column=1)

zipcode=Entry(root, width=30)
zipcode.grid(row=5,column=1)

delete_box=Entry(root, width=30)
delete_box.grid(row=8,column=1,pady=5)

#create text box labels
f_name_label=Label(root,text="First name")
f_name_label.grid(row=0,column=0,pady=(10,0))

l_name_label=Label(root,text="Last name")
l_name_label.grid(row=1,column=0)

address_label=Label(root,text="Address")
address_label.grid(row=2,column=0)

city_label=Label(root,text="City")
city_label.grid(row=3,column=0)

state_label=Label(root,text="State")
state_label.grid(row=4,column=0)

zipcode_label=Label(root,text="Zipcode")
zipcode_label.grid(row=5,column=0)

delete_box_label=Label(root,text="Select ID")
delete_box_label.grid(row=8,column=0,pady=5)

#crteate submit button
submit_btn=Button(root, text="Add record to database",command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,padx=10,pady=10,ipadx=100)

#create a query button
query_btn=Button(root, text="Show records",command=query)
query_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=137)

#create a delete button
delete_btn=Button(root, text="Delete records",command=delete)
delete_btn.grid(row=9,column=0,columnspan=2,pady=10,padx=10,ipadx=137)

#create a udate button
edit_btn=Button(root, text="Edit records",command=edit)
edit_btn.grid(row=10,column=0,columnspan=2,pady=10,padx=10,ipadx=143)


#commit changes
conn.commit()

#close connection
conn.close()


root.mainloop()
