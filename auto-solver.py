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
# function for solving the sudoku fs the user is stuck, using recursive method