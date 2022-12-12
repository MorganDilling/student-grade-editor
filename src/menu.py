import pyChalk

colours = pyChalk.pyChalk()

class Menu:
    def __init__(self, title:str, options):
        self.title = title.capitalize()
        self.options = options

    def display(self):
        print(colours.header(self.title + ":"))
        for i, option in enumerate(self.options): 
            green = colours.green(str(i + 1) + ":")
            print(f"{colours.bold( green ) } {option}")

    def run(self):
        while True:
            self.display()
            try:
                choice = int(input(colours.bold("Enter your choice: ")))
                if choice == 0:
                    break
                elif 0 < choice <= len(self.options):
                    return choice - 1
                else:
                    print(colours.warn("Invalid choice"))
            except ValueError:
                print(colours.warn("Invalid choice"))

def Prompt(text:str, noEmpty:bool = False):
    while True:
        response = input(colours.header(text) + " ")
        if noEmpty and response == "":
            print(colours.warn("Response cannot be empty"))
        else:
            return response
def NumberPrompt(text:str, min:int = None, max:int = None):
    while True:
        try:
            number = int(input(colours.header(text) + " "))
            if min != None and number < min:
                print(colours.warn(f"Number must be greater than or equal to {min}"))
            elif max != None and number > max:
                print(colours.warn(f"Number must be less than or equal to {max}"))
            else:
                return number
        except ValueError:
            print(colours.warn("Invalid number"))