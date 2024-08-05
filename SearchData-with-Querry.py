from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
import MysqlDBHelper as dbss

root = Tk()
root.title("Database Table Viewer")
root.state("zoomed")

def selectInList(typStrV):
    listboxss.selection_clear(0, 'end')
    if typStrV == "":
        return
    lennn = len(typStrV)
    rowV = 0

    for item in listVar.get():
        it = item[:lennn]

        if it.lower() == typStrV.lower():
            listboxss.select_set(rowV)
            listSelectIndex = rowV
            listboxss.see(rowV)
            break
        rowV = rowV + 1

def selectedlana():
    if entno == 'databaseN':
        selectInList(entry_database_namee.get())
        entry_database_namee.set(listboxss.get(listboxss.curselection()[0]))
    if entno == 'tableN':
        selectInList(entry_table_namee.get())
        entry_table_namee.set(listboxss.get(listboxss.curselection()[0]))
    if entno == 'entry':
        selectInList(entry_column_namee.get())
        entry_column_namee.set(listboxss.get(listboxss.curselection()[0]))
    if entno == 'entry1':
        selectInList(entry_column_namee1.get())
        entry_column_namee1.set(listboxss.get(listboxss.curselection()[0]))
    if entno == 'entry2':
        selectInList(entry_OderBy_namee.get())
        entry_OderBy_namee.set(listboxss.get(listboxss.curselection()[0]))
        
def entert(wht):
    print("aaaaaa2", wht)
    selectedlana()
    pass


def focusoutt(wht):
    print("aaaaaa2", wht)
    selectedlana()
    pass

def focusintt(wht):
    global entno
    if wht == 'databasea':
        entno = 'databaseN'
    if wht == 'tablea':
        entno = 'tableN'
    if wht == 'entryy':
        entno = 'entry'
    if wht == 'entryy1':
        entno = 'entry1'
    if wht == 'entryy2':
        entno = 'entry2'
    List_bharna(wht)

def selectInList2(wht):
    filtered_databases = []
    if wht == 'databasea':
        selectInList(entry_database_namee.get())
        
    if wht == 'tablea':
        selectInList(entry_table_namee.get())
        
    if wht == 'entryy':
        selectInList(entry_column_namee.get())
    
    if wht == 'entryy1':
        selectInList(entry_column_namee1.get())
    
    if wht == 'entryy2':
        selectInList(entry_OderBy_namee.get())
    
    if  len(filtered_databases) == 0:
        return
   
    
    for item in filtered_databases:
        listboxss.insert(END, item)


def List_bharna(wht):
    filtered_databases = []
    print(wht)
    listboxss.delete(0, 'end')
    if wht == 'databasea':
        databases = dbss.fetch_databases()
        filtered_databases = [db for db in databases if db.lower()]
        listboxss.place(x=enter_database_name.winfo_rootx(), y=10 + enter_database_name.winfo_height())
    if wht == 'tablea':
        database_name = entry_database_namee.get()
        filtered_databases = dbss.fetch_tables(database_name)
        print("hhhhh", filtered_databases)
        listboxss.place(x=enter_table_name.winfo_rootx(), y=10 + enter_table_name.winfo_height())
    
    if wht == 'entryy':
        database_name = entry_database_namee.get()
        table_name = entry_table_namee.get()
        filtered_databases = dbss.fetch_columns(database_name, table_name)
        listboxss.place(x=enter_sql_querry.winfo_rootx(), y=10 + enter_sql_querry.winfo_height())
    
    if wht == 'entryy1':
        database_name = entry_database_namee.get()
        table_name = entry_table_namee.get()
        filtered_databases = dbss.fetch_columns(database_name, table_name)
        listboxss.place(x=enter_sql_querry2.winfo_rootx(), y=10 + enter_sql_querry2.winfo_height())
    
    if wht == 'entryy2':
        database_name = entry_database_namee.get()
        table_name = entry_table_namee.get()
        filtered_databases = dbss.fetch_columns(database_name, table_name)
        listboxss.place(x=enter_OderBy_name.winfo_rootx(), y=10 + enter_OderBy_name.winfo_height())
    
    if len(filtered_databases) == 0:
        return
    
    for item in filtered_databases:
        listboxss.insert(END, item)

