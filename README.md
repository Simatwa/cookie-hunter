# cookie-hunter

>Sort cookies exported by `Cookies-to-Json` extension.

## Installation

1. Install [addtopath](https://github.com/Simatwa/addtopath)
2. Execute `addtopath main.py ch`

## Usage
- Export cookies with `Cookies-to-Json` Chrome Extension.
- `$ ch <path-to-the.json-file-exported>`

<details>

<summary>

* For more info you can run `$ ch -h`

</summary>

```
usage: main.py [-h] [-i n] [-g KEY] [-p PATH]
               [--zero-mapping]
               FILE-PATH

Hunt cookies from `Json-to-Cookies` extension
.json files

positional arguments:
  FILE-PATH            Path to .json file

options:
  -h, --help           show this help message
                       and exit
  -i n, --indent n     Indent level while
                       dumping json data - 7
  -g KEY, --get KEY    Stdout the specific
                       cookie value of the key
  -p PATH, --pre PATH  Path to .json file
                       containing key-mappings
  --zero-mapping       Disable key mappings -
                       False
```
</details>
