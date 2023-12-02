limit = {"green": 13, "blue": 14, "red": 12}

with open("Day2/input.txt", "r") as file:
    games = file.readlines()
    result = 0
    for game in games:
        bad = False
        game_id = int(game.split(":")[0].split()[1])
        subset_balls = {"green": 0, "blue": 0, "red": 0}
        sub_games = game.split(":")[1].split("; ")
        for sub in sub_games:
            sub_game_balls = sub.strip().split(", ")
            for i in sub_game_balls:
                if subset_balls[i.split()[1]] < int(i.split()[0]):
                    subset_balls[i.split()[1]] = int(i.split()[0])
            for i in subset_balls:
                if subset_balls[i] > limit[i]:
                    bad = True
                    break
        if not bad:
            result += game_id
print(result)
