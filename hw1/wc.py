import sys
import fileinput


def count_lines_words_bytes(file_lines):
    lines = 0
    words = 0
    bytes_count = 0

    for line in file_lines:
        lines += 1
        words += len(line.split())
        bytes_count += len(line.encode("utf-8"))

    return lines, words, bytes_count


def wc_from_files(files):
    if len(files) == 1:
        with open(files[0], "r") as f:
            lines, words, bytes_count = count_lines_words_bytes((f.readlines()))
            print(lines, words, bytes_count, files[0], sep="\t")
    elif len(files) > 1:
        total_lines = 0
        total_words = 0
        total_bytes = 0
        for file in files:
            with open(file, "r") as f:
                lines, words, bytes_count = count_lines_words_bytes(f.readlines())
                total_lines += lines
                total_words += words
                total_bytes += bytes_count
                print(lines, words, bytes_count, file, sep="\t")
        print(total_lines, total_words, total_bytes, "total", sep="\t")


def wc_from_stdin():
    stdin_lines = []
    try:
        for line in fileinput.input():
            stdin_lines.append(line)
    except KeyboardInterrupt:
        lines, words, bytes_count = count_lines_words_bytes(stdin_lines)
        print(lines, words, bytes_count, sep="\t")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        wc_from_files(sys.argv[1:])
    elif len(sys.argv) == 1:
        wc_from_stdin()
