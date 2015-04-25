# CMake files for native GTKMM 3 build with MS VC++ on Win32 platform

## Why

Native GTKMM builds for Win32 with MS VC++ lag behind those with gcc.

## How

* <del>[Use OBS](http://mail.gnome.org/archives/gtk-list/2011-March/msg00111.html) (openSUSE Build Service)</del> <del>[Fedora-mingw binaries](http://build1.openftd.org/fedora-cross/i386/RPMS_noarch/) for all prerequisites</del>
  Now msys2 `pacman -S mingw-w64-i686-gtk3 mingw-w64-i686-gstreamer mingw-w64-i686-gst-plugins-good`
 + <del>[Nice script by Maarten Bosmans](http://www.bosmans.ch/pulseaudio/download-mingw-rpm.py) downloads everything: \Python32\python download-mingw-rpm.py --no-clean --deps libxml2 libxml2-devel atk atk-devel libcairo2 libcairo-gobject2 cairo-devel pango pango-devel gstreamer gstreamer-devel gdk-pixbuf gdk-pixbuf-devel</del>
* <del>You'll need perl to build gtk+ git submodule</del>
* It is complicated to build MM counterpart from git on Win32 as they heavily use m4 macro processor
* <del>Download source code release for corresponding subfolders</del>

## Problems

* There may be glitches with path names
* Some stuff from OBS may be broken

## Notes

Windows XP doesn't have mklink tool and is not supported anymore.

## Status

Builds with

- [libsigc++-2.4.1](http://ftp.gnome.org/pub/GNOME/sources/libsigc++/2.4)
- [glibmm-2.44.0](http://ftp.gnome.org/pub/GNOME/sources/glibmm/2.44)
- [atkmm-2.22.7](http://ftp.gnome.org/pub/GNOME/sources/atkmm/2.22)
- [cairomm-1.11.2](http://cairographics.org/releases)
- [pangomm-2.36.0](http://ftp.gnome.org/pub/gnome/sources/pangomm/2.36)
- [gtkmm-3.16.0](http://ftp.gnome.org/pub/GNOME/sources/gtkmm/3.16)
- [libxml++-2.38.0](http://ftp.gnome.org/pub/GNOME/sources/libxml++/2.38)
- [gstreamermm-1.4.3](http://ftp.gnome.org/pub/GNOME/sources/gstreamermm/1.4)
- GTK+ (See msys2 fordetails)

## TODO

* Consider using ExternalProject CMake module
