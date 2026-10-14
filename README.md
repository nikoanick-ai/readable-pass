# readable-pass

> 生成不含易混淆字符的随机密码 — Random passwords without ambiguous characters

单文件、零依赖。排除 `0/O`、`1/l/I` 等视觉易混淆字符，并保证至少含一位大写、一位小写、一位数字，适合需要抄写、口述、打印密码的场景。

[![CI](https://github.com/nikoanick-ai/readable-pass/actions/workflows/ci.yml/badge.svg)](https://github.com/nikoanick-ai/readable-pass/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)

## Quick Start

需要 Python 3.10+：

```bash
python pwdgen.py              # 一条 16 位密码
python pwdgen.py -l 20 -n 3   # 三条 20 位密码
python pwdgen.py --no-symbols # 不含符号
```

输出示例：

```
$ python pwdgen.py -n 2
rT7kxP2mQvJz9wAa
eF4bN8sHcLd3gYqM
```

## 核心功能

- 排除易混淆字符（0/O、1/l/I 等），手抄、转述零出错
- 使用标准库 `secrets`（密码学安全随机），而非 `random`
- 保证至少含一位大写、一位小写、一位数字
- 零依赖，单文件，复制 `pwdgen.py` 即可使用

## 设计取舍

为了「可读性」，字符池比常规生成器少 4 个字符，熵值略有牺牲——这是本项目的取舍，也是它存在的理由。

## Roadmap

- [ ] `-p` passphrase 模式（字典词组合）
- [ ] 密码强度估算输出

## License

[MIT](./LICENSE)
