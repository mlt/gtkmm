# to rescue CMake files use: 7z a -ir!CMakeLists.txt cmake.7z
cmake_minimum_required(VERSION 2.8)

project(gtk+)
set(GTK_MAJOR_VERSION 3)
set(GTK_MINOR_VERSION 1)
set(GTK_MICRO_VERSION 8)
set( GTK_INTERFACE_AGE 0)
math (EXPR GTK_BINARY_AGE  100*${GTK_MINOR_VERSION}+${GTK_MICRO_VERSION})

set (GlibEtcInstallRoot S:/obs/usr/i686-w64-mingw32/sys-root/mingw CACHE PATH "GlibEtcInstallRoot")
#set (CMAKE_INSTALL_PREFIX ${GlibEtcInstallRoot} CACHE PATH "Override" FORCE)

include(FindPerl)
if(NOT PERL_FOUND)
#message(FATAL_ERROR "Need perl to generate some files")
endif(NOT PERL_FOUND)

configure_file(gtk/gtkversion.h.in ${CMAKE_CURRENT_SOURCE_DIR}/gtk/gtkversion.h @ONLY)
configure_file(gdk/gdkconfig.h.win32 ${CMAKE_CURRENT_SOURCE_DIR}/gdk/gdkconfig.h COPYONLY)

# Use this or uncomment next line for release build "\Program Files\CMake 2.8\bin\cmake.exe" -D CMAKE_BUILD_TYPE=RELEASE ..
#set(CMAKE_BUILD_TYPE RELEASE CACHE STRING "Forced release" FORCE)

configure_file(config.h.win32.in ${CMAKE_CURRENT_SOURCE_DIR}/config.h COPYONLY)

if (MSVC)
add_definitions( /wd4250 /wd4018 /wd4305 /wd4244 /wd4996 /wd4101 /wd4090 )
endif (MSVC)

set (GtkApiVersion "${GTK_MAJOR_VERSION}.${GTK_MINOR_VERSION}")
set (GtkBinaryVersion "${GtkApiVersion}.${GTK_MICRO_VERSION}")

#if (MSVC80)
#set (CMAKE_Debug_POSTFIX "-vc80-d")
#set (CMAKE_RELEASE_POSTFIX "-vc80")
#set(EXTRA "MSVC_Net2005")
#elseif (MSVC90)
#set (CMAKE_Debug_POSTFIX "-vc90-d")
#set (CMAKE_RELEASE_POSTFIX "-vc90")
#set(EXTRA "MSVC_Net2008")
#elseif (MSVC10)
#set (CMAKE_Debug_POSTFIX "-vc100-d")
#set (CMAKE_RELEASE_POSTFIX "-vc100")
#set(EXTRA "MSVC_Net2010")
#endif (MSVC80)

add_definitions( -DHAVE_CONFIG_H -DG_DISABLE_DEPRECATED
-DG_DISABLE_SINGLE_INCLUDES -DATK_DISABLE_SINGLE_INCLUDES
-DGDK_PIXBUF_DISABLE_SINGLE_INCLUDES -DGTK_DISABLE_SINGLE_INCLUDES )

include_directories( .
		     gdk
		     gdk/win32
		     gtk
		     ${GlibEtcInstallRoot}/include
		     ${GlibEtcInstallRoot}/include/glib-2.0
		     ${GlibEtcInstallRoot}/lib/glib-2.0/include
		     ${GlibEtcInstallRoot}/include/atk-1.0
		     ${GlibEtcInstallRoot}/include/pango-1.0
		     ${GlibEtcInstallRoot}/include/cairo
		     ${GlibEtcInstallRoot}/include/gdk-pixbuf-2.0
)

link_directories( ${GlibEtcInstallRoot}/lib )

add_subdirectory(modules)
add_subdirectory(gdk)
add_subdirectory(gtk)
add_subdirectory(demos)
#add_dependencies(gtk3-demo gtk gdk gdk-win32 modules-input gdk/gdkenumtypes.h)
add_dependencies(modules-input gdkenumtypes gtktypebuiltins)

####### INSTALL #########
#set( CPACK_GENERATOR "ZIP" )

#SET(CPACK_PACKAGE_VERSION_MAJOR "${GTK_MAJOR_VERSION}")
#SET(CPACK_PACKAGE_VERSION_MINOR "${GTK_MINOR_VERSION}")
#SET(CPACK_PACKAGE_VERSION_PATCH "${GTK_MICRO_VERSION}")

#INCLUDE(CPack)