def on_select(event):
    print("aaaaaa")
    selectInList(entry_database_namee.get())
       
def fetch_table_data(event):
    def get_value(event):
        selected_value = tree.selection()
        
        if selected_value:
            values = tree.item(selected_value, "values")
            for i in range(len(col_types)):
                entry_list[i].delete(0, END)
                entry_list[i].insert(0, values[i])
    tree = ttk.Treeview(my_framee)
    tree.place(x=40, y=25, width=1250)
    tree.bind('<Double-Button-1>', get_value)
    tree.bind('<Return>', get_value)
    
    database_name = entry_database_namee.get()
    table_name = entry_table_namee.get()
    sqlsql = entry_column_namee.get()
    orderr = entry_OderBy_namee.get()
    quess1 = entry_column_namee.get()
    anss1 = entry_sql_querry1.get()
    quess2 = entry_column_namee1.get()
    anss2 = entry_sql_querry3.get()
    
    global entry_list, col_types, sql_query_entry

    entry_list = []

    if not database_name or not table_name:
        messagebox.showwarning("Input Error", "Please enter both database and table names")
        return
    
    try:
        conn = mysql.connector.connect(
            host="localhost", 
            user="root",  
            password="",  
            database=database_name
        )
        cursor = conn.cursor()
        
        mysqll = ''
        if quess1:
            mysqll = f"SELECT * FROM {table_name} WHERE {quess1} = '{anss1}'"
        if quess2:
            mysqll = f"SELECT * FROM {table_name} WHERE {quess1} = '{anss1}' AND {quess2} = '{anss2}'"
        if orderr:
            mysqll = f"SELECT * FROM {table_name} WHERE {quess1} = '{anss1}' AND {quess2} = '{anss2}' ORDER BY {orderr}"
            
        print("aaa",mysqll)
        cursor.execute(mysqll)
        rows = cursor.fetchall()
        columns = cursor.column_names
        
        cursor.execute(f"SHOW COLUMNS FROM {table_name}")
        col_info = cursor.fetchall()
        col_types = [col[1][:4] for col in col_info]
        conn.close()
        xx = 40
        
        for i in range(len(col_types)):
            txtVV = StringVar()
            col_type = col_types[i]
            if col_type == "int(":
                widthe = 40
            if col_type == "varc":
                widthe = 65
            if col_type == "date":
                widthe = 100
            if col_type == "tiny":
                widthe = 30
                
            my_entryy = Entry(my_framee, textvariable=txtVV)
            my_entryy.place(x=xx, y=60, width=widthe)
            entry_list.append(my_entryy)
            xx += widthe
        
        for i in tree.get_children():
            tree.delete(i)
        
        if rows:
            tree["columns"] = columns
            tree["show"] = "headings"
            trwi = 0
            for idx, col in enumerate(columns):
                col_type = col_types[idx]
                widthe = 100  
                if col_type == "int(":
                    widthe = 40
                elif col_type == "varc":
                    widthe = 65
                elif col_type == "date":
                    widthe = 100
                elif col_type == "tiny":
                    widthe = 30
                trwi += widthe
                tree.column(col, width=widthe, minwidth=1)
                tree.heading(col, text=col)
            tree.place(x=40, y=80, width=trwi)
            for row in rows:
                tree.insert("", "end", values=row)
        else:
            messagebox.showinfo("No Data", f"No data found in table '{table_name}'")
        
        # Create or update the SQL query Entry widget
        if 'sql_query_entry' in globals():
            sql_query_entry.destroy()
        
        sql_query_var = StringVar()
        sql_query_entry = Entry(frame, textvariable=sql_query_var, width=40)
        sql_query_entry.place(x=180, y=130, height=30, width=500)
        sql_query_var.set(mysqll)
        
        sql_query_var1 = StringVar()
        sql_query_entry1 = Entry(frame, textvariable=sql_query_var1, width=40)
        sql_query_entry1.place(x=0, y=50, height=30, width=600)
        sql_query_var1.set(mysqll)

    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", str(e))
    
    def update_query():
        mysqllll = sql_query_entry.get()
        conn = mysql.connector.connect(
                    host="localhost", 
                    user="root",  
                    password="",  
                    database=database_name
                )
        cursor = conn.cursor()
        cursor.execute(mysqllll)
        rows = cursor.fetchall()
        columns = cursor.column_names
        
        cursor.execute(f"SHOW COLUMNS FROM {table_name}")
        col_info = cursor.fetchall()
        col_types = [col[1][:4] for col in col_info]
        conn.close()
        xx = 40
        
        for i in range(len(col_types)):
            txtVV = StringVar()
            col_type = col_types[i]
            if col_type == "int(":
                widthe = 40
            if col_type == "varc":
                widthe = 65
            if col_type == "date":
                widthe = 100
            if col_type == "tiny":
                widthe = 30
                
            my_entryy = Entry(my_framee, textvariable=txtVV)
            my_entryy.place(x=xx, y=60, width=widthe)
            entry_list.append(my_entryy)
            xx += widthe
        
        for i in tree.get_children():
            tree.delete(i)
        
        if rows:
            tree["columns"] = columns
            tree["show"] = "headings"
            trwi = 0
            for idx, col in enumerate(columns):
                col_type = col_types[idx]
                widthe = 100  
                if col_type == "int(":
                    widthe = 40
                elif col_type == "varc":
                    widthe = 65
                elif col_type == "date":
                    widthe = 100
                elif col_type == "tiny":
                    widthe = 30
                trwi += widthe
                tree.column(col, width=widthe, minwidth=1)
                tree.heading(col, text=col)
            tree.place(x=40, y=80, width=trwi)
            for row in rows:
                tree.insert("", "end", values=row)
        else:
            messagebox.showinfo("No Data", f"No data found in table '{table_name}'")
        
        # Create or update the SQL query Entry widget
        if 'sql_query_entry' in globals():
            sql_query_entry.destroy()
            
    def insert_value():
        new_values = [entry_list[i].get() for i in range(len(col_types))]
        print("valuesss",new_values)
        tree.insert("", "end", values=new_values)
        valuee = new_values.pop(0)
        print("hhh", new_values)
        dbss.insert_txtsetting(dataa=new_values)
    
    
    
    def update_value(event):
        selected_value = tree.selection()
        if selected_value:
            new_values = [entry_list[i].get() for i in range(len(col_types))]
            tree.item(selected_value, values=new_values)
            
            primary_key_value = tree.item(selected_value, "values")[0]
            primary_key_column = columns[0]

            set_clause = ", ".join([f"{columns[i]} = %s" for i in range(len(columns))])
            update_query = f"UPDATE {table_name} SET {set_clause} WHERE {primary_key_column} = %s"
            update_values = new_values + [primary_key_value]

            try:
                conn = mysql.connector.connect(
                    host="localhost", 
                    user="root",  
                    password="",  
                    database=database_name
                )
                cursor = conn.cursor()
                cursor.execute(update_query, update_values)
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Row updated successfully")
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", e)
            
            for entry in entry_list:
                entry.delete(0, END)
    
    def delete_value():
        selected_value = tree.selection()
        print("hhhh11", selected_value)
        if selected_value:
            values = tree.item(selected_value, "values")
            print("valueee", values)
            # Get the primary key value for deletion
            primary_key_value = tree.item(selected_value, "values")[0]
            primary_key_column = columns[0]
            print("hhhh",primary_key_column)
            sss= dbss.deleteData('ID',values[0],'null','','txtsetting', 'settingg')

            # Clear the entries
            for entry in entry_list:
                entry.delete(0, END)

            # Remove the item from the tree view
            tree.delete(selected_value)
            
    btnn = Button(my_framee, text="Insert", command=insert_value)
    btnn.place(x=80, y=350)
    
    btnn2 = Button(my_framee, text="Update Value", command=update_value)
    btnn2.place(x=150, y=350)
    btnn2.bind("<Return>", update_value)
    
    btnn3 = Button(text="Update", command=update_query)
    btnn3.place(x=120, y=130)
    
    btnn4 = Button(my_framee, text="Delete record", command=delete_value)
    btnn4.place(x=270, y=350) 
    btnn4.bind("<Return>")
    
    

