from robot import *

bIsCellPainted = False

while not bIsCellPainted:
    while is_free_up() and not bIsCellPainted:
        bIsCellPainted = is_cell_painted()
        if not bIsCellPainted:
            move_up()
    while is_free_down() and not bIsCellPainted:
        bIsCellPainted = is_cell_painted()
        if not bIsCellPainted:
            move_down()
    while is_free_left() and not bIsCellPainted:
        bIsCellPainted = is_cell_painted()
        if not bIsCellPainted:
            move_left()
    while is_free_right() and not bIsCellPainted:
        bIsCellPainted = is_cell_painted()
        if not bIsCellPainted:
            move_right()