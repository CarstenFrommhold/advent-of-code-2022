import utils

data = utils.day_puzzle_to_list("10")
instructions = [d.split(" ") for d in data]

X = [(1, 1)]

for exec_ in instructions:
    start = X[-1][1]
    if exec_ == ['noop']:
        X.append((start, start))
    else:
        increase = int(exec_[1])
        X.append((start, start))
        X.append((start, start + increase))

pt1 = X[20][0] * 20 + X[60][0] * 60 + X[100][0] * 100 + X[140][0] * 140 + X[180][0] * 180 + X[220][0] * 220
print("Part 1:", pt1)


def sprite_covers_pixel(X: int, pos: int) -> bool:
    return abs(X-pos) <= 1


def draw(X: int, pos: int) -> str:
    if sprite_covers_pixel(X, pos):
        return "#"
    else:
        return "."


def jump_row(pos: int, X: int) -> int:
    if pos % 40 == 0:
        return X + 40
    else:
        return X


X = [(2, 2)]
pic = ["0"]
pos = 0
for exec_ in instructions:
    pos += 1
    start = X[-1][1]
    start = jump_row(pos, start)
    if exec_ == ['noop']:
        X.append((start, start))
        pic.append(draw(start, pos))
    else:
        increase = int(exec_[1])
        pic.append(draw(start, pos))
        X.append((start, start))
        pos += 1
        start = jump_row(pos, start)
        X.append((start, start + increase))
        pic.append(draw(start, pos))

print("Part 2:")
print(pic[1:41])
print(pic[41:81])
print(pic[81:121])
print(pic[121:161])
print(pic[161:201])
print(pic[201:241])
