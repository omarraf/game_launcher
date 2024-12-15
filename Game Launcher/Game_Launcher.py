

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
import os

# Set the working directory to the script's location
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# Function to launch games based on the selected button
def launch_game(game):
    try:
        # Check which game to launch based on the button clicked
        if game == "Clicker Game":
            subprocess.Popen(["python", "clicker_game.py"])  # Launch Clicker Game
        elif game == "Puzzle Game":
            subprocess.Popen(["python", "puzzle_game.py"])  # Launch Puzzle Game
        elif game == "Adventure Game":
            subprocess.Popen(["python", "adventure_game.py"])  # Launch Adventure Game
        elif game == "Slime Slayer":
            subprocess.Popen(["Slime Slayer Version A.5\\Slime Slayer.exe"])
        else:
            # Show error if the game is not recognized
            messagebox.showinfo("Error", "Game not found!")
    except Exception as e:
        # Handle errors if launching the game fails
        messagebox.showinfo("Error", f"Failed to launch {game}: {e}")

# Function to display the details/description of the selected game
def show_game_details(game):
    # Check which game was clicked and display its description
    if game == "Clicker Game":
        game_description.set("Clicker Game: Earn points by clicking as fast as possible. Simple yet fun!")
    elif game == "Puzzle Game":
        game_description.set("Puzzle Game: Solve the puzzles to progress. Brain-teasers galore!")
    elif game == "Adventure Game":
        game_description.set("Adventure Game: Explore a mysterious world filled with challenges.")
    elif game == "Slime Slayer":
        game_description.set("Slime Slayer: A Hack and Slash Game where you explore and kill all the slimes!")
    else:
        # Default message when no specific game is selected
        game_description.set("Select a game to see its details.")

# Main GUI for the game launcher
def create_launcher():
    # Initialize Tkinter Window
    root = tk.Tk()
    root.title("Advanced Game Launcher")  # Title of the window
    root.geometry("720x720")  # Size of the window
    root.configure(bg="#1e1e2f")  # Background color of the window
    
    # Add Title Label to the window
    title_label = tk.Label(root, text="Fullerton Funhouse - Game Launcher", font=("Arial", 20, "bold"), bg="#1e1e2f", fg="white")
    title_label.pack(pady=20)  # Padding around the title label

    # Add Game Buttons with hover effect for better user experience
    def on_enter(e, button):
        # Change the button color when the mouse enters
        button.config(bg="#5050f0")

    def on_leave(e, button):
        # Revert the button color when the mouse leaves
        button.config(bg="#404040")

    # Button for Clicker Game
    clicker_btn = tk.Button(root, text="Clicker Game", font=("Arial", 14), command=lambda: launch_game("Clicker Game"), width=20, bg="#404040", fg="white")
    clicker_btn.pack(pady=10)  # Padding for the button
    clicker_btn.bind("<Enter>", lambda e: on_enter(e, clicker_btn))  # Bind hover effects
    clicker_btn.bind("<Leave>", lambda e: on_leave(e, clicker_btn))

    # Button for Puzzle Game
    puzzle_btn = tk.Button(root, text="Puzzle Game", font=("Arial", 14), command=lambda: launch_game("Puzzle Game"), width=20, bg="#404040", fg="white")
    puzzle_btn.pack(pady=10)
    puzzle_btn.bind("<Enter>", lambda e: on_enter(e, puzzle_btn))
    puzzle_btn.bind("<Leave>", lambda e: on_leave(e, puzzle_btn))

    # Button for Adventure Game
    adventure_btn = tk.Button(root, text="Adventure Game", font=("Arial", 14), command=lambda: launch_game("Adventure Game"), width=20, bg="#404040", fg="white")
    adventure_btn.pack(pady=10)
    adventure_btn.bind("<Enter>", lambda e: on_enter(e, adventure_btn))
    adventure_btn.bind("<Leave>", lambda e: on_leave(e, adventure_btn))

    #Button for Slime SLayer
    slimeslayer_btn = tk.Button(root, text="Slime Slayer", font=("Arial",14), command=lambda: launch_game("Slime Slayer"), width=20, bg="#404040", fg="white")
    slimeslayer_btn.pack(pady=10)
    slimeslayer_btn.bind("<Enter>", lambda e: on_enter(e, slimeslayer_btn))
    slimeslayer_btn.bind("<Leave>", lambda e: on_leave(e, slimeslayer_btn))


    # Game Description Section (displays when a game is selected)
    global game_description
    game_description = tk.StringVar()  # StringVar is used to dynamically update the label text
    game_description.set("Select a game to see its details.")  # Default description
    
    # Label to display the game description
    description_label = tk.Label(root, textvariable=game_description, wraplength=400, font=("Arial", 12), bg="#1e1e2f", fg="white")
    description_label.pack(pady=20)  # Padding around the description label

    # Add Game Icon Section (each game has its corresponding image icon)
    def load_image(filename, size):
        # Function to load and resize images for icons
        img = Image.open(filename)
        img = img.resize(size, Image.Resampling.LANCZOS)  # Resize the image using LANCZOS filter
        return ImageTk.PhotoImage(img)

    # Load and resize the game icons
    clicker_image = load_image("clicker_icon.png", (80, 80))
    puzzle_image = load_image("puzzle_icon.png", (80, 80))
    adventure_image = load_image("adventure_icon.png", (80, 80))
    slime_slayer_image = load_image("slime_icon.png", (80,80))

    # Frame to contain game icons
    game_icons_frame = tk.Frame(root, bg="#1e1e2f")
    game_icons_frame.pack(pady=10)

    # Clicker Game Icon
    clicker_icon_label = tk.Label(game_icons_frame, image=clicker_image, bg="#1e1e2f", cursor="hand2")
    clicker_icon_label.grid(row=0, column=0, padx=20)  # Grid positioning of the icon
    clicker_icon_label.bind("<Button-1>", lambda e: show_game_details("Clicker Game"))  # Bind the click event to show game details

    # Puzzle Game Icon
    puzzle_icon_label = tk.Label(game_icons_frame, image=puzzle_image, bg="#1e1e2f", cursor="hand2")
    puzzle_icon_label.grid(row=0, column=1, padx=20)
    puzzle_icon_label.bind("<Button-1>", lambda e: show_game_details("Puzzle Game"))

    # Adventure Game Icon
    adventure_icon_label = tk.Label(game_icons_frame, image=adventure_image, bg="#1e1e2f", cursor="hand2")
    adventure_icon_label.grid(row=0, column=2, padx=20)
    adventure_icon_label.bind("<Button-1>", lambda e: show_game_details("Adventure Game"))

    # Slime Slayer Game Icon
    slimeslayer_icon_label = tk.Label(game_icons_frame, image=slime_slayer_image, bg="#1e1e2f", cursor="hand2")
    slimeslayer_icon_label.grid(row=1, column=1, padx=20, pady=20)
    slimeslayer_icon_label.bind("<Button-1>", lambda e: show_game_details("Slime Slayer"))


    # Exit Button to close the launcher
    exit_btn = tk.Button(root, text="Exit", font=("Arial", 14), command=root.quit, width=20, bg="#FF5733", fg="white")
    exit_btn.pack(pady=20)

    # Main loop to run the GUI
    root.mainloop()

# Run the launcher
if __name__ == "__main__":
    create_launcher()
