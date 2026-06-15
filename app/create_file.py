import os
import sys
from datetime import datetime

d_index = sys.argv.index("-d") if "-d" in sys.argv else None
f_index = sys.argv.index("-f") if "-f" in sys.argv else None

dir_path = ""
file_name = ""

if d_index is not None:
    end_index = f_index \
        if (f_index is not None and f_index > d_index) \
        else len(sys.argv)
    list_dir = sys.argv[d_index + 1:end_index]

    if list_dir:
        dir_path = os.path.join(*list_dir)
        os.makedirs(dir_path, exist_ok=True)

if f_index is not None and f_index + 1 < len(sys.argv):
    file_name = sys.argv[f_index + 1]

if file_name:
    file_path = os.path.join(dir_path, file_name)

    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    output_text = timestamp + "\n"
    for i, line in enumerate(lines, 1):
        output_text += f"{i} {line}\n"

    with open(file_path, "a", encoding="utf-8") as f:
        f.write(output_text)
else:
    print("Error: Please specify a file name using -f flag.")
