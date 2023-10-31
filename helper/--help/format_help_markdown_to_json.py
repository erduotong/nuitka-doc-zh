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


def extract_info(section_lines):
    original_param_name = ""
    chinese_param_name = ""
    original_intro = ""
    chinese_intro = ""

    for i in range(len(section_lines)):
        if section_lines[i] == '原始参数名:':
            j = i + 1
            while '```' not in section_lines[j]:
                j += 1
            j += 1
            while '```' not in section_lines[j]:
                original_param_name += section_lines[j] + "\n"
                j += 1
        elif section_lines[i] == '中文参数名:':
            j = i + 1
            while '```' not in section_lines[j]:
                j += 1
            j += 1
            while '```' not in section_lines[j]:
                chinese_param_name += section_lines[j] + "\n"
                j += 1
        elif section_lines[i] == '原始简介:':
            j = i + 1
            while '```' not in section_lines[j]:
                j += 1
            j += 1
            while '```' not in section_lines[j]:
                original_intro += section_lines[j] + "\n"
                j += 1
        elif section_lines[i] == '中文简介:':
            j = i + 1
            while '```' not in section_lines[j]:
                j += 1
            j += 1
            while '```' not in section_lines[j]:
                chinese_intro += section_lines[j] + "\n"
                j += 1

    return original_param_name.strip(), chinese_param_name.strip(), original_intro.strip(), chinese_intro.strip()


def reformat_english(text):
    return text


def reformat_chinese(text):
    return text


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
after_split = after_split[1:]  # 第一个Options是无用的
tot = 0
for i in after_split:
    """
    先对##的内容进行拆分
    然后再对###的命令进行拆分
    最后再筛选中文参数名,原始参数名,原始简介,中文简介啥的
    """
    # 得到第一行的内容
    lines = i.split('\n')
    first_line = lines.pop(0).strip()
    # 去除第一行开头的#直到第一个空格
    first_lines = first_line[first_line.find(' ') + 1:]
    del first_line
    sec_key, sec_chinese = split_title_string(first_lines)
    to_dict = {
        "chinese": sec_chinese,
        "content": {

        }
    }
    # 解析每一行内容并且输出出去
    lines = '\n'.join(lines)
    sections = re.split(r'\n###', lines)
    for section in sections:
        # 读取第一行
        section_lines = section.split('\n')
        key_third = section_lines.pop(0).strip()  # 最终内容的key
        if len(key_third) == 0:
            continue
        in_to_dict = {
            "raw_parameter": "",
            "chinese_parameter": "",
            "raw_introduction": "",
            "chinese_introduction": "",
        }
        # 解析其中内容
        raw_parameter, chinese_parameter, raw_introduction, chinese_introduction = extract_info(section_lines)
        tot += 1
        in_to_dict["raw_parameter"] = reformat_english(raw_parameter)
        in_to_dict["chinese_parameter"] = reformat_chinese(chinese_parameter)
        in_to_dict["raw_introduction"] = reformat_english(raw_introduction)
        in_to_dict["chinese_introduction"] = reformat_chinese(chinese_introduction)
        to_dict["content"][key_third] = in_to_dict

    out_dict[out]["content"][sec_key.strip()] = to_dict


with open("./output.json", "w", encoding='utf-8') as f:
    f.write(json.dumps(out_dict, indent=4, ensure_ascii=False))
print(f"处理完成，请检查output.json\n共{tot}个参数被识别")
