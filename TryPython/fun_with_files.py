#!/opt/python3/bin/python3.5
# -*- coding: utf-8 -*-

import os

"""
for root, dirs, files, rootfd in os.fwalk('/home/marik/temp'):
    print(root, "consumes ", end="")
    print(sum([os.stat(name, dir_fd=rootfd).st_size for name in files]),
          end="")
    print("bytes in", len(files), "non-directory files")
    if 'CVS' in dirs:
        dirs.remove('CVS')  # don't visit CVS directories
"""

for root, dirs, files, rootfd in os.fwalk('/home/marik/temp'):
    print("Katalog:", root)
