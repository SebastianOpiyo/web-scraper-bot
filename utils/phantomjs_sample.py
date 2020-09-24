from phantomjs import Phantom

phantom = Phantom()


def main():
    print(dir(phantom.__ge__))


if __name__ == '__main__':
    main()
