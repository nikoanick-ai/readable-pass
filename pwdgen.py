"""readable-pass: 生成不含易混淆字符的随机密码。

单文件、零依赖，基于标准库 secrets 提供密码学安全的随机性。
"""

import argparse
import secrets
import string
import sys

# 视觉易混淆字符
AMBIGUOUS = set("0O1lI")

UPPER = "".join(c for c in string.ascii_uppercase if c not in AMBIGUOUS)
LOWER = "".join(c for c in string.ascii_lowercase if c not in AMBIGUOUS)
DIGITS = "".join(c for c in string.digits if c not in AMBIGUOUS)
SYMBOLS = "!@#$%^&*-_=+?"


def generate(length: int = 16, symbols: bool = True) -> str:
    """生成随机密码；保证至少含一位大写、一位小写、一位数字。"""
    if length < 4:
        raise ValueError("length must be >= 4")
    mandatory = [
        secrets.choice(UPPER),
        secrets.choice(LOWER),
        secrets.choice(DIGITS),
    ]
    if symbols:
        mandatory.append(secrets.choice(SYMBOLS))
    pool = UPPER + LOWER + DIGITS + (SYMBOLS if symbols else "")
    chars = mandatory + [secrets.choice(pool) for _ in range(length - len(mandatory))]
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        prog="readable-pass",
        description="生成不含易混淆字符（0/O、1/l/I 等）的随机密码",
    )
    parser.add_argument("-l", "--length", type=int, default=16, help="密码长度（默认 16）")
    parser.add_argument("-n", "--count", type=int, default=1, help="生成数量（默认 1）")
    parser.add_argument("--no-symbols", action="store_true", help="不含符号")
    args = parser.parse_args(argv)
    try:
        for _ in range(args.count):
            print(generate(args.length, not args.no_symbols))
    except ValueError as err:
        print(f"Error: {err}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
