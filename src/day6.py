from pathlib import Path

# test = "bvwbjplbgvbhsrlpgdmjqwftvncz"
# test = "nppdvjthqldpwncqszvftbrmjlhg"
# test = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprw"
# test = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"


def calc_engine(data, distinct):
    for ctr in range(distinct, len(data) - distinct):
        if len(set(data[ctr - distinct : ctr])) == distinct:
            return ctr
    print("No solution found")
    raise RuntimeError


if __name__ == "__main__":

    path = Path(__file__).parent / "input" / "input6.txt"
    with open(path, "r") as f:
        input_data = f.readline()

    print(calc_engine(input_data, 4))
    print(calc_engine(input_data, 14))
