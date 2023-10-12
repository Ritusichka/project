import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)

def remove_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.delete(selected_task)

def complete_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.itemconfig(selected_task, {'bg': 'light green'})

# Создание главного окна
app = tk.Tk()
app.title("To-Do List")

# Создание и настройка элементов интерфейса
entry = tk.Entry(app)
add_button = tk.Button(app, text="Добавить задачу", command=add_task)
remove_button = tk.Button(app, text="Удалить задачу", command=remove_task)
complete_button = tk.Button(app, text="Выполнить задачу", command=complete_task)
task_list = tk.Listbox(app)

# Размещение элементов на окне
entry.pack()
add_button.pack()
remove_button.pack()
complete_button.pack()
task_list.pack()

# Запуск главного цикла приложения
app.mainloop()
