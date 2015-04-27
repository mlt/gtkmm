#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Convert .a to .lib by generating a list of exported functions from
DLL into .def file and generating import library based on that .def
file. Run this tool from VS command prompt."""

import argparse
import os,re,sys,shutil
from os.path import join, getsize
from subprocess import Popen, PIPE

def gen(dll,lib,d):
    output = Popen(["dumpbin", "-exports", dll], stdout=PIPE).communicate()[0]
    with open(d, "wb") as f:
        f.write(b"EXPORTS\n")
        lines = output.splitlines()
        for line in lines[19:]:
            if line != "" and line[0] == " ":
                cols = line.split()
                if len(cols)==4 and cols[0].isdigit():
                    # msvcrt.dll on windows misses secure versions of common CRT functions
                    if not ("msvcrt.dll" == dll and cols[3].endswith(b"_s")):
                        f.write(cols[3] + b"\n")
        f.write(str.encode("LIBRARY %s\n" % dll))

def walk(root):
    os.chdir(root + "\\lib")
    for root, dirs, files in os.walk(root + "\\bin"):
        for f in files:
            if (re.search(".dll", f)):
                name = re.sub("^lib", "", f)
                name = re.sub("\\.dll$", "", name)
                name = re.sub("(?:-\\d+)$", "", name)
                d = "%s.def" % name
                if not os.path.exists(d):
                    print("Working on %s to produce %s\n" % (f, d))
                    lib = "lib%s.dll.a" % name
                    gen(join(root, f), lib, d)
                Popen(["lib", "/def:%s" % d, "/name:%s" % f]).communicate()

def get_parser():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--root',
                        default="C:/msys32/mingw32",
                        help='Root directory for MINGW. The one that has /bin and /lib.')
    return parser


if __name__ == '__main__':
    p = get_parser()
    args = p.parse_args()
    walk(args.root)
