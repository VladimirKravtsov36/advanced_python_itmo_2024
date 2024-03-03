import sys
import fileinput


def nl_from_file(filename):
    with open(filename, "r") as f:
        for line_counter, line in enumerate(f.readlines(), start=1):
            print(line_counter, line, end="")


def nl_from_stdin():
    try:
        for line_counter, line in enumerate(fileinput.input(), start=1):
            print(line_counter, line)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    if len(sys.argv) == 2:
        nl_from_file(sys.argv[1])
    elif len(sys.argv) == 1:
        nl_from_stdin()
    else:
        print("Wrong arguments!")
