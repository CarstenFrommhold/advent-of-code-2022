import utils
import time

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
solved = []

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

## Pt 2 - Idea (not efficient loop, works for sample data but is not the correct approach for large data)


def extract_root_eq(equations: list) -> str:
    for eq in equations:
        if "root" in eq:
            return eq


def solve_root_eq(eq: str, known_values: dict) -> bool:
    x2 = eq[6:10]
    x3 = eq[13:17]
    x2_v = known_values.get(x2)
    x3_v = known_values.get(x3)
    if x2_v and x3_v:
        return x2_v == x3_v
    else:
        raise Exception("x2 and x3 not found!")


equations, known_values = parse(data)
root_eq = extract_root_eq(equations)

to_be_solved = [get_x1(eq) for eq in equations if get_x1(eq) != "root"]

solution = None

for try_ in range(999, 10000):

    if not solution:

        print(f"Try with {try_}")
        start = time.time()

        to_be_solved = [get_x1(eq) for eq in equations if get_x1(eq) != "root"]

        known_values_ = known_values.copy()
        known_values_["humn"] = try_

        done = False
        while not done:
            for eq in equations:
                x1 = get_x1(eq)
                if not known_values_.get(x1):
                    result = solve(eq=eq, known_values=known_values_)
                    if result:
                        known_values_[x1] = result
                        to_be_solved = [x for x in to_be_solved if x != x1]
            if to_be_solved == []:
                done = True
            if time.time() - start > 5:
                print("Longer than 5 sec")
                break
        try:
            root_eq_result = solve_root_eq(root_eq, known_values=known_values_)
            if root_eq_result:
                print("Hooray!")
                print(try_)
                solution = try_
        except Exception as e:
            print("too long")


pt2 = solution
print("Part 2:", pt2)
