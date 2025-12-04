rolls = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

with open("./04.txt", "r") as f:
  rolls = f.read().strip()

rolls = [[col for col in row] for row in rolls.split("\n")]
directions_y = [-1, -1, 0, 1, 1, 1, 0, -1]
directions_x = [0, 1, 1, 1, 0, -1, -1, -1]
accessible_rolls = 0

for y in range(len(rolls)):
    for x in range(len(rolls[y])):
        adjacent_rolls = 0  
        if rolls[y][x] == "@":
            for i in range(len(directions_y)):
                dir_y = directions_y[i]
                dir_x = directions_x[i]
                if y + dir_y >= 0 and y + dir_y < len(rolls):
                    if x + dir_x >= 0 and x + dir_x < len(rolls[y]):
                        if rolls[y+dir_y][x + dir_x] == "@":
                            adjacent_rolls += 1
            if adjacent_rolls < 4:
                accessible_rolls += 1


print(accessible_rolls)