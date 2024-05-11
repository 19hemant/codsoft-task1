import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        tasks.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    try:
        selected_index = tasks.curselection()[0]
        tasks.delete(selected_index)
    except IndexError:
        pass

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Task Entry
task_entry = tk.Entry(root, width=35, font=15)
task_entry.pack(padx=20, pady=25)

# Add Task Button
add_button = tk.Button(root, text="Add Task",  width=20, command=add_task, background="skyblue")
add_button.pack(padx=15, pady=11)


# Task List
tasks = tk.Listbox(root, width=40, height=10, font=15, background="lightgray")
tasks.pack(padx=10, pady=10)

# Delete Task Button
delete_button = tk.Button(root, text="Delete Task", width=20, command=delete_task, background="red")
delete_button.pack(padx=10, pady=5)

root.mainloop()
