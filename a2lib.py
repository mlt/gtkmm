import os,re,sys,shutil
from os.path import join, getsize
from subprocess import Popen, PIPE
os.environ['PATH'] = os.environ['PATH'] + ";C:\\Program Files\\Microsoft Visual Studio 9.0\\Common7\\IDE\\;C:\\Program Files\\Microsoft Visual Studio 9.0\\VC\\bin\\;C:\\MinGW\\bin"
root = sys.path[0] + "\\usr\\i686-w64-mingw32\\sys-root\\mingw"

def gen(dll,lib,d):
    output = Popen(["nm", lib], stdout=PIPE).communicate()[0]
    with open(d, "wb") as f:
        f.write(b"EXPORTS\n")
        for line in output.split(b"\r\n"):
            if (re.match(b".* T _|.* I __nm", line)): #|.* I __imp
                line = re.sub(b"^.* T _|^.* I __nm__", b"", line) #|^.* I _
                # msvcrt.dll on windows misses secure versions of common CRT functions
                if not ("msvcrt.dll" == dll and line.endswith(b"_s")):
                    f.write(line + b"\n")
        f.write(str.encode("LIBRARY %s\n" % dll))

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
                gen(f, lib, d)
            Popen(["lib", "/def:%s" % d, "/name:%s" % f]).communicate()

gen("msvcrt.dll", "libmsvcrt.a", "libmsvcrt.def")
Popen(["lib", "/def:libmsvcrt.def"]).communicate()
