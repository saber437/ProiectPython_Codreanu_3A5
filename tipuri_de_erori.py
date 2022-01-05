def first_error():
    text = first_font.render("This is a wrong value! Please try another one!", 1, (0, 0, 0))
    window.blit(text, (15, 680))

def second_error():
    text = first_font.render("Wrong key! Please enter a valid key for the game!", 1, (0, 0, 0))
    window.blit(text, (15, 680))