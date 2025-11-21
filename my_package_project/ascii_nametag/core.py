import pyfiglet

class NameTagGenerator:
    def __init__(self, font='slant'):
        self.font = font

    def generate(self, text):
        ascii_art = pyfiglet.figlet_format(text, font=self.font)
        border = "=" * 40
        return f"{border}\n{ascii_art}{border}"

    def print_tag(self, text):
        print(self.generate(text))
