import json
import re

with open("../../docs/--help.md", "r", encoding='utf-8') as f:
    help_text = f.read()
# 先遍历每一行 直到遇到一行的字符为'该文档目前Nuitka版本'开头 然后该行``内的内容为版本号
out_dict = {
    "version": "",
}
print("寻找版本号")
for line in help_text.splitlines():
    if line.startswith("该文档目前Nuitka版本"):
        print("找到版本号")
        out_dict["version"] = line.split("`")[1]
        break



print(json.dumps(out_dict, indent=4, ensure_ascii=False))
# with open("./output.json", "w", encoding='utf-8') as f:
#     f.write(json.dumps(out_dict, indent=4, ensure_ascii=False))
