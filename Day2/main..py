# Day2/input.txt

with open("Day2/input.txt") as f:
    lines = f.readlines()

split_lines = []
for line in lines:
    line = line.replace(":", "").replace(",", "").replace(";", "")
    split_lines.append(line.strip().split(" "))


def main():
    cubes = {"red": 12, "blue": 14, "green": 13}
    # for every game/line
    # for every cell in list
    # ignoring the index 0 and 1, if cell in cubes
    # compare the count of cubes in the dict with the count of cell -1 (left) of the cell
    # if the count of the value pair in the dict is lower than the count in the game
    # add the game number to the return value to sum up the games where the cube count is lower

    return_value = 0

    for game in split_lines:
        index = 0
        for cell in game[1:]:
            if cell in cubes:
                if cubes[cell] < int(game[index]):
                    break
                elif index == len(game) - 1:
                    return_value += int(game[0])

            index += 1

    print(return_value)


if __name__ == "__main__":
    main()
