from tkinter import *
import requests
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import ttk
import pyperclip
import json
import os

from tkinterweb.utilities import download

history_file = 'upload_history.json'

def save_history(filepath, link):
    history = []
    if os.path.exists(history_file):
        with open(history_file, 'r') as f:
            history = json.load(f)
    history.append({'filepath': os.path.basename(filepath), 'download_link': link})
    with open(history_file, 'w') as f:
        json.dump(history, f, indent=4)




def get_response():
    try:
        filepath=fd.askopenfilename()
        if filepath:
            with open(filepath, 'rb') as f:
                file = {'file': f}
                response = requests.post('https://file.io/', files=file)
                response.raise_for_status()
                link = response.json()['link']
                entry.delete(0, END)
                entry.insert(0, link)
                pyperclip.copy(link)
                save_history(filepath, link)
                mb.showinfo('Ссылка', f'Ссылка {link} успешно скопирована в буфер обмена')
    except Exception as ex:
        mb.showerror('Ошибка', f'Произошла ошибка: {ex}')


window = Tk()
window.title('Отправка файлов в file.io')
window.geometry(f'400x200+{window.winfo_screenwidth()//2-200}+{window.winfo_screenheight()//2-150}')

btn = ttk.Button(window, text='Загрузить файл', command=get_response)
btn.pack(pady=10)

entry = ttk.Entry(window, width=30)
entry.pack(pady=10)

window.mainloop()