frame = Frame(root)
frame.place(x=10, y=0, width=3000, height=700)

Label(frame, text="Database Name:").grid(column=0, row=0)
entry_database_namee = StringVar()
enter_database_name = Entry(frame, textvariable=entry_database_namee, width=30)
enter_database_name.grid(column=1, row=0, padx=10)
enter_database_name.bind("<FocusIn>",lambda event, wht = 'databasea': focusintt(wht))
enter_database_name.bind("<KeyRelease>",lambda event, wht = 'databasea': selectInList2(wht))
enter_database_name.bind("<Return>",lambda event, wht = 'databasea': entert(wht))
enter_database_name.bind("<FocusOut>",lambda event, wht = 'databasea': focusoutt(wht))

Label(frame, text="Table Name:").grid(column=3, row=0, padx=10)
entry_table_namee = StringVar()
enter_table_name = Entry(frame, textvariable=entry_table_namee, width=30)
enter_table_name.grid(column=4, row=0)
enter_table_name.bind("<FocusIn>",lambda event, wht = 'tablea': focusintt(wht))
enter_table_name.bind("<KeyRelease>",lambda event, wht = 'tablea': selectInList2(wht))
enter_table_name.bind("<Return>",lambda event, wht = 'tablea': entert(wht))
enter_table_name.bind("<FocusOut>",lambda event, wht = 'tablea': focusoutt(wht))

