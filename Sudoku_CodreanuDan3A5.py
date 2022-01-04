import sys
import time
import pygame

pygame.font.init()
# this is the first function that needs to be initialised before the other functionalities - it initiates the font module

WINDOW_HEIGHT = 800
WINDOW_WIDTH = 600
# global variables for window size
window  = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# this is the whole game window - the size can be adjusted

pygame.display.set_caption("SUDOKU")
# window title

x = 0
y = 0
difference = 600 / 9 # the size of a block - as we want a timer, we will use a smaller unit for blocks
value = 0

default_table = [
        [9, 2, 0, 0, 1, 0, 3, 0, 0],
        [8, 5, 0, 0, 9, 0, 0, 2, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [3, 0, 0, 0, 0, 1, 6, 0, 0],
        [1, 9, 7, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 5, 0, 9, 0, 6, 2],
        [0, 8, 5, 0, 2, 0, 4, 0, 0],
        [0, 0, 9, 7, 4, 0, 0, 3, 0]
    ]
# the default table is the one that needs to be solved - inspired from Sudoku.com

first_font = pygame.font.SysFont("Times New Roman", 40)
second_font = pygame.font.SysFont("Times New Roman", 20)
timer_font = pygame.font.SysFont("Times New Roman", 30)
clock = pygame.time.Clock()
counter = 20
timer_text = timer_font.render(str(counter), True, (0, 0, 0))

timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 20000)


def get_coordinates(position):
    global x
    x = position[0] // difference
    global y
    y = position[1] // difference

def highlight_box():
    for i in range(2):
        pygame.draw.line(window, (0, 0, 0), (x * difference - 3, (y + i) * difference), (x * difference + difference + 3, (y + i) * difference), 7)
        pygame.draw.line(window, (0, 0, 0), ((x + i) * difference, y * difference), ((x + i) * difference, y * difference + difference), 7)
# this function is meant to highlight the current cell that the user is going to complete

def draw_table():
    for i in range (9):
        for j in range (9):
            if default_table[i][j] != 0:
                pygame.draw.rect(window, (255, 255, 0), (i * difference, j * difference, difference + 1, difference + 1))
                text1 = first_font.render(str(default_table[i][j]), 1, (0, 0, 0))
                window.blit(text1, (i * difference + 15, j * difference + 15))
    for i in range(10):
        if i % 3 == 0:
            thick = 7
        else:
            thick = 1
        pygame.draw.line(window, (0, 0, 0), (0, i * difference), (600, i * difference), thick)
        pygame.draw.line(window, (0, 0, 0), (i * difference, 0), (i * difference, 600), thick)

# the function draws the entire table, meaning that the lines are drawn

def fill_value(value):
    text = first_font.render(str(value), 1, (0, 0, 0))
    window.blit(text, (x * difference + 15, y * difference + 15))
# the function fills the value from the user into the current cell and it stores the value in the text variable (cast to string)

def first_error():
    text = first_font.render("This is a wrong value! Please try another one!", 1, (0, 0, 0))
    window.blit(text, (15, 680))

def second_error():
    text = first_font.render("Wrong key! Please enter a valid key for the game!", 1, (0, 0, 0))
    window.blit(text, (15, 680))

# the error functions will display a message is a wrong key or value is pressed by the user

def check_value(m, i, j, value):
    for it in range(9):
        if m[i][it]== value:
            return False
        if m[it][j]== value:
            return False
    it = i//3
    jt = j//3
    for i in range(it * 3, it * 3 + 3):
        for j in range (jt * 3, jt * 3 + 3):
            if m[i][j]== value:
                return False
    return True
# the function checks if a value is valid

def solve_game(default_table, i, j):
    while default_table[i][j] != 0:
        if i < 8:
            i += 1
        elif i == 8 and j < 8:
            i = 0
            j += 1
        elif i == 8 and j == 8:
            return True
    pygame.event.pump()
    for it in range(1, 10):
        if check_value(default_table, i, j, it) == True:
            default_table[i][j] = it
            global x, z
            x = i
            z = j
            window.fill((153, 204, 255))
            draw_table()
            highlight_box()
            pygame.display.update()
            pygame.time.delay(20)
            if solve_game(default_table, i, j) == 1:
                return True
            else:
                default_table[i][j] = 0
            window.fill((0, 0, 0))

            draw_table()
            highlight_box()
            pygame.display.update()
            pygame.time.delay(50)
    return False
