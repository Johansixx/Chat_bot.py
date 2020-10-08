
import tkinter as tk

def clicked(event):
    newline = '\n'
    chatbox.insert('1.0', f'{entry.get()} {newline}')
    hello = "Hello " + entry.get()
    label.configure(text="The message has been sent!!" )
    label.pack()

window = tk.Tk()
window.title('Chat bot')

entry = tk.Entry(window,width=30)

chatbox = tk.Text()

button = tk.Button(text='Send message')
button.bind("<Button-1>", clicked)

label = tk.Label(
    text='Chatprogram',
    fg='Black',
    bg='white',
    width=100,
    height=5
    )

# label.pack()
chatbox.pack()
entry.pack()
button.pack()

window.mainloop()


