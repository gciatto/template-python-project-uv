import sys

from main_package.greeting import greet


def main() -> None:
    print(greet(*sys.argv[1:2]))


if __name__ == "__main__":
    main()
