import os
import argparse
from utils import is_pdf, is_match, init_container

parser = argparse.ArgumentParser(description="Check a directory if a PDF file is reapeted")
parser.add_argument("--path", type=str, default=".", help="Directory to clean")

args = parser.parse_args()
path = args.path

print(f"Checking {path}")

# get all the documents from given directory
content = os.listdir(path)

# create a relative path from the file and the document
path_content = [os.path.join(path, doc) for doc in content]

# filter our directory content into a documents and folders list
docs = [init_container(doc) for doc in path_content if is_pdf(doc)]

# go through all files
for doc in docs:
    print(f"> Looking for {doc.name}")
    matches = [file for file in docs if is_match(doc, file)]
    if len(matches) == 0:
        print("Not matches")
        continue
    for match in matches:
        print(f"\t- {match.name}")
