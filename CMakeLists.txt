cmake_minimum_required(VERSION 2.8)
project(gtkmm)

include(macros.cmake)
MKLINK(gtk+.local gtk+)

set(SIGC_DIR libsigc++-2.2.10)
set(GLIBMM_DIR glibmm-2.28.2)
set(ATKMM_DIR atkmm-2.22.5)
set(CAIROMM_DIR cairomm-1.10.0)
set(PANGOMM_DIR pangomm-2.28.2)
set(GTKMM_DIR gtkmm-3.1.8)
set(XMLMM_DIR libxml++-2.34.1)
set(GSTREAMERMM_DIR gstreamermm-0.10.9)

VERSION(${SIGC_DIR} SIGC_VERSION)
VERSION(${GLIBMM_DIR} GLIBMM_VERSION)
VERSION(${ATKMM_DIR} ATKMM_VERSION)
VERSION(${CAIROMM_DIR} CAIROMM_VERSION)
VERSION(${PANGOMM_DIR} PANGOMM_VERSION)
VERSION(${GTKMM_DIR} GTKMM_VERSION)
VERSION(${XMLMM_DIR} XMLMM_VERSION)
VERSION(${GSTREAMERMM_DIR} GSTREAMERMM_VERSION)
set(GtkApiVersion 3.1)

if(NOT EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/usr)
OBS()
endif()

GET(http://ftp.gnome.org/pub/GNOME/sources/atkmm/${ATKMM_VERSION}/${ATKMM_DIR}.tar.bz2)
GET(http://cairographics.org/releases/${CAIROMM_DIR}.tar.gz)
GET(ftp://ftp.gnome.org/pub/GNOME/sources/glibmm/${GLIBMM_VERSION}/${GLIBMM_DIR}.tar.bz2)
GET(ftp://ftp.gnome.org/pub/GNOME/sources/gtkmm/${GTKMM_VERSION}/${GTKMM_DIR}.tar.bz2)
GET(http://ftp.gnome.org/pub/gnome/sources/pangomm/${PANGOMM_VERSION}/${PANGOMM_DIR}.tar.bz2)
GET(http://ftp.gnome.org/pub/GNOME/sources/libsigc++/${SIGC_VERSION}/${SIGC_DIR}.tar.bz2)
GET(http://ftp.gnome.org/pub/GNOME/sources/libxml++/${XMLMM_VERSION}/${XMLMM_DIR}.tar.bz2)
GET(http://ftp.gnome.org/pub/GNOME/sources/gstreamermm/${GSTREAMERMM_VERSION}/${GSTREAMERMM_DIR}.tar.bz2)

SET(CPACK_PACKAGE_VERSION_MAJOR 3)
SET(CPACK_PACKAGE_VERSION_MINOR 1)
set( CPACK_GENERATOR "ZIP" )
TODAY(TWEAK)
SET(CPACK_PACKAGE_VERSION_PATCH "8-${TWEAK}")

INCLUDE(CPack)

# Use this or uncomment next line for release build "\Program Files\CMake 2.8\bin\cmake.exe" -D CMAKE_BUILD_TYPE=RELEASE ..
#set(CMAKE_BUILD_TYPE RELEASE CACHE STRING "Forced release" FORCE)

if (MSVC80)
set (CMAKE_DEBUG_POSTFIX "-vc80-d")
set (CMAKE_RELEASE_POSTFIX "-vc80")
set(EXTRA "MSVC_Net2005")
elseif (MSVC90)
set (CMAKE_DEBUG_POSTFIX "-vc90-d")
set (CMAKE_RELEASE_POSTFIX "-vc90")
set(EXTRA "MSVC_Net2008")
elseif (MSVC10)
set (CMAKE_DEBUG_POSTFIX "-vc100-d")
set (CMAKE_RELEASE_POSTFIX "-vc100")
set(EXTRA "MSVC_Net2010")
endif (MSVC80)

string(TOUPPER ${CMAKE_BUILD_TYPE} BT)
set(POSTFIX ${CMAKE_${BT}_POSTFIX})
message("Postfix is ${POSTFIX}")

set (GlibEtcInstallRoot ${CMAKE_CURRENT_SOURCE_DIR}/usr/i686-w64-mingw32/sys-root/mingw CACHE PATH "GlibEtcInstallRoot")
set (CMAKE_INSTALL_PREFIX ${GlibEtcInstallRoot} CACHE PATH "Override" FORCE)

add_definitions( -DG_HAVE_ISO_VARARGS )
add_definitions( /wd4273 /wd4290 /wd4250 )

include_directories(
     ${GlibEtcInstallRoot}/include
     ${GlibEtcInstallRoot}/include/glib-2.0
     ${GlibEtcInstallRoot}/lib/glib-2.0/include
     ${GlibEtcInstallRoot}/include/atk-1.0
     ${GlibEtcInstallRoot}/include/pango-1.0
     ${GlibEtcInstallRoot}/include/cairo
     ${GlibEtcInstallRoot}/include/gdk-pixbuf-2.0
     ${SIGC_DIR}
     ${SIGC_DIR}/${EXTRA}
     ${GLIBMM_DIR}/glib
     ${GLIBMM_DIR}/${EXTRA}/glibmm
     ${GLIBMM_DIR}/gio
     ${GLIBMM_DIR}/${EXTRA}/giomm
     ${ATKMM_DIR}/atk
     ${GlibEtcInstallRoot}/include/freetype2
     ${CAIROMM_DIR}
     ${CAIROMM_DIR}/${EXTRA}/cairomm
     ${PANGOMM_DIR}/pango
     ${PANGOMM_DIR}/${EXTRA}/pangomm
     gtk+
     ${GTKMM_DIR}/gdk
     ${GTKMM_DIR}/${EXTRA}/gdkmm
     ${GTKMM_DIR}/gtk
     ${GTKMM_DIR}/${EXTRA}/gtkmm
)

link_directories(
     ${GlibEtcInstallRoot}/lib
)

add_subdirectory(${SIGC_DIR}/sigc++)
add_subdirectory(${GLIBMM_DIR}/${EXTRA}/gendef)
add_subdirectory(${GLIBMM_DIR}/glib/glibmm)
add_subdirectory(${GLIBMM_DIR}/gio/giomm)
add_subdirectory(${ATKMM_DIR}/atk/atkmm)
add_subdirectory(${CAIROMM_DIR}/cairomm)
add_subdirectory(${PANGOMM_DIR}/pango/pangomm)
add_subdirectory(gtk+)
add_subdirectory(${GTKMM_DIR}/gdk/gdkmm)
add_subdirectory(${GTKMM_DIR}/gtk/gtkmm)
add_subdirectory(${GTKMM_DIR}/demos/gtk-demo)
add_subdirectory(${XMLMM_DIR}/libxml++)
add_subdirectory(${GSTREAMERMM_DIR})

configure_file(MSVC/gtkmm3.vsprops.in ${CMAKE_CURRENT_SOURCE_DIR}/MSVC/gtkmm3${POSTFIX}.vsprops @ONLY)
install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/MSVC/gtkmm3${POSTFIX}.vsprops DESTINATION "MSVC")
#set(RuntimeLibrary 3) # for debug

configure_file(README.md.in ${CMAKE_CURRENT_SOURCE_DIR}/README.md @ONLY)

install(DIRECTORY ${GlibEtcInstallRoot}/ DESTINATION .)
