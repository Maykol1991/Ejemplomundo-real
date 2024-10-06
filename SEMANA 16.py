import tkinter as tk
from tkinter import messagebox


class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("400x400")

        # Task input field
        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.add_task)  # Enter key event

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(root, height=15, width=35, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # Buttons
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Mark Completed", command=self.mark_completed)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Keyboard shortcuts
        self.root.bind("<Escape>", lambda event: root.quit())  # Escape key to close
        self.root.bind("<c>", self.mark_completed)  # 'C' key to mark completed
        self.root.bind("<d>", self.delete_task)  # 'D' key to delete task

    def add_task(self, event=None):
        task = self.entry.get()
        if task != "":
            self.task_listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task")

    def mark_completed(self, event=None):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_task_index)
            self.task_listbox.delete(selected_task_index)
            self.task_listbox.insert(tk.END, f"{task} - Completed")
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to mark as completed")

    def delete_task(self, event=None):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete")


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
