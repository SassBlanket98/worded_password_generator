import secrets
import tkinter as tk
from tkinter import ttk

# List of colours.
colors = [
    "red", "blue", "green", "yellow", "orange", "purple", "black", "white",
    "gray", "brown", "pink", "gold", "silver", "bronze", "copper", "platinum",
    "ruby", "sapphire", "emerald", "diamond", "pearl", "opal", "topaz", "amethyst",
    "turquoise", "aquamarine", "peridot", "garnet", "onyx", "jade", "amber", "coral",
    "ivory", "marble", "charcoal", "scarlet", "indigo", "magenta", "cyan", "teal",
    "lavender", "fuchsia", "violet", "peach", "lime", "olive", "mint", "cream"
]

# Revised list of non-colour words (only nouns).
words = [
    "abacus", "balloon", "cactus", "dolphin", "eclipse", "forest", "galaxy", "harbor",
    "island", "jungle", "kingdom", "lighthouse", "mountain", "nebula", "ocean", "pinnacle",
    "quartz", "rainbow", "tornado", "unicorn", "volcano", "waterfall", "xenon", "zenith",
    "aurora", "breeze", "canyon", "desert", "frost", "glacier", "horizon", "icicle",
    "jaguar", "koala", "lagoon", "meadow", "nova", "prairie", "quiver", "raven", "solstice",
    "tempest", "umbra", "valley", "whisper", "xylophone", "yacht", "zephyr", "blizzard",
    "cobalt", "dusk", "ember", "fable", "gale", "harvest", "iris", "jewel", "karma",
    "mist", "nectar", "orbit", "pebble", "quintessence", "ripple", "saffron", "thunder",
    "vortex", "whimsy", "zen", "aether", "boulder", "cascade", "dawn", "echo", "flame",
    "glow", "inertia", "krypton", "luster", "mirage", "nocturne", "oasis", "quasar",
    "reverie", "silhouette", "velvet", "wisp", "solace", "zodiac", "bramble", "dew",
    "enigma", "fog", "glimmer", "halo", "illusion", "jubilee", "kaleidoscope", "labyrinth",
    "nirvana", "onyx", "paradise", "quicksilver", "radiance", "serenity", "twilight",
    "utopia", "whirlpool", "xanadu", "yearning", "zest", "alabaster", "blossom", "crystal",
    "enchantment", "gossamer", "harmony", "infinity", "kismet", "mirth", "paragon",
    "serendipity", "allure", "bloom", "chalice", "felicity", "grace"
]

def generate_password():
    """
    Generate a password by concatenating:
    - A randomly chosen colour (with its first letter capitalized).
    - A randomly chosen noun (with its first letter capitalized).
    - A random three-digit number.
    """
    color = secrets.choice(colors).capitalize()
    word = secrets.choice(words).capitalize()
    number = secrets.randbelow(1000)
    number_str = f"{number:03d}"
    return f"{color}{word}{number_str}"

def update_password():
    """Generate a new password and update the label in the GUI."""
    new_password = generate_password()
    password_label.config(text=new_password)

# Create the main application window.
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x300")
root.resizable(False, False)  # Fixed window size for simplicity.

# Use a themed frame for a modern look.
frame = ttk.Frame(root, padding=20)
frame.pack(expand=True, fill="both")

# Title label.
title_label = ttk.Label(frame, text="Password Generator", font=("Helvetica", 20, "bold"))
title_label.pack(pady=10)

# Label to display the generated password.
password_label = ttk.Label(frame, text="", font=("Helvetica", 18), foreground="#333")
password_label.pack(pady=20)

# Button to trigger password generation.
generate_button = ttk.Button(frame, text="Generate Password", command=update_password)
generate_button.pack(pady=10)

# Optionally, generate an initial password on startup.
update_password()

# Run the application.
root.mainloop()
