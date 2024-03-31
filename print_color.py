# ANSI escape codes for different colors
color_codes = {
    'black': '\033[0;30m',
    'red': '\033[0;31m',
    'green': '\033[0;32m',
    'yellow': '\033[0;33m',
    'blue': '\033[0;34m',
    'purple': '\033[0;35m',
    'cyan': '\033[0;36m',
    'white': '\033[0;37m',
    'reset': '\033[0m'  # Reset to default color
}

def print_color_text(text, color, **kwargs):
    color_code = color_codes.get(color.lower())
    if color_code:
        colored_text = f"{color_code}{text}{color_codes['reset']}"
        print(colored_text, **kwargs)
    else:
        print(text, **kwargs)

# # Example usage
# print_color_text("Hello, World!", "red")
# print_color_text("Python is awesome.", "green")
