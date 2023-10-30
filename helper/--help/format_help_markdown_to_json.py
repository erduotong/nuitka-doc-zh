import json
import re

with open("../../docs/--help.md", "r", encoding='utf-8') as f:
    help_text = f.read()
# 先遍历每一行 直到遇到一行的字符为'该文档目前Nuitka版本'开头 然后该行``内的内容为版本号
out_dict = {
    "version": "",
    "source": "",
}
for line in help_text.splitlines():
    if line.startswith("该文档目前Nuitka版本"):
        print("找到版本号")
        out_dict["version"] = line.split("`")[1]
        break

matches = re.findall(r'<details>.*?<summary>源文本</summary>\n\n```\n(.*?)\n```\n\n</details>', help_text, re.DOTALL)
if len(matches) == 0:
    raise RuntimeError("源文本似乎丢失了")
else:
    print("找到源文本")
    out_dict["source"] = matches[0]
# 一直去除help_text中的文本，直到遇到# Options为止
help_text = help_text[help_text.find("# Options"):]


def split_string(s):
    lines = s.split('\n')
    parts = []
    current_part = ''
    for linef in lines:
        if linef.startswith('## '):
            if current_part:
                parts.append(current_part)
            current_part = linef + '\n'
        else:
            current_part += linef + '\n'
    if current_part:
        parts.append(current_part)
    return parts


# 进行按照大分类的切割
after_split = split_string(help_text)
del split_string


def split_title_string(s):
    depth = 0
    start = 0
    for i, c in enumerate(s):
        if c == '(':
            if depth == 0:
                start = i
            depth += 1
        elif c == ')':
            depth -= 1
            if depth == 0:
                return s[:start], s[start + 1:i]
    return s, ''


# 将after_split中的第一个# 后面的内容(去除收尾空格)新建为一个键，值为一个空字典 并且保存到一个值中
options_key = after_split[0][1:].strip()
# 拆分这个字符串，提取它碰到的第一个最外层的括号中的内容以及括号外的内容
# 例如basic(基本设置(无分类)) => basic, 基本设置(无分类)

out, inside = split_title_string(options_key)
out_dict[out] = {
    "chinese": inside,
    "content": {

    }
}
# after_split = after_split[1:]  # 第一个Options是无用的
# print(after_split)
# print(json.dumps(out_dict, indent=4, ensure_ascii=False))
# with open("./output.json", "w", encoding='utf-8') as f:
#     f.write(json.dumps(out_dict, indent=4, ensure_ascii=False))
