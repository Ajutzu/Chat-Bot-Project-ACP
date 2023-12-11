import tkinter as tk
from tkinter import font, PhotoImage
from chatBot import get_response

def send_message(name):
    message = entry.get()
    chat_box.config(state=tk.NORMAL)

    # Insert the user's message with right alignment and red name
    chat_box.insert(tk.END, f"\n{name}:", ("user", "red_name"))
    chat_box.insert(tk.END, f" {message}\n  ", "user_message")

    response = get_bot_response(message)

    # Insert the bot's response with left alignment and blue "ChatBot:"
    chat_box.insert(tk.END, f"  \nChatBot:", ("bot", "blue_bot"))
    chat_box.insert(tk.END, f" {response}\n", "bot_message")

    chat_box.config(state=tk.DISABLED)
    chat_box.yview(tk.END)
    entry.delete(0, tk.END)

def get_bot_response(user_message):
    answer = get_response(user_message)
    return answer

def chat_tab(name):
    global entry, chat_box  # Declare entry and chat_box as global variables
    root = tk.Tk()

    courier_new_font = font.Font(family="Courier New", size=12)
    window_width = 500
    window_height = 800
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    root.resizable(False, False)

    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    root.title("Chat Bot")

    image = PhotoImage(file="chatScreenBackground.png")
    background_label = tk.Label(root, image=image)
    background_label.place(relwidth=1, relheight=1)

    chat_frame = tk.Frame(root)
    chat_box = tk.Text(chat_frame, height=33, width=60, bd=1, relief="solid", font=courier_new_font, wrap="word")
    chat_box.tag_configure("user", justify="right", foreground="red")  # Set the name color to red
    chat_box.tag_configure("bot", justify="left", foreground="blue")  # Set the "ChatBot:" text color to blue
    chat_box.tag_configure("red_name", foreground="red")  # Set the name color to red
    chat_box.tag_configure("user_message", foreground="black")  # Set the user message color to black
    chat_box.tag_configure("bot_message", foreground="black")  # Set the bot message color to black
    chat_box.config(state=tk.DISABLED)
    scrollbar = tk.Scrollbar(chat_frame, command=chat_box.yview)
    chat_box['yscrollcommand'] = scrollbar.set

    chat_box.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    chat_frame.pack(padx=10, pady=10)

    entry_frame = tk.Frame(root)
    entry = tk.Entry(root, font=courier_new_font, width=47, justify="center", bd=1, relief="solid", highlightthickness=1, highlightcolor="#87CEEB")
    entry.place(relx=0.5, rely=0.87, anchor="center", height=50)

    # Bind the <Return> key to send_message function
    entry.bind("<Return>", lambda event: send_message(name))

    entry_frame.pack(pady=10)

    root.mainloop()
