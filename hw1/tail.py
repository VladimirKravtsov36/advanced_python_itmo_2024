import sys
import fileinput


def tail_from_files(files):
    if len(files) == 1:
        tail_one_file(files[0])
    elif len(files) > 1:
        for file in files:
            print(f"==> {file} <==")
            tail_one_file(file)


def tail_one_file(file):
    with open(file, "r") as f:
        lines = f.readlines()
        print("".join(lines[-10:]))


def tail_from_stdin():
    stdin_lines = []
    try:
        for line in fileinput.input():
            stdin_lines.append(line)
    except KeyboardInterrupt:
        print("".join(stdin_lines[-17:]))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        tail_from_files(sys.argv[1:])
    elif len(sys.argv) == 1:
        tail_from_stdin()
