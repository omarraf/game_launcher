"""
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess

# Function to launch games
def launch_game(game):
    try:
        if game == "Clicker Game":
            subprocess.Popen(["python", "clicker_game.py"])
        elif game == "Puzzle Game":
            subprocess.Popen(["python", "puzzle_game.py"])
        elif game == "Adventure Game":
            subprocess.Popen(["python", "adventure_game.py"])
        else:
            messagebox.showinfo("Error", "Game not found!")
    except Exception as e:
        messagebox.showinfo("Error", f"Failed to launch {game}: {e}")

# Function to display game details
def show_game_details(game):
    if game == "Clicker Game":
        game_description.set("Clicker Game: Earn points by clicking as fast as possible. Simple yet fun!")
    elif game == "Puzzle Game":
        game_description.set("Puzzle Game: Solve the puzzles to progress. Brain-teasers galore!")
    elif game == "Adventure Game":
        game_description.set("Adventure Game: Explore a mysterious world filled with challenges.")
    else:
        game_description.set("Select a game to see its details.")

# Main GUI for the launcher
def create_launcher():
    # Initialize Tkinter Window
    root = tk.Tk()
    root.title("Advanced Game Launcher")
    root.geometry("600x400")
    root.configure(bg="#1e1e2f")
    
    # Add Title Label
    title_label = tk.Label(root, text="Fullerton Funhouse - Game Launcher", font=("Arial", 20, "bold"), bg="#1e1e2f", fg="white")
    title_label.pack(pady=20)

    # Game Buttons with Hover Effect
    def on_enter(e, button):
        button.config(bg="#5050f0")

    def on_leave(e, button):
        button.config(bg="#404040")

    clicker_btn = tk.Button(root, text="Clicker Game", font=("Arial", 14), command=lambda: launch_game("Clicker Game"), width=20, bg="#404040", fg="white")
    clicker_btn.pack(pady=10)
    clicker_btn.bind("<Enter>", lambda e: on_enter(e, clicker_btn))
    clicker_btn.bind("<Leave>", lambda e: on_leave(e, clicker_btn))

    puzzle_btn = tk.Button(root, text="Puzzle Game", font=("Arial", 14), command=lambda: launch_game("Puzzle Game"), width=20, bg="#404040", fg="white")
    puzzle_btn.pack(pady=10)
    puzzle_btn.bind("<Enter>", lambda e: on_enter(e, puzzle_btn))
    puzzle_btn.bind("<Leave>", lambda e: on_leave(e, puzzle_btn))

    adventure_btn = tk.Button(root, text="Adventure Game", font=("Arial", 14), command=lambda: launch_game("Adventure Game"), width=20, bg="#404040", fg="white")
    adventure_btn.pack(pady=10)
    adventure_btn.bind("<Enter>", lambda e: on_enter(e, adventure_btn))
    adventure_btn.bind("<Leave>", lambda e: on_leave(e, adventure_btn))

    # Game Description Section
    global game_description
    game_description = tk.StringVar()
    game_description.set("Select a game to see its details.")
    
    description_label = tk.Label(root, textvariable=game_description, wraplength=400, font=("Arial", 12), bg="#1e1e2f", fg="white")
    description_label.pack(pady=20)

    # Add Game Icon Section
    def load_image(filename, size):
        img = Image.open(filename)
        img = img.resize(size, Image.Resampling.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
        return ImageTk.PhotoImage(img)

    clicker_image = load_image("clicker_icon.png", (80, 80))
    puzzle_image = load_image("puzzle_icon.png", (80, 80))
    adventure_image = load_image("adventure_icon.png", (80, 80))

    game_icons_frame = tk.Frame(root, bg="#1e1e2f")
    game_icons_frame.pack(pady=10)

    clicker_icon_label = tk.Label(game_icons_frame, image=clicker_image, bg="#1e1e2f", cursor="hand2")
    clicker_icon_label.grid(row=0, column=0, padx=20)
    clicker_icon_label.bind("<Button-1>", lambda e: show_game_details("Clicker Game"))

    puzzle_icon_label = tk.Label(game_icons_frame, image=puzzle_image, bg="#1e1e2f", cursor="hand2")
    puzzle_icon_label.grid(row=0, column=1, padx=20)
    puzzle_icon_label.bind("<Button-1>", lambda e: show_game_details("Puzzle Game"))

    adventure_icon_label = tk.Label(game_icons_frame, image=adventure_image, bg="#1e1e2f", cursor="hand2")
    adventure_icon_label.grid(row=0, column=2, padx=20)
    adventure_icon_label.bind("<Button-1>", lambda e: show_game_details("Adventure Game"))

    # Exit Button
    exit_btn = tk.Button(root, text="Exit", font=("Arial", 14), command=root.quit, width=20, bg="#FF5733", fg="white")
    exit_btn.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_launcher()

"""

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess

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
    else:
        # Default message when no specific game is selected
        game_description.set("Select a game to see its details.")

# Main GUI for the game launcher
def create_launcher():
    # Initialize Tkinter Window
    root = tk.Tk()
    root.title("Advanced Game Launcher")  # Title of the window
    root.geometry("600x400")  # Size of the window
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

    # Exit Button to close the launcher
    exit_btn = tk.Button(root, text="Exit", font=("Arial", 14), command=root.quit, width=20, bg="#FF5733", fg="white")
    exit_btn.pack(pady=20)

    # Main loop to run the GUI
    root.mainloop()

# Run the launcher
if __name__ == "__main__":
    create_launcher()
