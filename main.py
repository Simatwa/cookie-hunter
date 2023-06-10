#!/usr/bin/python3
from json import loads, load, dumps
from sys import argv, exit


def error_handler(exit_on_error=True):
    def decorator(func):
        def main(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Error : {e.args[1] if len(e.args)>1 else e}")
                if exit_on_error:
                    exit("Quitting")

        return main

    return decorator


@error_handler()
def get_raw_data(resp: dict = {}) -> dict:
    with open(args.file, encoding="utf-8") as fh:
        data = fh.read()
    sorted = f'{{"cookies":{data} }}'
    for entry in loads(sorted).get("cookies"):
        resp.update({entry["name"]: entry["value"]})
    return resp


@error_handler()
def get_key(key: str) -> str:
    predefined = {
        "bard": "__Secure-1PSID",
        "bing": "_U",
    }
    if args.pre:
        with open(args.pre, encoding="utf-8") as fh:
            predefined.update(load(fh))
    return predefined.get(key, key)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Hunt cookies from `Json-to-Cookies` extension .json files",
        exit_on_error=True,
    )
    parser.add_argument("file", help="Path to .json file", metavar="FILE-PATH")
    parser.add_argument(
        "-i",
        "--indent",
        help="Indent level  while dumping json data - %(default)s",
        metavar="n",
        type=int,
        default=7,
    )
    parser.add_argument(
        "-g", "--get", help="Stdout the specific cookie value of the key", metavar="KEY"
    )
    parser.add_argument(
        "-p", "--pre", help="Path to .json file containing key-mappings", metavar="PATH"
    )
    parser.add_argument(
        "--zero-mapping",
        action="store_true",
        help="Disable key mappings - %(default)s",
    )
    args = parser.parse_args()
    hunted = get_raw_data()
    if args.get:
        print(hunted.get(args.get if args.zero_mapping else get_key(args.get)))
    else:
        print(dumps(hunted, indent=args.indent))

    # Dated Mon, 29 - May - 2023 1809hrs
