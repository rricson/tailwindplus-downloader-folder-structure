import json
import os
import sys
import html

def create_structure(data, base_path=""):
    if not isinstance(data, dict):
        return

    for key, value in data.items():
        if key == "snippets":
            write_snippets(value, base_path)
        elif isinstance(value, dict):
            new_path = os.path.join(base_path, key)
            os.makedirs(new_path, exist_ok=True)
            create_structure(value, new_path)

def write_snippets(snippets, base_path):
    component_name = os.path.basename(base_path.rstrip(os.sep))

    for snippet in snippets:
        version_path = os.path.join(base_path, "v" + str(snippet.get("version")))
        os.makedirs(version_path, exist_ok=True)

        extension = snippet.get("name")
        mode = snippet.get("mode") or "default"
        filename = f"{component_name}.{mode}.{extension}"
        filepath = os.path.join(version_path, filename)
        decoded_code = html.unescape(snippet.get("code", ""))

        write_file(filepath, decoded_code)

def write_file(filepath, content):
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(content)

def main(json_file_path):
    with open(json_file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    create_structure(data)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python structure.py <json_file_path>")
    else:
        main(sys.argv[1])