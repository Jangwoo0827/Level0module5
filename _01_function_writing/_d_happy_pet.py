"""
Write methods to represent the activities that will make the user's pet happy.
"""
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    Window = Tk()
    Window.withdraw()
    # TODO)
    #   1. Ask the user to enter the type of pet they want (give them a few
    #      choices).
    #   2. Use a loop (maybe a while loop?) to keep offering interactions with
    #      their pet until the desired pet happiness level has been reached.
    #      Examples of activities are: Feed, Walk, Play
    #   3. Write a method for each of the pet activities offered.
    #      Each activity should increase (or decrease) the pet's happiness
    #      level by a different amount, depending on the kind of pet they
    #      have. For example, a fish might not enjoy a walk!
    pass
a = simpledialog.askstring(title="", prompt="What type of pet you want?(dog or cat)")
pet = 0
while True:
    w = simpledialog.askstring(title="", prompt="How are going to make your pet happy?(feed or walk or play)")
    if w == "feed":
        messagebox.showinfo(title="", message="You fed your pet")
        pet = pet + 10
    if w == "walk":
        messagebox.showinfo(title="", message="You walked your pet")
        pet = pet + 10
    if w == "play":
        messagebox.showinfo(title="", message="You played your pet")
        pet = pet + 10
    if pet >= 100:
        messagebox.showinfo(title="", message="Your pet is happy")
        break
