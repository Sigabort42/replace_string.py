#!/usr/bin/env python3

import re
import os
import glob
import argparse


PARSER = argparse.ArgumentParser(
    prog="replace_string.py",
    description="Cherche dans chaque fichier de l'arborescence une string et la remplace",
    epilog="Cherche dans chaque fichier de l'arborescence une string et la remplace"
)
PARSER.add_argument(
    "-d",
    default="./",
    help="path of directory",
    metavar=""
)
PARSER.add_argument(
    "-s",
    default="",
    help="string source",
    metavar=""
)
PARSER.add_argument(
    "-n",
    default="",
    help="new string",
    metavar=""
)
PARSER.add_argument(
    "-r",
    default="",
    help="Passing regex localize source string",
    metavar=""
)

def listdirectory(path): 
    files=[] 
    l = glob.glob(path+'/*') 
    for i in l: 
        if os.path.isdir(i): files.extend(listdirectory(i)) 
        else: files.append(i)
    return files

def     call_regex(src, dst, reg):
    re_s = re.compile(reg)
    res = re_s.sub(dst, src)
    return (res)

          
def     main(doss="./", src="", dst="", reg=""):
    files = listdirectory(doss)
    for f in files:
        print("files is working is: ", f, "\033[32;5m[Ok]\033[0m")
        with open(f, "r") as fdr:
            content = fdr.read()
            fdr.close()
            if (reg != ""):
                res = call_regex(content, dst, reg)
            else:
                res = content.replace(src, dst)
            with open(f, "w") as fdw:
                fdw.write(res)
                fdw.close()

if __name__ == "__main__":
    doss = os.path.abspath(PARSER.parse_args().d)
    src = PARSER.parse_args().s
    dst = PARSER.parse_args().n
    reg = PARSER.parse_args().r
    main(doss, src, dst, reg)
