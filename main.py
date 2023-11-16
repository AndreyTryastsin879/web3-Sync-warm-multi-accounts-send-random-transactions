from functions import main_function_make_random_or_self_txns, export_report
from config import TXT_WITH_PRIVATE_KEYS


def main():
    with open(TXT_WITH_PRIVATE_KEYS) as file:
        list_of_private_keys = [line.strip() for line in file.readlines()]

    for private_key in list_of_private_keys:
        main_function_make_random_or_self_txns(private_key)

    export_report()


if __name__ == '__main__':
    main()
