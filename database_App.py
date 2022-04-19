from tkinter import *
import sqlite3

root=Tk()
root.title("DATABASE APPLICATION")
root.iconbitmap("icony/camera.ico")
root.geometry("400x600")
'''
#create a database file
conn=sqlite3.connect("address_book.db") #create a database
cur=conn.cursor()  #Create a cursor
cur.execute("""CREATE TABLE addresses(
    Firstname text,
    Lastname text,
    Sex text,
    Age integer,
    Addresses text,
    City text,
    State_ text,
    Postal code integer

)""")
conn.commit()  #commit changes
conn.close()  #close connection
'''


#Create a new window for showing records
def show():
    top=Toplevel()
    top.title("DISPLAYING DATABASE RECORDS")
    top.geometry("400x400")
    #create a database file
    conn=sqlite3.connect("address_book.db") #create a database
    cur=conn.cursor()  #Create a cursor
    cur.execute("SELECT *,oid FROM addresses")
    records=cur.fetchall()

    #loop through records
    print_record=" "
    for record in records:
        print_record+=str(record[0]) +"\t"+ "\t" + str(record[1]) +"\t"+"\t" + str(record[8])+"\n"
    
    Label(top, text=print_record).pack()
    conn.commit()  #commit changes
    conn.close()  #close connection


#create submittion command function

def submit():
    conn=sqlite3.connect("address_book.db") #connect to an already created database
    cur=conn.cursor()  #Create a cursor
    cur.execute("INSERT INTO addresses VALUES (:f_name,:l_name,:sex,:age,:address_,:city,:state_,:postal_code)",
        {
            'f_name':f_name.get(),
            'l_name':l_name.get(),
            'sex':sex.get(),
            'age':age.get(),
            'address_':address_.get(),
            'city':city.get(),
            'state_':state_.get(),
            'postal_code':postal_code.get()
            }
    )
    conn.commit()  #commit changes
    conn.close()  #close connection

    #Clear boxes after submittion
    f_name.delete(0,END)
    l_name.delete(0,END)
    sex.delete(0,END)
    age.delete(0,END)
    address_.delete(0,END)
    city.delete(0,END)
    state_.delete(0,END)
    postal_code.delete(0,END)

def eraser():
    conn=sqlite3.connect("address_book.db")
    cur=conn.cursor()
    cur.execute("DELETE from addresses WHERE oid="+select_id.get())
    select_id.delete(0,END)
    conn.commit()
    conn.close()

def editor():
    global top2
    top2=Tk()
    top2.title("UPDATING DATABASE RECORDS")
    top2.geometry("400x400")
    #connect to the address_book database file
    conn=sqlite3.connect("address_book.db") #connect to the database
    cur=conn.cursor()  #Create a cursor
    cur.execute("SELECT * FROM addresses WHERE oid=" + select_id.get())
    records=cur.fetchall()
    
    conn.commit()
    conn.close()
    global f_name2
    global l_name2
    global sex2
    global age2
    global address_2
    global city2
    global state_2
    global postal_code2
    

    #Create text box Entries
    f_name2=Entry(top2, width=50)
    f_name2.grid(row=0,column=1,padx=10, pady=10)
    l_name2=Entry(top2, width=50)
    l_name2.grid(row=1,column=1,padx=10, pady=10)
    sex2=Entry(top2, width=50)
    sex2.grid(row=2,column=1,padx=10, pady=10)
    age2=Entry(top2, width=50)
    age2.grid(row=3,column=1,padx=10,pady=10)
    address_2=Entry(top2, width=50)
    address_2.grid(row=4,column=1,padx=10,pady=10)
    city2=Entry(top2, width=50)
    city2.grid(row=5,column=1,padx=10,pady=10)
    state_2=Entry(top2, width=50)
    state_2.grid(row=6,column=1,padx=10,pady=10)
    postal_code2=Entry(top2, width=50)
    postal_code2.grid(row=7,column=1,padx=10,pady=10)

    #Create text box labels
    f_name_lbl2=Label(top2, text="Firstname")
    f_name_lbl2.grid(row=0, column=0)
    l_name_lbl2=Label(top2, text="Lastname")
    l_name_lbl2.grid(row=1, column=0)
    sex_lbl2=Label(top2, text="sex")
    sex_lbl2.grid(row=2, column=0)
    age_lbl2=Label(top2, text="Age")
    age_lbl2.grid(row=3, column=0)
    address_lbl2=Label(top2, text="Address")
    address_lbl2.grid(row=4, column=0)
    city_lbl2=Label(top2, text="City")
    city_lbl2.grid(row=5, column=0)
    state_lbl2=Label(top2, text="State")
    state_lbl2.grid(row=6, column=0)
    postal_code_lbl2=Label(top2, text="Postal code")
    postal_code_lbl2.grid(row=7, column=0)

    #loop through results

    for record in records:
        f_name2.insert(0, record[0])
        l_name2.insert(0, record[1])
        sex2.insert(0, record[2])
        age2.insert(0, record[3])
        address_2.insert(0, record[4])
        city2.insert(0, record[5])
        state_2.insert(0, record[6])
        postal_code2.insert(0, record[7])
        
    #create Save button
    save_btn=Button(top2, text="SAVE DATA", command=store)
    save_btn.grid(row=8, column=0, columnspan=2, pady=10, ipadx=157)


