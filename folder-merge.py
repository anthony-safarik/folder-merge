#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 08:01:41 2020

@author: anthonysafarik
"""

import os
import shutil

#recursively merge two folders including subfolders
def folder_merge(root_src_dir, root_dst_dir):
    for src_dir, dirs, files in os.walk(root_src_dir):
        dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        for fname in files:
            src_file = os.path.join(src_dir, fname)
            dst_file = os.path.join(dst_dir, fname)
            print(src_file)
            print(dst_file)
            if os.path.exists(dst_file):
                print('EXISTS')
            else:
                shutil.move(src_file, dst_dir)

user_src = input('input the source path: ')
user_dst = input('input the destination path: ')

folder_merge(user_src,user_dst)
