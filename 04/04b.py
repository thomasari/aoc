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
accessible_rolls = 1
total_removed_rolls = 0

while accessible_rolls > 0:
    accessible_rolls = 0
    removed_rolls = []
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
                    removed_rolls.append((y, x))
                    accessible_rolls += 1
            if rolls[y][x] == "x":
                rolls[y][x] = "."
    for y, x in removed_rolls:
        rolls[y][x] = "x"
    total_removed_rolls += len(removed_rolls)
    [print("".join(y)) for y in rolls]
    print("removed rolls:", len(removed_rolls))
    print("\n")


print("total removed rolls:", total_removed_rolls)