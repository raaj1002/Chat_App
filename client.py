import tkinter as tk
import time, socket, sys
root = tk.Tk()
root.geometry("500x500")

def send_message():
    message = entry.get()
    entry.delete(0, tk.END)
    chat_text.insert(tk.END, "You: " + message + "\n")

time.sleep(1)

s = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
print(shost, "(", ip, ")\n")
host = input(str("Enter server address: "))
name = input(str("\nEnter your name: "))
port = 1234
print("\nTrying to connect to ", host, "(", port, ")\n") 
time.sleep(1)
s.connect((host, port))
print("Connected...\n")

s.send(name.encode())
s_name = s.recv(1024)
s_name = s_name.decode()
print(s_name, "has joined the chat room\nEnter [e] to exit chat room\n")

while True:
    message = s.recv(1024)
    message = message.decode()
    print(s_name, ":", message)
    message = input(str("Me : "))
    if message == "[e]":
        message = "Left chat room!"
        s.send(message.encode())
        print("\n")
        break
    s.send(message.encode())

chat_frame = tk.Frame(root)
chat_frame.pack(fill=tk.BOTH, expand=True)
scrollbar = tk.Scrollbar(chat_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_text = tk.Text(chat_frame, yscrollcommand=scrollbar.set)
chat_text.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=chat_text.yview)
entry = tk.Entry(root)
entry.pack(side=tk.BOTTOM, fill=tk.X)
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.BOTTOM)

chat_label = tk.Label(root, text="My Chat App")
chat_label.pack(side=tk.TOP)
root.mainloop()