Label(frame, text="SQL:").grid(column=5, row=0, padx=10)

entry_column_namee = StringVar()
enter_sql_querry = Entry(frame, textvariable=entry_column_namee, width=30)
enter_sql_querry.grid(column=6, row=0)
enter_sql_querry.bind("<FocusIn>",lambda event, wht = 'entryy': focusintt(wht))
enter_sql_querry.bind("<KeyRelease>",lambda event, wht = 'entryy': selectInList2(wht))
enter_sql_querry.bind("<Return>",lambda event, wht = 'entryy': entert(wht))
enter_sql_querry.bind("<FocusOut>",lambda event, wht = 'entryy': focusoutt(wht))

entry_sql_querry1 = StringVar()
enter_sql_querry1 = Entry(frame, textvariable=entry_sql_querry1, width=20)
enter_sql_querry1.grid(column=7, row=0)

entry_column_namee1 = StringVar()
enter_sql_querry2 = Entry(frame, textvariable=entry_column_namee1, width=30)
enter_sql_querry2.grid(column=8, row=0)
enter_sql_querry2.bind("<FocusIn>",lambda event, wht = 'entryy1': focusintt(wht))
enter_sql_querry2.bind("<KeyRelease>",lambda event, wht = 'entryy1': selectInList2(wht))
enter_sql_querry2.bind("<Return>",lambda event, wht = 'entryy1': entert(wht))
enter_sql_querry2.bind("<FocusOut>",lambda event, wht = 'entryy1': focusoutt(wht))

entry_sql_querry3 = StringVar()
enter_sql_querry3 = Entry(frame, textvariable=entry_sql_querry3, width=20)
enter_sql_querry3.grid(column=9, row=0)


Label(frame, text=" Order By:").grid(column=10, row=0, padx=10)
entry_OderBy_namee = StringVar()
enter_OderBy_name = Entry(frame, textvariable=entry_OderBy_namee, width=60)
enter_OderBy_name.grid(column=11, row=0)
enter_OderBy_name.bind("<FocusIn>",lambda event, wht = 'entryy2': focusintt(wht))
enter_OderBy_name.bind("<KeyRelease>",lambda event, wht = 'entryy2': selectInList2(wht))
enter_OderBy_name.bind("<Return>",lambda event, wht = 'entryy2': entert(wht))
enter_OderBy_name.bind("<FocusOut>",lambda event, wht = 'entryy2': focusoutt(wht))

btn_show = Button(frame, text="Show Data")
btn_show.place(x=20, y=130)
btn_show.bind("<Return>", fetch_table_data)

my_framee = Frame(root, width=1250, height=5000)
my_framee.place(x=0, y=170)

db_list_frame = Frame(root, width=200, height=150)

table_list_frame = Frame(root, width=200, height=150)
columnsList = Frame(root, width=200, height=150)
listVar = Variable(value=[])
listboxss = Listbox(root,listvariable=listVar)
listboxss.bind("<KeyRelease>", on_select)

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

root.mainloop()
