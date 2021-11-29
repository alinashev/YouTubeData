from Action.Router import Router


def main():
    router = Router(2)
    router.generate_menu()
    router.selection_version()


if __name__ == '__main__':
    main()
