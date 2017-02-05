def line_up(commands):
    positionsFace = 0
    position = 0
    for command in commands:        
        if command == "L" or command == "R":
            position += 90        
        if command == "A":
            position += 180

        if position % 180 == 0:
            positionsFace += 1


    return positionsFace