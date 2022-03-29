import argparse
import os.path

processed_imports = []
out_header = ""
out_source = ""


def parse_args():
    parser = argparse.ArgumentParser(description="Merge cpp project directory in one file (that could be copy-pasted "
                                                 "in CodingGame IDLE)")
    parser.add_argument("-i", "--input", default="./cg.cpp", help="Relative path to the file to start merge with")
    parser.add_argument("-o", "--output", default="cg_out.cpp", help="Name of output file")
    # parser.add_argument("directory", help="Path to the root directory")
    return parser.parse_args()


def process_file(file_path):
    if file_path in processed_imports:
        return ""

    file_ext = os.path.splitext(file_path)[1]
    # if file_ext == ".cpp":
    print(f"Processing {file_path}")
    base_path, base_name = os.path.split(file_path)
    cur_header = f"/////////     File: {base_name}     /////////\n"
    processed_imports.append(file_path)

    with open(file_path, "r") as opened_file:
        content = opened_file.read()
        # if "#pragma once" in content:
        #     processed_imports.append(file_path)
        for line in content.splitlines():
            if "#pragma once" in line:
                processed_imports.append(file_path)
            elif "#include \"" in line:
                included = os.path.normpath(os.path.join(base_path, line.split("\"")[1]))
                cur_header += process_file(included)
            else:
                cur_header += line + "\n"

    cur_header += f"/////////     End: {base_name}     /////////\n\n"
    return cur_header


def process_dir(dir_path, main_file):
    content = ""
    nodes = os.listdir(dir_path)
    for node in nodes:
        cur_path = os.path.join(dir_path, node)
        if os.path.isdir(cur_path):
            content += process_dir(cur_path, main_file)
        elif os.path.isfile(cur_path) and cur_path != main_file:
            content += process_file(cur_path)
    return content


def main():
    process_once = []
    args = parse_args()
    working_dir, inp_name = os.path.split(args.input)
    out_name = args.output
    result_file = os.path.join(working_dir, out_name)
    if os.path.isfile(result_file):
        os.remove(result_file)
    content = process_file(args.input)
    content += process_dir(working_dir, args.input)
    with open(os.path.join(working_dir, out_name), "w") as out_file:
        out_file.write(content)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
