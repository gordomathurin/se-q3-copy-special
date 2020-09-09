#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "Gordon Mathurin, with help from JT"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    # your code here
    special_paths = []
    for dirpath, _, filenames in os.walk(os.path.abspath(dirname)):
        for f in filenames:
            file_match_regex = re.findall(r'__\w+__', f)
            if file_match_regex:
                special_paths.append(os.path.join(dirpath, f))
        break
    return special_paths


def create_dir(path):
    """ Checks if directory exists, if not create it """
    if not os.path.isdir(path):
        try:
            os.makedirs(path)
        except OSError:
            print(f'Creation of dir {path} failed')
            return False
    return True


def copy_to(path_list, dest_dir):
    # your code here
    """ Copy files to a given directory """
    create_dir_status = create_dir(dest_dir)
    if not create_dir_status:
        return

    for f in path_list:
        shutil.copyfile(f, os.path.join(dest_dir, os.path.basename(f)))


def zip_to(path_list, dest_zip):
    # your code here
    """ Given a list of paths, zip files to given zip dir """
    cmd = ['zip', '-j', dest_zip]
    cmd.extend(path_list)
    print(" ".join(cmd))
    subprocess.call(cmd)


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    parser.add_argument(
        'from_dir', help='directory to grab specail files from')
    ns = parser.parse_args(args)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions
    path_list = get_special_paths(ns.from_dir)

    for path in path_list:
        print(path)

    if ns.todir:
        copy_to(path_list, ns.todir)

    if ns.tozip:
        zip_to(path_list, ns.tozip)


if __name__ == "__main__":
    main(sys.argv[1:])
