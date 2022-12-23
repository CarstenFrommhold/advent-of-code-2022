import utils

data = utils.day_puzzle_to_list("21")
int_str = [str(i) for i in range(1, 10)]


def parse(data):
    equations = []
    known_values = dict()
    for d in data:
        if any([s in int_str for s in d]):
            monkey_name, shout = d.split(": ")
            known_values[monkey_name] = int(shout)
        else:
            equations.append(d)
    return equations, known_values


equations, known_values = parse(data)


def get_x1(eq: str) -> str:
    return eq[0:4]


def solve(eq: str, known_values: dict):
    x1 = eq[0:4]
    x2 = eq[6:10]
    x3 = eq[13:17]
    operator = eq[11]
    x2_v = known_values.get(x2)
    x3_v = known_values.get(x3)
    if x2_v and x3_v:
        result = {"+": x2_v + x3_v,
                  "-": x2_v - x3_v,
                  "*": x2_v * x3_v,
                  "/": x2_v / x3_v,
                  }.get(operator)
        return result
    else:
        return None


to_be_solved = [get_x1(eq) for eq in equations]

done = False
while not done:
    for eq in equations:
        x1 = get_x1(eq)
        if not known_values.get(x1):
            result = solve(eq=eq, known_values=known_values)
            if result:
                known_values[x1] = result
                to_be_solved = [x for x in to_be_solved if x != x1]
    if to_be_solved == []:
        done = True

pt1 = known_values.get("root")
print("Part 1:", pt1)


""" pt 2 """

def solve(eq: str, known_values: dict):
    x1 = eq[0:4]
    x2 = eq[6:10]
    x3 = eq[13:17]
    operator = eq[11]
    x1_v = known_values.get(x1)
    x2_v = known_values.get(x2)
    x3_v = known_values.get(x3)
    if x1_v is None and x2_v is not None and x3_v is not None:
        result = {"+": x2_v + x3_v,
                  "-": x2_v - x3_v,
                  "*": x2_v * x3_v,
                  "/": x2_v / x3_v,
                  }.get(operator)
        return x1, int(result)
    elif x3_v is None and x1_v is not None and x2_v is not None:
        result = {"+": x1_v - x2_v,  # x1 = x2 + x3
                  "-": x2_v - x1_v,  # x1 = x2 - x3
                  "*": x1_v / x2_v,  # x1 = x2 * x3
                  "/": x1_v * x2_v,  # x1 = x2 / x3
                  }.get(operator)
        return x3, int(result)
    elif x2_v is None and x1_v is not None and x3_v is not None:
        result = {"+": x1_v - x3_v,  # x1 = x2 + x3
                  "-": x1_v + x3_v,  # x1 = x2 - x3
                  "*": x1_v / x3_v,  # x1 = x2 * x3
                  "/": x1_v * x3_v,  # x1 = x2 / x3
                  }.get(operator)
        return x2, int(result)
    else:
        return None, None

equations, known_values = parse(data)
# adjust root equation:  root: bla + blub -> 0 = bla - blub
root_equation = [eq for eq in equations if get_x1(eq) == "root"][0]
non_root_equations = [eq for eq in equations if get_x1(eq) != "root"]
root_equation = root_equation.replace("+", "-")
equations = non_root_equations + [root_equation]
known_values["root"] = 0
known_values.pop("humn")

to_be_solved = equations.copy()

done = False
while not done:
    for eq in equations:
        var, result = solve(eq=eq, known_values=known_values)
        if result:
            known_values[var] = result
            to_be_solved = [x for x in to_be_solved if x != eq]
    if to_be_solved == []:
        done = True

pt2 = known_values["humn"]
print("Part 2:", pt2)