def store():
    conn=sqlite3.connect('address_book.db')
    cur=conn.cursor()
    
    record_id = select_id.get()

    cur.execute("""UPDATE addresses SET
        Firstname = :f_namee,
        Lastname = :l_namee,
        Sex = :sexee,
        Age = :agee,
        Addresses = :addressee,
        City = :citie,
        State_ = :statee,
        Postal code = :postal

        WHERE oid = :oid""",
        {
            'f_namee': f_name2.get(),
            'l_namee': l_name2.get(),
            'sexee': sex2.get(),
            'agee': age2.get(),
            'addressee': address_2.get(),
            'citie': city2.get(),
            'statee': state_2.get(),
            'postal': postal_code2.get(),
            'oid': record_id
        })
    conn.commit()
    conn.close()
    top2.destroy()

#Create text box Entries
f_name=Entry(root, width=50)
f_name.grid(row=0,column=1,padx=10, pady=10)
l_name=Entry(root, width=50)
l_name.grid(row=1,column=1,padx=10, pady=10)
sex=Entry(root, width=50)
sex.grid(row=2,column=1,padx=10, pady=10)
age=Entry(root, width=50)
age.grid(row=3,column=1,padx=10,pady=10)
address_=Entry(root, width=50)
address_.grid(row=4,column=1,padx=10,pady=10)
city=Entry(root, width=50)
city.grid(row=5,column=1,padx=10,pady=10)
state_=Entry(root, width=50)
state_.grid(row=6,column=1,padx=10,pady=10)
postal_code=Entry(root, width=50)
postal_code.grid(row=7,column=1,padx=10,pady=10)

#Create text box labels
f_name_lbl=Label(root, text="Firstname")
f_name_lbl.grid(row=0, column=0)
l_name_lbl=Label(root, text="Lastname")
l_name_lbl.grid(row=1, column=0)
sex_lbl=Label(root, text="sex")
sex_lbl.grid(row=2, column=0)
age_lbl=Label(root, text="Age")
age_lbl.grid(row=3, column=0)
address_lbl=Label(root, text="Address")
address_lbl.grid(row=4, column=0)
city_lbl=Label(root, text="City")
city_lbl.grid(row=5, column=0)
state_lbl=Label(root, text="State")
state_lbl.grid(row=6, column=0)
postal_code_lbl=Label(root, text="Postal code")
postal_code_lbl.grid(row=7, column=0)

#create submit button
submit_btn=Button(root, text="SUBMIT INSERTED DATA", command=submit)
submit_btn.grid(row=8, column=0, columnspan=2, pady=10, ipadx=120)

#create Query button
query_btn=Button(root, text="SHOW RECORD(S)", command=show)
query_btn.grid(row=9, column=0, columnspan=2, ipadx=135)

#create select ID Entry and Label
select_id=Entry(root, width=50)
select_id.grid(row=10, column=1, padx=10, pady=20)

select_label=Label(root, text="SELECT ID")
select_label.grid(row=10,column=0)

#create Delete button
erase=Button(root, text="DELETE DATA", command=eraser)
erase.grid(row=11, column=0, columnspan=2, ipadx=149)

#EDIT DATA
#create Delete button
edit=Button(root, text="UPDATE RECORD", command=editor)
edit.grid(row=12, column=0, columnspan=2, pady=10, ipadx=140)

mainloop()