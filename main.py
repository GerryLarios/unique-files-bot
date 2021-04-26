import os
import argparse
from utils import is_match, init_container

parser = argparse.ArgumentParser(description="Check a directory if a PDF file is reapeted")
parser.add_argument("--path", type=str, default=".", help="Directory to clean")
parser.add_argument("--output", type=str, default="duplicated", help="Directory to storage the duplicated items")

args = parser.parse_args()
path = args.path
output = args.output

print(f"Checking {path}")

# get all the documents from given directory
content = os.listdir(path)

# create a relative path from the file and the document
path_content = [os.path.join(path, doc) for doc in content]

# filter our directory content into a documents and folders list
docs = [init_container(doc) for doc in path_content if os.path.isfile(doc)]
folders = [folder for folder in path_content if os.path.isdir(folder)]

# creating copies folder
output_folder = os.path.join(path, output)
if not output_folder in folders:
    try:
        os.mkdir(output_folder)
    except FileExistsError as err:
        print(f"Folder already exists {output_folder}... {err}")

# moved files
checked_files = []
moved_files_counter = 0

# go through all files
for doc in docs:
    print(f"> Looking for {doc.name}")
    matches = [file for file in docs if is_match(doc, file) and file not in checked_files]
    checked_files.append(doc)
    if len(matches) == 0:
        print("Not matches")
        continue
    for match in matches:
        checked_files.append(match)
        new_doc_path = os.path.join(output_folder, match.name) + doc.filetype
        os.rename(doc.full_path, new_doc_path)
        moved_files_counter += 1
        print(f"\tMoved file {match.name} to {output}")

print(f"Moved {moved_files_counter} of {len(docs)} elements")
