import tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox  
import sqlite3 as sql   
def add_task():  
    # getting the string from the entry field  
    task_string = task_field.get()  
    # checking whether the string is empty or not  
    if len(task_string) == 0:  
        # displaying a message box with 'Empty Field' message  
        messagebox.showinfo('Error', 'Field is Empty.')  
    else:  
        # adding the string to the tasks list  
        tasks.append(task_string)  
        # using the execute() method to execute a SQL statement  
        the_cursor.execute('insert into tasks values (?)', (task_string ,))  
        # calling the function to update the list  
        list_update()  
        # deleting the entry in the entry field  
        task_field.delete(0, 'end')  
  
# defining the function to update the list  
def list_update():  
    # calling the function to clear the list  
    clear_list()  
    # iterating through the strings in the list  
    for task in tasks:  
        # using the insert() method to insert the tasks in the list box  
        task_listbox.insert('end', task)  
  
# defining the function to delete a task from the list  
def delete_task():  
    # using the try-except method  
    try:  
        # getting the selected entry from the list box  
        the_value = task_listbox.get(task_listbox.curselection())    
        if the_value in tasks:  
            # removing the task from the list  
            tasks.remove(the_value)    
            list_update()    
            the_cursor.execute('delete from tasks where title = ?', (the_value,))  
    except: 
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')        
  
# function to delete all tasks from the list  
def delete_all_tasks():   
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')    
    if message_box == True:    
        while(len(tasks) != 0):   
            tasks.pop()   
        the_cursor.execute('delete from tasks')  
        # calling the function to update the list  
        list_update()  
  
# function to clear the list  
def clear_list():   
    task_listbox.delete(0, 'end')  
  
# function to close the application  
def close():   
    print(tasks)  
    guiWindow.destroy()  
  
# function to retrieve data from the database  
def retrieve_database():   
    while(len(tasks) != 0):   
        tasks.pop()   
    for row in the_cursor.execute('select title from tasks'):    
        tasks.append(row[0])  
    
if __name__ == "__main__":   
    guiWindow = tk.Tk()    
    guiWindow.title("To-Do List App")    
    guiWindow.geometry("500x450+750+250")    
    guiWindow.resizable(0, 0)   
    guiWindow.configure(bg = "#005A9C")    
    the_connection = sql.connect('listOfTasks.db')  #connecting database  
    the_cursor = the_connection.cursor()  
    #SQL statement  
    the_cursor.execute('create table if not exists tasks (title text)')   
    tasks = []   
    header_frame = tk.Frame(guiWindow, bg = "#005A9C")  
    functions_frame = tk.Frame(guiWindow, bg = "#005A9C")  
    listbox_frame = tk.Frame(guiWindow, bg = "#005A9C")  
  
    # using the pack() method to place the frames in the application  
    header_frame.pack(fill = "both")  
    functions_frame.pack(side = "left", expand = True, fill = "both")  
    listbox_frame.pack(side = "right", expand = True, fill = "both")  
      
    # defining a label  
    header_label = ttk.Label(  
        header_frame,  
        text = "To-Do List",  
        font = ("Brush Script MT", "30"),  
        background = "#005A9C",  
        foreground = "WHITE"  
    )  
    # using the pack() method to place the label in the application  
    header_label.pack(padx = 20, pady = 20)  
  
    # defining another label using the ttk.Label() widget  
    task_label = ttk.Label(  
        functions_frame,  
        text = "Enter the Task:",  
        font = ("Consolas", "11", "bold"),  
        background = "#FAEBD7",  
        foreground = "#000000"  
    )  
    # using the place() method to place the label in the application  
    task_label.place(x = 30, y = 40)  
      
    # defining an entry field using the ttk.Entry() widget  
    task_field = ttk.Entry(  
        functions_frame,  
        font = ("Consolas", "12"),  
        width = 18,  
        background = "#FFF8DC",  
        foreground = "#A52A2A"  
    )  
    # using the place() method to place the entry field in the application  
    task_field.place(x = 30, y = 80)  
  
    # adding buttons to the application using the ttk.Button() widget  
    add_button = ttk.Button(  
        functions_frame,  
        text = "Add Task",  
        width = 24,  
        command = add_task  
    )  
    del_button = ttk.Button(  
        functions_frame,  
        text = "Delete Task",  
        width = 24,  
        command = delete_task  
    )  
    del_all_button = ttk.Button(  
        functions_frame,  
        text = "Delete All Tasks",  
        width = 24,  
        command = delete_all_tasks  
    )  
    exit_button = ttk.Button(  
        functions_frame,  
        text = "Exit",  
        width = 24,  
        command = close  
    )  
    # using the place() method to set the position of the buttons in the application  
    add_button.place(x = 30, y = 120)  
    del_button.place(x = 30, y = 160)  
    del_all_button.place(x = 30, y = 200)  
    exit_button.place(x = 30, y = 240)  
  
    # defining a list box using the tk.Listbox() widget  
    task_listbox = tk.Listbox(  
        listbox_frame,  
        width = 26,  
        height = 13,  
        selectmode = 'SINGLE',  
        background = "#FFFFFF",  
        foreground = "#000000",  
        selectbackground = "#CD853F",  
        selectforeground = "#FFFFFF"  
    )  
    task_listbox.place(x = 10, y = 20)  
   
    retrieve_database()  
    list_update()  
    guiWindow.mainloop()  
    # establishing the connection with database  
    the_connection.commit()  
    the_cursor.close()  
