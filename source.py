import parse
import output
import solver


def main() -> int:
    url_data = "https://raw.githubusercontent.com/thewhitesoft/student-2023-assignment/main/data.json"
    url_replace = "https://raw.githubusercontent.com/thewhitesoft/student-2023-assignment/main/replacement.json"

    data = parse.get_data(url_data)
    replaceItems = parse.get_data(url_replace)

    result = solver.replace_data(replaceItems, data)

    output.write_data2json(result)
    return 0


if __name__ == "__main__":
    main()
