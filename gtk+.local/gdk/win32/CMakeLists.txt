add_definitions ( -DINSIDE_GDK_WIN32 )

set (GDK_WIN32_SRCS
bdfcursor.c
gdkcursor-win32.c
gdkdevice-win32.c
gdkdevice-win32.h
gdkdevice-wintab.c
gdkdevice-wintab.h
gdkdevicemanager-win32.c
gdkdevicemanager-win32.h
gdkdisplay-win32.c
gdkdisplaymanager-win32.c
gdkdnd-win32.c
gdkevents-win32.c
gdkgeometry-win32.c
gdkglobals-win32.c
gdkinput.c
gdkkeys-win32.c
gdkmain-win32.c
gdkprivate-win32.h
gdkproperty-win32.c
gdkscreen-win32.c
gdkselection-win32.c
gdktestutils-win32.c
gdkvisual-win32.c
gdkwin32.h
gdkwin32cursor.h
gdkwin32display.h
gdkwin32displaymanager.h
gdkwin32dnd.h
gdkwin32id.c
gdkwin32keys.h
gdkwin32screen.h
gdkwin32window.h
gdkwindow-win32.c
gdkwindow-win32.h
pktdef.h
wintab.h
xcursors.h
${CMAKE_CURRENT_SOURCE_DIR}/../gdkenumtypes.h
)

SET_SOURCE_FILES_PROPERTIES( ${CMAKE_CURRENT_SOURCE_DIR}/../gdkenumtypes.h
PROPERTIES GENERATED true )

add_library(gdk-win32-lib STATIC ${GDK_WIN32_SRCS})

set_target_properties (gdk-win32-lib PROPERTIES OUTPUT_NAME "gdk-win32")
