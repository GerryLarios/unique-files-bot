import os
import argparse
from utils import isPDF
from collections import namedtuple

parser = argparse.ArgumentParser(description="Check a directory if a PDF file is reapeted")
parser.add_argument("--path", type=str, default=".", help="Directory to clean")

args = parser.parse_args()
path = args.path

print(f"Checking {path}")

# create the namedtuple
Container = namedtuple('Container', ['name', 'size'])

# get all the documents from given directory
content = os.listdir(path)

# create a relative path from the file and the document
path_content = [os.path.join(path, doc) for doc in content]

# filter our directory content into a documents and folders list
docs = [doc for doc in path_content if os.path.isfile(doc) and isPDF(doc)]

# go through all files and get the size.
for doc in docs:
    full_doc_path, filetype = os.path.splitext(doc)
    doc_name = os.path.basename(full_doc_path)
    current_file = Container(doc_name, os.path.getsize(doc))
    print(f"{current_file.name} - {current_file.size}BYTES")
