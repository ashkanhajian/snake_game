from tkinter import *
from random import randint


class Snake:
    def __init__(self):
        self.body_size = BODY_SIZE
        self.coordinates = []
        self.square = []
        for i in range(0, BODY_SIZE):
            self.coordinates.append([0, 0])
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tags='snake')
            self.square.append(square)


class Food:
    def __init__(self):
        x = randint(0, (GAME_WITH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tags='food')


# BUTTON
def restart_program():
    pass


# varietals
GAME_WITH = 700
GAME_HEIGHT = 700
SPACE_SIZE = 50
SLOWNESS = 200
BODY_SIZE = 2
SNAKE_COLOR = 'GREEN'
BACKGROUND_COLOR = 'BLACK'
FOOD_COLOR = 'RED'
score = 0
direction = 'down'
#
window = Tk()
window.title('snake game')
window.resizable(False, False)
label = Label(window, text=f"score:{score}", font=('Arial', 30))
label.pack()
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WITH)
canvas.pack()
restart = Button(window, text='Restart', fg='red', command=restart_program)
restart.pack()
# window_width = window.winfo_width()
# window_height = window.winfo_height()
# screen_width = window.winfo_screenwidth()
# screen_height = window.winfo_screenheight()
# x = int((screen_width / 2) - (window_height / 2))
# y = int((screen_width / 2) - (window_height / 2))
# window.geometry(f"{window_width}x{window_height}+{x}+{y}")
snake = Snake()
food = Food()
window.mainloop()
