cmake_minimum_required(VERSION 2.8)
project(gtkmm)

include(macros.cmake)

set(SIGC_DIR libsigc++-2.2.10)
set(GLIBMM_DIR glibmm-2.29.13)
set(ATKMM_DIR atkmm-2.22.5)
set(CAIROMM_DIR cairomm-1.10.0)
set(PANGOMM_DIR pangomm-2.28.2)
set(GTKMM_DIR gtkmm-3.1.18)
set(XMLMM_DIR libxml++-2.34.2)
set(GSTREAMERMM_DIR gstreamermm-0.10.10)

VERSION(${SIGC_DIR} SIGC_VERSION)
VERSION(${GLIBMM_DIR} GLIBMM_VERSION)
VERSION(${ATKMM_DIR} ATKMM_VERSION)
VERSION(${CAIROMM_DIR} CAIROMM_VERSION)
VERSION(${PANGOMM_DIR} PANGOMM_VERSION)
VERSION(${GTKMM_DIR} GTKMM_VERSION)
VERSION(${XMLMM_DIR} XMLMM_VERSION)
VERSION(${GSTREAMERMM_DIR} GSTREAMERMM_VERSION)

SET(ATKMM_DIR_URL http://ftp.gnome.org/pub/GNOME/sources/atkmm/${ATKMM_VERSION})
SET(CAIROMM_DIR_URL http://cairographics.org/releases)
SET(GLIBMM_DIR_URL http://ftp.gnome.org/pub/GNOME/sources/glibmm/${GLIBMM_VERSION})
SET(GTKMM_DIR_URL http://ftp.gnome.org/pub/GNOME/sources/gtkmm/${GTKMM_VERSION})
SET(PANGOMM_DIR_URL http://ftp.gnome.org/pub/gnome/sources/pangomm/${PANGOMM_VERSION})
SET(SIGC_DIR_URL http://ftp.gnome.org/pub/GNOME/sources/libsigc++/${SIGC_VERSION})
SET(XMLMM_DIR_URL http://ftp.gnome.org/pub/GNOME/sources/libxml++/${XMLMM_VERSION})
SET(GSTREAMERMM_DIR_URL http://ftp.gnome.org/pub/GNOME/sources/gstreamermm/${GSTREAMERMM_VERSION})

GET(${ATKMM_DIR_URL}/${ATKMM_DIR}.tar.bz2)
GET(${CAIROMM_DIR_URL}/${CAIROMM_DIR}.tar.gz)
GET(${GLIBMM_DIR_URL}/${GLIBMM_DIR}.tar.bz2)
if(NOT EXISTS ${GTKMM_DIR})
GET(${GTKMM_DIR_URL}/${GTKMM_DIR}.tar.bz2)
execute_process(COMMAND patch -p0 --binary -i ${CMAKE_CURRENT_SOURCE_DIR}/patches/gtkmm_demowindow_cc.patch
WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/${GTKMM_DIR})
endif()
GET(${PANGOMM_DIR_URL}/${PANGOMM_DIR}.tar.bz2)
GET(${SIGC_DIR_URL}/${SIGC_DIR}.tar.bz2)
GET(${XMLMM_DIR_URL}/${XMLMM_DIR}.tar.bz2)
if(NOT EXISTS ${GSTREAMERMM_DIR})
GET(${GSTREAMERMM_DIR_URL}/${GSTREAMERMM_DIR}.tar.bz2)
execute_process(COMMAND patch -p0 --binary -i ${CMAKE_CURRENT_SOURCE_DIR}/patches/gstreamermm_clock_h.patch
WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/${GSTREAMERMM_DIR})
execute_process(COMMAND patch -p0 --binary -i ${CMAKE_CURRENT_SOURCE_DIR}/patches/gstreamer_mp_player_window_cc.patch
WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/${GSTREAMERMM_DIR})
#FIXME: parse version
set(GSTREAMERMM_MAJOR_VERSION 0)
set(GSTREAMERMM_MINOR_VERSION 10)
set(GSTREAMERMM_MiCRO_VERSION 10)
configure_file(patches/gstreamermmconfig.h.in ${CMAKE_CURRENT_SOURCE_DIR}/${GSTREAMERMM_DIR}/gstreamer/gstreamermmconfig.h @ONLY)
endif()

SET(CPACK_PACKAGE_VERSION_MAJOR 3)
SET(CPACK_PACKAGE_VERSION_MINOR 1)
set( CPACK_GENERATOR "ZIP" )
TODAY(TWEAK)
SET(CPACK_PACKAGE_VERSION_PATCH "18-${TWEAK}")

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
elseif (MSVC11)
set (CMAKE_DEBUG_POSTFIX "-vc110-d")
set (CMAKE_RELEASE_POSTFIX "-vc110")
set(EXTRA "MSVC_Net2008")
else()
error("FIXME: You are using unknown MSVC version.")
endif (MSVC80)

string(TOUPPER ${CMAKE_BUILD_TYPE} BT)
set(POSTFIX ${CMAKE_${BT}_POSTFIX})
message("Postfix is ${POSTFIX}")

set (GlibEtcInstallRoot ${CMAKE_CURRENT_SOURCE_DIR}/usr/i686-w64-mingw32/sys-root/mingw CACHE PATH "GlibEtcInstallRoot")
set (CMAKE_INSTALL_PREFIX C:/gtkmm CACHE PATH "Installation prefix" FORCE)

add_definitions( -DG_HAVE_ISO_VARARGS )
add_definitions( /wd4273 /wd4290 /wd4250 )

include_directories(
     ${GlibEtcInstallRoot}/include
     ${GlibEtcInstallRoot}/include/gtk-3.0
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
