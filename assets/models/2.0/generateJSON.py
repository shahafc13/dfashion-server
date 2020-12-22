import json
import os
import shutil

list_dir = r"C:\Users\shahaf\Downloads\clothing"


def generate_index():
    index = [{
        "name": "shoes",
        "variants": {
            "glTF-Binary": "shoes.glb"
        }
    },
        {
        "name": "bag",
        "variants": {
            "glTF-Binary": "test.glb"
        }
    },
        {
        "name": "blackSuit",
        "variants": {
            "glTF-Binary": "black_suit.glb"
        }
    }]
    for root, dirs, files in os.walk(list_dir):
        for file in files:
            try:
                if file.endswith(".glb"):
                    name = file[:-4]
                    path = os.path.join(root, file)
                    os.makedirs(f"{name}\\glTF-Binary")
                    shutil.copy(path, f"{name}\\glTF-Binary")
                    file_index = {
                        "name": name,
                        "variants": {
                            "glTF-Binary": file
                        }
                    }
                    index.append(file_index)
            except Exception:
                print(root, file)
    print(index)
    with open("model-index.json", "w") as write_stream:
        write_stream.write(json.dumps(index))


generate_index()
