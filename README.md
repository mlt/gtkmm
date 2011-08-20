# CMake files for native GTKMM 3 build with MS VC++ on Win32 platform

## Why

Native GTKMM builds for Win32 with MS VC++ lag behind those with gcc.

## How

* [Use OBS](http://mail.gnome.org/archives/gtk-list/2011-March/msg00111.html) (openSUSE Build Service) for all prerequisites
* You'll need perl to build gtk+ git submodule
* It is complicated to build MM counterpart from git on Win32 as they heavily use m4 macro processor
* <del>Download source code release for corresponding subfolders</del>


http://www.bosmans.ch/pulseaudio/download-mingw-rpm.py

\Python32\python download-mingw-rpm.py --no-clean --deps libxml2 libxml2-devel atk atk-devel libcairo2 libcairo-gobject2 cairo-devel pango pango-devel gstreamer gstreamer-devel gdk-pixbuf gdk-pixbuf-devel

C:\obs\usr\i686-w64-mingw32\sys-root\mingw\bin>\workspace\gtkmm.build\glibmm-2.28.2\MSVC_Net2008\gendef\gendef.exe glib-2.0.def libglib-2.0-0.dll libglib-2.0-0.dll

lib /def:glib-2.0.def

## Problems

* There may be glitches with path names
* Some stuff from OBS may be broken

## Notes

Windows XP doesn't have mklink tool.
ln tool from http://schinagl.priv.at/nt/ln/ln.html should be used as fsutil requires elevated privileges.

## Status

Builds with

    libsigc++-2.2.10
    glibmm-2.28.2
    atkmm-2.22.5
    cairomm-1.10.0
    pangomm-2.28.2
    gtkmm-3.1.8
    
