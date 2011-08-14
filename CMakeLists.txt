cmake_minimum_required(VERSION 2.8)
project(gtkmm)

SET(CPACK_PACKAGE_VERSION_MAJOR 3)
SET(CPACK_PACKAGE_VERSION_MINOR 0)
SET(CPACK_PACKAGE_VERSION_PATCH 1)
set( CPACK_GENERATOR "ZIP" )
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

set(POSTFIX ${CMAKE_${CMAKE_BUILD_TYPE}_POSTFIX})
message("Postfix is ${POSTFIX}")

set (GlibEtcInstallRoot S:/obs/usr/i686-w64-mingw32/sys-root/mingw)
set (CMAKE_INSTALL_PREFIX ${GlibEtcInstallRoot} CACHE PATH "Override" FORCE)

add_definitions( /wd4273 /wd4290 /wd4250 )

include_directories(
     ${GlibEtcInstallRoot}/include
     ${GlibEtcInstallRoot}/include/glib-2.0
     ${GlibEtcInstallRoot}/lib/glib-2.0/include
     ${GlibEtcInstallRoot}/include/atk-1.0
     ${GlibEtcInstallRoot}/include/pango-1.0
     ${GlibEtcInstallRoot}/include/cairo
     ${GlibEtcInstallRoot}/include/gdk-pixbuf-2.0
     libsigc++
     libsigc++/${EXTRA}
     glibmm/glib
     glibmm/${EXTRA}/glibmm
     glibmm/gio
     glibmm/${EXTRA}/giomm
     atkmm/atk
     ${GlibEtcInstallRoot}/include/freetype2
     cairomm
     cairomm/${EXTRA}/cairomm
     pangomm/pango
     pangomm/${EXTRA}/pangomm
     gtk+
     gtkmm/gdk
     gtkmm/${EXTRA}/gdkmm
     gtkmm/gtk
     gtkmm/${EXTRA}/gtkmm
)

link_directories(
     ${GlibEtcInstallRoot}/lib
)

set(SIGC_VERSION 2.2)
set(GLIBMM_VERSION 2.28)
set(ATKMM_VERSION 2.22)
set(CAIROMM_VERSION 1.10)
set(PANGOMM_VERSION 2.28)
set(GTKMM_VERSION 3.0)
set(GtkApiVersion 3.1)

add_subdirectory(libsigc++/sigc++)
add_subdirectory(glibmm/${EXTRA}/gendef)
add_subdirectory(glibmm/glib/glibmm)
add_subdirectory(glibmm/gio/giomm)
add_subdirectory(atkmm/atk/atkmm)
add_subdirectory(cairomm/cairomm)
add_subdirectory(pangomm/pango/pangomm)
add_subdirectory(gtk+)
add_subdirectory(gtkmm/gdk/gdkmm)
add_subdirectory(gtkmm/gtk/gtkmm)
add_subdirectory(gtkmm/demos/gtk-demo)

configure_file(MSVC/gtkmm3.vsprops.in ${CMAKE_CURRENT_SOURCE_DIR}/MSVC/gtkmm3${POSTFIX}.vsprops @ONLY)
install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/MSVC/gtkmm3${POSTFIX}.vsprops DESTINATION "MSVC")
#set(RuntimeLibrary 3) # for debug