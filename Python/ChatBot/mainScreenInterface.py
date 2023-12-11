import tkinter as tk
from tkinter import font, PhotoImage
from chatBotInterface import chat_tab

def playbutton():
    user_input = entry.get().strip()  # Get the text from the Entry widget and remove leading/trailing whitespaces
    user_input = user_input if user_input else "Guest"  # Set to "Guest" if the input is empty
    print("Button click with input:", user_input)
    root.destroy()
    chat_tab(user_input)

root = tk.Tk()

# Set the window size
window_width = 500
window_height = 800

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the window position to center it
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

# Set the window geometry
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
root.title("Chat Bot")

# Make the window non-resizable
root.resizable(False, False)

# Load the background image 
image = PhotoImage(file="mainScreenBackground.png")

# Create a label with the background image and add it to the window
background_label = tk.Label(root, image=image)
background_label.place(relwidth=1, relheight=1)

# Create a Courier New font
courier_new_font = font.Font(family="Courier New", size=12)

# Create an entry widget and center it
entry = tk.Entry(root, font=courier_new_font, width=35, justify="center", bd=1.5, relief="solid", highlightthickness=1, highlightcolor="#87CEEB")
entry.place(relx=0.8, rely=0.48, anchor="e", height=50)

# Create a button and center it
# Load a circular image (replace "circle.png" with your circular image)
circle_image = PhotoImage(file="playButton.png")  # Replace with your circular image

# Resize the circular image
new_width = 48  # Replace with your desired width
new_height = 48  # Replace with your desired height
resized_circle_image = circle_image.subsample(int(circle_image.width() / new_width), int(circle_image.height() / new_height))

# Create a round button with the resized circular image
button = tk.Button(root, image=resized_circle_image, command=playbutton, bd=0, highlightthickness=0)
button.place(relx=0.82, rely=0.48, anchor="w")

# Start the Tkinter event loop
root.mainloop()
