run_window = True
flag1 = 0
flag2 = 0
rs = 0
error = 0
position = []

while run_window:
    
    window.fill((153, 204, 255))
    instructions()
    clock.tick(2000)
    for event in pygame.event.get():
        if event.type == timer_event:
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else 'GG BRO'
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
            print(position)
            get_coordinates(position)
            highlight_box()
        if event.type == pygame.KEYDOWN: ##### 
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
        instructions()
        if position[1] < 601:
            highlight_box()

    window.blit(timer_text, (470, 670))
    show_timer(counter)
    pygame.display.flip()
