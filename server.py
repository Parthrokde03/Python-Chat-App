import socket
from tkinter import *
from tkinter import ttk

def send():
    message = entry.get()
    if message.strip() == "":
        return
    chat_listbox.insert(END, "Server: " + message)
    entry.delete(0, END)
    client.send(message.encode('utf-8'))
    receive()

def receive():
    try:
        msg = client.recv(1024).decode('utf-8')
        if msg:
            chat_listbox.insert(END, "Client: " + msg)
    except:
        chat_listbox.insert(END, "Error receiving message")

root = Tk()
root.title("Server Chat")
root.geometry("400x500")
root.resizable(False, False)

chat_frame = Frame(root)
chat_frame.pack(pady=10, fill=BOTH, expand=True)

scrollbar = Scrollbar(chat_frame)
scrollbar.pack(side=RIGHT, fill=Y)

chat_listbox = Listbox(chat_frame, yscrollcommand=scrollbar.set, font=("Arial", 12), bg="white", fg="black")
chat_listbox.pack(fill=BOTH, expand=True)
scrollbar.config(command=chat_listbox.yview)

entry_frame = Frame(root)
entry_frame.pack(pady=10, fill=X)

entry = Entry(entry_frame, font=("Arial", 12))
entry.pack(side=LEFT, padx=10, fill=X, expand=True)

send_button = Button(entry_frame, text="Send", command=send, width=10, bg="#4CAF50", fg="white")
send_button.pack(side=LEFT, padx=5)

receive_button = Button(root, text="Receive", command=receive, bg="#2196F3", fg="white", width=15)
receive_button.pack(pady=5)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 80

s.bind((HOST_NAME, PORT))
s.listen(4)

chat_listbox.insert(END, "Waiting for client to connect...")
client, address = s.accept()
chat_listbox.insert(END, f"Client connected from {address}")

root.mainloop()
