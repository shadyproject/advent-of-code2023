from aocd import get_data


def problem_one(num_red=12, num_green=13, num_blue=14):
    input = get_data(day=2, year=2023)

    valid_game_ids = []

    for game in input.split("\n"):
        (game_id, plays) = game.split(":")
        valid_game = True
        # we don't really care about the "plays" for this just the numbers of colored cubes
        # and replacing ; with , makes it easier to iterate
        plays = plays.replace(";", ",")
        for play in plays.split(","):
            play = play.strip()
            (count, color) = play.split(" ")
            if color == "red":
                if int(count) > num_red:
                    valid_game = False
                    break
            if color == "green":
                if int(count) > num_green:
                    valid_game = False
                    break
            if color == "blue":
                if int(count) > num_blue:
                    valid_game = False
                    break
        if valid_game is True:
            valid_game_ids.append(int(game_id[4:]))

    return sum(valid_game_ids)


def problem_two():
    input = get_data(day=2, year=2023)

    game_powers = []
    for game in input.split("\n"):
        needed = {"red": 0, "green": 0, "blue": 0}

        (_, plays) = game.split(":")
        # still don't really care about the individual sets of the game,
        # so lets make it easier to parse
        plays = plays.replace(";", ",")
        for play in plays.split(","):
            play = play.strip()
            (count, color) = play.split(" ")
            # simple addition here won't work, we need to check if the value is greater and then set it to that
            if int(count) > needed[color]:
                needed[color] = int(count)
        power = needed["red"] * needed["green"] * needed["blue"]
        game_powers.append(power)

    return sum(game_powers)


if __name__ == "__main__":
    print(f"Answer for problem one: {problem_one()}")
    print(f"Answer for problem two: {problem_two()}")
