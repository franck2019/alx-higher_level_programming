#!/usr/bin/python3
"""add_item module"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = 'add_item.json'

try:
    old_content = load_from_json_file(filename)
except Exception:
    old_content = []

args = sys.argv[1:]
old_content.extend(args)
save_to_json_file(old_content, filename)

"""
try:
    old_content = load_from_json_file(filename)
except Exception:
    save_to_json_file([], filename)
else:
    args = sys.argv[1:]
    old_content.extend(args)
    save_to_json_file(old_content, filename)
"""
"""
if len(sys.argv) <= 1:
    save_to_json_file([], filename)
else:
    args = sys.argv[1:]
    old_content = load_from_json_file(filename)
    old_content.extend(args)
    save_to_json_file(old_content, filename)

load_from_json_file(filename)
"""
