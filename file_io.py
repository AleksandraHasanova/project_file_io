from tkinter import *
import requests
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import ttk

def get_response():
    try:
        file=fd.askopenfilename()
        if file:
            with open(file, 'rb') as fi:
                f = {'file': fi}
                answer_json = requests.post('https://file.io/', files=f)
                if answer_json.status_code == 200:
                    link = answer_json.json()['link']
                    e.delete(0, END)
                    e.insert(0, link)
    except Exception as ex:
        mb.showerror('Ошибка', f'Произошла ошибка: {ex}')


window = Tk()
window.title('Отправка файлов в file.io')
window.geometry(f'400x300+{window.winfo_screenwidth()//2-200}+{window.winfo_screenheight()//2-150}')

btn = Button(window, text='Выбрать файл', font=('Arial', 16), command=get_response)
btn.pack(pady=10)

e = Entry(window, width=30, font=('Arial', 16))
e.pack(pady=10)

window.mainloop()