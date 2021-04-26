import os
import re
from collections import namedtuple

Container = namedtuple("Container", ["name", "size", "path", "full_path", "filetype"])

def init_container(doc):
    path, filetype = os.path.splitext(doc)
    name = os.path.basename(path)
    size = os.path.getsize(doc)
    return Container(name, size, path, doc, filetype)

def is_pdf(filetype):
    return re.search(r'pdf|PDF', filetype)

def is_match(base_doc, current_doc):
    return current_doc.size == base_doc.size and current_doc.name is not base_doc.name 
