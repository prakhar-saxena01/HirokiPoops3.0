def check_and_save_score(score: int):
    with open("saves/highscore.txt") as f:
        previous_score = int(f.read())
    if score > previous_score:
        save_score(score)


def save_score(score: int):
    with open("saves/highscore.txt", "w") as f:
        f.write(str(score))
