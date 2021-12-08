import sys

from Action.Router import Router
from Commons.CLParser import CLParser


def main():
    parser = CLParser()
    version = parser.createParser().parse_args(sys.argv[1:])

    router = Router(int(version.v))
    router.generate_menu()
    router.selection_version()


if __name__ == '__main__':
    main()