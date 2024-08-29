import os
import shutil
import argparse


def extract_paths_with_extensions(folder_path):
    all_files = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            all_files.append((
                os.path.join(root, file),
                os.path.splitext(file)[1][1:]
            ))
    return all_files


def create_extension_tree(extensions, files, output_folder):
    try:
        for extension in extensions:
            ext_folder_path = f'{output_folder}/{extension if extension else "blank"}'
            os.makedirs(ext_folder_path)
            ext_paths = [path for path, _ in list(filter(lambda file: file[1] == extension, files))]
            for path in ext_paths:
                shutil.copy(path, ext_folder_path)
    except FileExistsError:
        print('Output folder of given name already exists.')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source', type=str, required=True, help='Directory to sort')
    parser.add_argument('-o', '--output', type=str, required=False, help='Directory to which sorted files should be saved')
    args = parser.parse_args()

    files = extract_paths_with_extensions(folder_path=args.source)
    unique_extensions = set([extension for _, extension in files])

    create_extension_tree(
        extensions=unique_extensions,
        files=files,
        output_folder=args.output or 'output'
    )


if __name__ == "__main__":
    main()





