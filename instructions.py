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
    text_render = timer_font.render(text, True, (0, 0, 0), (255, 255, 255))
    window.blit(text_render, (520, 670))

def final_result():
    text = first_font.render("Congratulations!" , 1, (0, 0, 0))
    text_2 = first_font.render("You finished the game!", 1, (0, 0, 0))
    window.blit(text, (20, 650))
    window.blit(text_2, (20, 690))