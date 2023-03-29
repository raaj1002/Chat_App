import tkinter as tk
import time, socket, sys
root = tk.Tk()
root.geometry("500x500")
def send_message():
    message = entry.get()
    entry.delete(0, tk.END)
    chat_text.insert(tk.END, "You: " + message + "\n")
    
s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 1234
s.bind((host, port))
print(host, "(", ip, ")\n")
name = input(str("Enter your name: "))
           
s.listen(1)
print("\nWaiting for incoming connections...\n")
conn, addr = s.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")

s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name, "has connected to the chat room\nEnter [e] to exit chat room\n")
conn.send(name.encode())

while True:
    message = input(str("Me : "))
    if message == "[e]":
        message = "Left chat room!"
        conn.send(message.encode())
        print("\n")
        break
conn.send(message.encode())
message = conn.recv(1024)
message = message.decode()
print(s_name, ":", message)

chat_label = tk.Label(root, text="My Chat App")
chat_label.pack(side=tk.TOP)
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

root.mainloop()
