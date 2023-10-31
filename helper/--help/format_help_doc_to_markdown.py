# 首先删除第一行的Options

with open('./input.in', 'r', encoding='utf-8') as f:
    input_str = f.read()
    input_str = input_str.strip()
Options = {
    "basic": {

    }
}
# 删除前后空行

# 删除第一行
input_str = input_str.split('\n', 1)[1]
key = ''
lines = input_str.split('\n')
# 遍历每一行
i = 0
now_key = ''
while i < len(lines):
    # 如果line空两格有--
    if lines[i].startswith('  --'):
        # 读取--后面的内容(例如--help)直到遇到的第一个空格并且将其作为key 然后保存它后面的所有字符到value(如果后面没有字符就设置为一个空格
        key = "--" + lines[i].split('--', 1)[1].split(' ', 1)[0]
        value = lines[i].split('--', 1)[1].split(' ', 1)[1] if len(lines[i].split('--', 1)[1].split(' ', 1)) > 1 else ""

        # 一直都去下一行 直到下一行读取前10个字符的时候遇到了--(例如  --help)或者遇到了空行
        i += 1
        while i < len(lines) and '--' not in lines[i][:10] and lines[i] != '':
            value += f" {lines[i].strip()}"
            i += 1
        Options["basic"][key] = value
        # 清除两端空格
        Options["basic"][key] = Options["basic"][key].strip()
        continue

    # 如果这一行是只有空格的行
    elif lines[i].strip() == '':
        i += 1
        now_key = lines[i]
        # 删除now_key的两端空格和:
        now_key = now_key.strip().strip(':')
        Options[now_key] = {}
        i += 1
        continue
    elif '--' in lines[i][:10]:
        start = lines[i].find('--')
        # 找到'--'后的第一个空格的位置
        end = lines[i].find(' ', start)

        # 如果没有找到空格，说明这一行只有key，没有value
        if end == -1:
            key = lines[i][start:].strip()
            value = ''
        else:
            # 否则，将'--'和空格之间的内容作为key，空格后的内容作为value
            key = lines[i][start:end].strip()
            value = lines[i][end:].strip()
        i += 1
        while i < len(lines) and '--' not in lines[i][:10] and lines[i] != '':
            value += f" {lines[i].strip()}"
            i += 1
        Options[now_key][key] = value
        Options[now_key][key] = Options[now_key][key].strip()
        continue

max_line_len = 80
tot = 0
# 生成markdown
output_str = "# Options()\n"
for key, value in Options.items():
    output_str += f"## {key}()\n"
    for key2, value2 in value.items():
        tot += 1
        # 如果一行的长度超过了max_line_len，就在空格处换行
        words = value2.split(' ')
        lines = []
        current_line = ''
        for word in words:
            if len(current_line + ' ' + word) <= max_line_len:
                current_line += ' ' + word
            else:
                lines.append(current_line)
                current_line = word
        lines.append(current_line)
        value2 = '\n'.join(lines)
        # 去除value2的两端空格
        value2 = value2.strip()
        output_str += "\n---\n"
        output_str += f"### {key2}\n"
        output_str += f"""
原始参数名:
```
{key2}
```
中文参数名:
```

```
原始简介:
```
{value2}
```
中文简介:
```

```
"""
output_str += f"\n---\n"
output_str += f"\n---\n"

with open('./output.md', 'w', encoding='utf-8') as f:
    f.write(output_str)
print("complete\nplease check output.md")
print(tot)