# function for solving the sudoku is the user is stuck, using recursive method


def instructions():
    default_text = second_font.render("Press D to reset to Default Grid / R to empty the grid!", 1, (0, 0, 0))
    solve_option = second_font.render("Enter values and press enter to visualize the correct solution", 1, (0, 0, 0))
    window.blit(default_text, (20, 610))
    window.blit(solve_option, (20, 630))

def time_up():
    text = first_font.render("Time is UP!", 1, (0, 0, 0))
    window.blit(text, (20, 650))

def show_timer(sec):
    text = str(sec).rjust(3) if sec > 0 else time_up()
    window.blit(text, (620, 670))

def final_result():
    text = first_font.render("Congratulations!" , 1, (0, 0, 0))
    text_2 = first_font.render("You finished the game!", 1, (0, 0, 0))
    window.blit(text, (20, 650))
    window.blit(text_2, (20, 690))


run_window = True
flag1 = 0
flag2 = 0
rs = 0
error = 0

while run_window:
    window.fill((153, 204, 255))
    instructions()
    clock.tick(2000)
    window.blit(timer_text, (470, 670))
    #show_timer(counter)
    for event in pygame.event.get():
        pygame.display.flip()
        if event.type == timer_event:
            counter -= 1
            text = timer_font.render(str(counter), True, (0, 0, 0))
            if counter == 0:
                pygame.time.set_timer(timer_event, 0)
                time_up()
                #run_window = False
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            run_window = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            position = pygame.mouse.get_pos()
            get_coordinates(position)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 1
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                x += 1
                flag1 = 1
            if event.key == pygame.K_UP:
                y -= 1
                flag1 = 1
            if event.key == pygame.K_DOWN:
                y += 1
                flag1 = 1
            if event.key == pygame.K_1:
                value = 1
            if event.key == pygame.K_2:
                value = 2
            if event.key == pygame.K_3:
                value = 3
            if event.key == pygame.K_4:
                value = 4
            if event.key == pygame.K_5:
                value = 5
            if event.key == pygame.K_6:
                value = 6
            if event.key == pygame.K_7:
                value = 7
            if event.key == pygame.K_8:
                value = 8
            if event.key == pygame.K_9:
                value = 9
            if event.key == pygame.K_RETURN:
                flag2 = 1
            if event.key == pygame.K_r:
                rs = 0
                error = 0
                flag2 = 0
                default_table = [
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]
            if event.key == pygame.K_d:
                rs = 0
                error = 0
                flag2 = 0
                default_table = [
                    [9, 2, 0, 0, 1, 0, 3, 0, 0],
                    [8, 5, 0, 0, 9, 0, 0, 2, 0],
                    [0, 0, 3, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 2, 0, 0, 0],
                    [3, 0, 0, 0, 0, 1, 6, 0, 0],
                    [1, 9, 7, 0, 0, 0, 2, 5, 0],
                    [0, 0, 0, 5, 0, 9, 0, 6, 2],
                    [0, 8, 5, 0, 2, 0, 4, 0, 0],
                    [0, 0, 9, 7, 4, 0, 0, 3, 0]
                ]
    if flag2 == 1:
        if not solve_game(default_table, 0, 0):
            error = 1
        else:
            rs = 1
        flag2 = 0
    if value != 0:
        fill_value(value)
        if check_value(default_table, int(x), int(y), value) == True:
            default_table[int(x)][int(y)] = value
            flag1 = 0
        else:
            default_table[int(x)][int(y)] = 0
            second_error()
        value = 0

    if error == 1:
        first_error()
    if rs == 1:
        final_result()
    draw_table()
    if flag1 == 1:
        highlight_box()
        instructions()

    pygame.display.update()


pygame.display.quit()
pygame.quit()
sys.exit()