# CMake files for native GTKMM 3 build with MS VC++ on Win32 platform

## Why

Native GTKMM builds for Win32 with MS VC++ lag behind those with gcc.

## How

* <del>[Use OBS](http://mail.gnome.org/archives/gtk-list/2011-March/msg00111.html) (openSUSE Build Service)</del> [Fedora-mingw binaries](http://build1.openftd.org/fedora-cross/i386/RPMS_noarch/) for all prerequisites
 + [Nice script by Maarten Bosmans](http://www.bosmans.ch/pulseaudio/download-mingw-rpm.py) downloads everything: \Python32\python download-mingw-rpm.py --no-clean --deps libxml2 libxml2-devel atk atk-devel libcairo2 libcairo-gobject2 cairo-devel pango pango-devel gstreamer gstreamer-devel gdk-pixbuf gdk-pixbuf-devel
* You'll need perl to build gtk+ git submodule
* It is complicated to build MM counterpart from git on Win32 as they heavily use m4 macro processor
* <del>Download source code release for corresponding subfolders</del>

## Problems

* There may be glitches with path names
* Some stuff from OBS may be broken

## Notes

Windows XP doesn't have mklink tool.
ln tool from http://schinagl.priv.at/nt/ln/ln.html should be used as fsutil requires elevated privileges.

## Status

Builds with

    [libsigc++-2.2.10](http://ftp.gnome.org/pub/GNOME/sources/libsigc++/2.2)
    [glibmm-2.29.13](http://ftp.gnome.org/pub/GNOME/sources/glibmm/2.29)
    [atkmm-2.22.5](http://ftp.gnome.org/pub/GNOME/sources/atkmm/2.22)
    [cairomm-1.10.0](http://cairographics.org/releases)
    [pangomm-2.28.2](http://ftp.gnome.org/pub/gnome/sources/pangomm/2.28)
    [gtkmm-3.1.18](http://ftp.gnome.org/pub/GNOME/sources/gtkmm/3.1)
    [libxml++-2.34.2](http://ftp.gnome.org/pub/GNOME/sources/libxml++/2.34)
    [gstreamermm-0.10.10](http://ftp.gnome.org/pub/GNOME/sources/gstreamermm/0.10)
    GTK+ (See git submodule SHA)

## TODO

* Consider using ExternalProject CMake module
