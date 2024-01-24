# import the tkinter module
from tkinter import *

# Initializing adding item function
def add_item(entry: Entry, listbox: Listbox):
    new_task = entry.get()
    if new_task:
        listbox.insert(END, new_task)
        with open(r'\LearnProgramming\PYTHoN\MyApps\ToDolist-App\notes.txt', 'a') as tasks_list_file:
            tasks_list_file.write(f"\n{new_task}")

        # Clear the entry field after adding a new task
        entry.delete(0, END)

# Initializing delete item function
def delete_item(listbox: Listbox):
    selected_index = listbox.curselection()
    if selected_index:
        listbox.delete(selected_index)
        with open(r'\LearnProgramming\PYTHoN\MyApps\ToDolist-App\notes.txt', 'r') as tasks_list_file:
            lines = tasks_list_file.readlines()
        with open(r'\LearnProgramming\PYTHoN\MyApps\ToDolist-App\notes.txt', 'w') as tasks_list_file:
            for line in lines:
                if listbox.get(ACTIVE) == line.strip():
                    continue
                tasks_list_file.write(line)
                
# Initializing the GUI window
root = Tk()
root.title("ToDoList by saad")
root.geometry('300x400')
root.resizable(0, 0)
root.config(bg="yellow")

# Heading label
Label(root, text="ToDoList by saad", bg="white", font=("Comic Sans MS", 15), wraplength=300).place(x=60, y=0)

# Add list box with all the tasks and scroll bar
tasks = Listbox(root, selectbackground="gold", bg="silver", font=('Helvetica', 12), height=12, width=25)
scroller = Scrollbar(root, orient="vertical", command=tasks.yview)
scroller.place(x=260, y=50, height=230)
tasks.config(yscrollcommand=scroller.set)
tasks.place(x=35, y=50)

# Adding items to the list box
with open('\LearnProgramming\PYTHoN\MyApps\ToDolist-App\\notes.txt', 'r+') as task_list:
    for task in task_list:
        tasks.insert(END, task.strip())  # Use strip() to remove leading/trailing whitespaces

# Creating the Entry widget where the user can enter a new item
new_item_entry = Entry(root, width=37)
new_item_entry.place(x=35, y=310)

# Creating the buttons
add_button = Button(root, text="add item", bg="white", width=10, font=('Helvetica', 12), command=lambda: add_item(new_item_entry, tasks))
add_button.place(x=45, y=340)
delete_button = Button(root, text="delete item", bg="white", width=10, font=('Helvetica', 12), command=lambda: delete_item(tasks))
delete_button.place(x=160, y=340)

# Finalizing the window
root.update()
root.mainloop()