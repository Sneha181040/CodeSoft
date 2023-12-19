import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoList:
    def __init__(self, box):
        self.box = box
        self.box.title("To-Do List")

        self.tasks = []

        self.task_entry = tk.Entry(self.box, width=50)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(self.box, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(self.box, width=50, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.delete_button = tk.Button(self.box, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=0, pady=5)

        self.update_button = tk.Button(self.box, text="Update Task", command=self.update_task)
        self.update_button.grid(row=3, column=0, pady=5)

        self.clear_button = tk.Button(self.box, text="Clear All", command=self.clear_tasks)
        self.clear_button.grid(row=4, column=0, pady=5)

        self.task_listbox.bind("<Double-Button-1>", self.update_task)

    def add_task(self):
        new_task = self.task_entry.get()
        if new_task:
            self.tasks.append(new_task)
            self.task_listbox.insert(tk.END, new_task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.task_listbox.delete(selected_task_index)
            del self.tasks[selected_task_index[0]]
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            updated_task = simpledialog.askstring("Update Task", "Update Task:", parent=self.box)
            if updated_task:
                self.tasks[selected_task_index[0]] = updated_task
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index[0], updated_task)
        else:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def clear_tasks(self):
        confirmed = messagebox.askokcancel("Confirmation", "Are you sure you want to clear all tasks?")
        if confirmed:
            self.tasks.clear()
            self.task_listbox.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = TodoList(root)
    root.mainloop()

if __name__ == "__main__":
    main()
