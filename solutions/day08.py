import utils

data = utils.day_puzzle_to_list("08")
l = len(data)
w = len(data[0])

n_trees_on_edge = l*2 + (w-2)*2

forest = [list(row) for row in data]


def check_visibility(y, x) -> bool:
    height = forest[y][x]
    from_left = set([forest[y][i] < height for i in range(0, x)]) == {True}
    from_right = set([forest[y][i] < height for i in range(x+1, w)]) == {True}
    from_top = set([forest[i][x] < height for i in range(0, y)]) == {True}
    from_bottom = set([forest[i][x] < height for i in range(y+1, l)]) == {True}
    return from_left or from_right or from_top or from_bottom


to_be_summed = 0
for x in range(1, w-1):
    for y in range(1, l-1):
        to_be_summed += int(check_visibility(x, y))
pt1 = to_be_summed + n_trees_on_edge


def count_view(views: list) -> int:
    ans = 0
    for view in views:
        ans += 1
        if not view:
            break
    return ans


def measure_visibility(y, x) -> int:
    """ Note that view to left and top need to be reversed """
    height = forest[y][x]
    to_left = count_view(
        reversed([forest[y][i] < height for i in range(0, x)])
    )
    to_right = count_view([forest[y][i] < height for i in range(x+1, w)])
    to_top = count_view(
        reversed([forest[i][x] < height for i in range(0, y)])
    )
    to_bottom = count_view([forest[i][x] < height for i in range(y+1, l)])
    return to_left * to_right * to_top * to_bottom


best_view_measure = 1
for x in range(1, w-1):
    for y in range(1, l-1):
        view_measure = measure_visibility(x, y)
        if view_measure > best_view_measure:
            best_view_measure = view_measure
pt2 = best_view_measure

print("Part1:", pt1)
print("Part2:", pt2)
