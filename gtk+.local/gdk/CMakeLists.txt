add_definitions ( -DGDK_COMPILATION -DG_LOG_DOMAIN="Gdk" )

set ( GDK_SRCS
gdk.c
gdk.h
gdkapplaunchcontext.c
gdkapplaunchcontext.h
gdkapplaunchcontextprivate.h
gdkcairo.c
gdkcairo.h
gdkcolor.c
gdkcolor.h
gdkcursor.c
gdkcursor.h
gdkcursorprivate.h
gdkdevice.c
gdkdevice.h
gdkdevicemanager.c
gdkdevicemanager.h
gdkdevicemanagerprivate.h
gdkdeviceprivate.h
gdkdisplay.c
gdkdisplay.h
gdkdisplaymanager.c
gdkdisplaymanager.h
gdkdisplaymanagerprivate.h
gdkdisplayprivate.h
gdkdnd.c
gdkdnd.h
gdkdndprivate.h
${CMAKE_CURRENT_SOURCE_DIR}/gdkenumtypes.c
gdkenumtypes.h
gdkevents.c
gdkevents.h
gdkglobals.c
gdkinternals.h
gdkintl.h
gdkkeynames.c
gdkkeys.c
gdkkeys.h
gdkkeysprivate.h
gdkkeysyms.h
gdkkeysyms-compat.h
gdkkeyuni.c
gdkmain.h
${CMAKE_CURRENT_SOURCE_DIR}/gdkmarshalers.c
gdkmarshalers.h
gdkoffscreenwindow.c
gdkpango.c
gdkpango.h
gdkpixbuf.h
gdkpixbuf-drawable.c
gdkprivate.h
gdkproperty.h
gdkrectangle.c
gdkrectangle.h
gdkrgba.c
gdkrgba.h
gdkscreen.c
gdkscreen.h
gdkscreenprivate.h
gdkselection.c
gdkselection.h
gdktestutils.h
gdkthreads.h
gdktypes.h
gdkvisual.c
gdkvisual.h
gdkvisualprivate.h
gdkwindow.c
gdkwindow.h
gdkwindowimpl.c
gdkwindowimpl.h
gdkx.h
keyname-table.h
)

set (gdk_public_h_sources
gdk.h			
gdkapplaunchcontext.h	
gdkcairo.h		
gdkcolor.h		
gdkcursor.h		
gdkdevice.h		
gdkdevicemanager.h	
gdkdisplay.h		
gdkdisplaymanager.h	
gdkdnd.h		
gdkevents.h		
gdkkeys.h		
gdkkeysyms.h		
gdkkeysyms-compat.h	
gdkmain.h		
gdkpango.h		
gdkpixbuf.h		
gdkprivate.h		
gdkproperty.h		
gdkrectangle.h		
gdkrgba.h		
gdkscreen.h		
gdkselection.h		
gdktestutils.h		
gdkthreads.h		
gdktypes.h		
gdkvisual.h		
gdkwindow.h
win32/gdkwin32window.h
)

add_custom_command (OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/gdkenumtypes.h ${CMAKE_CURRENT_SOURCE_DIR}/gdkenumtypes.c
COMMAND ${PERL} ${GlibEtcInstallRoot}/bin/glib-mkenums --template gdkenumtypes.h.template ${gdk_public_h_sources} > gdkenumtypes.h
COMMAND ${PERL} ${GlibEtcInstallRoot}/bin/glib-mkenums --template gdkenumtypes.c.template ${gdk_public_h_sources} > gdkenumtypes.c
#COMMAND ${CMAKE_COMMAND} copy gdkenumtypes.c ${CMAKE_CURRENT_BINARY_DIR}/gdkenumtypes.c
DEPENDS ${gdk_public_h_sources}
WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
)

add_custom_target(gdkenumtypes DEPENDS gdkenumtypes.h gdkenumtypes.c)

add_custom_command (OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/gdkmarshalers.h ${CMAKE_CURRENT_SOURCE_DIR}/gdkmarshalers.c
COMMAND	${GlibEtcInstallRoot}/bin/glib-genmarshal --prefix=_gdk_marshal gdkmarshalers.list --header >>gdkmarshalers.h
COMMAND	${GlibEtcInstallRoot}/bin/glib-genmarshal --prefix=_gdk_marshal gdkmarshalers.list --body > gdkmarshalers.c
DEPENDS gdkmarshalers.list
WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
)

add_custom_command (OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/gdk.def
COMMAND echo EXPORTS > gdk.def
COMMAND cl /EP -DG_OS_WIN32 -DGDK_WINDOWING_WIN32 -DG_GNUC_CONST= gdk.symbols >> gdk.def
WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
)

add_subdirectory(win32)

add_library(gdk-${GtkApiVersion} SHARED ${GDK_SRCS} gdk.def win32/rc/gdk.rc)

#set_target_properties(gdk-win32 PROPERTIES
#				  IMPORT_SUFFIX "-${GtkApiVersion}.lib"
#)

target_link_libraries(gdk-${GtkApiVersion} gdk-win32-lib gdk_pixbuf-2.0
pangocairo-1.0 pango-1.0 cairo gio-2.0 gmodule-2.0 gobject-2.0
glib-2.0 intl cairo-gobject imm32)

install(TARGETS gdk-${GtkApiVersion}
LIBRARY DESTINATION "lib"
ARCHIVE DESTINATION "lib"
RUNTIME DESTINATION "bin")

install(FILES ${CMAKE_CURRENT_BINARY_DIR}/gdk-${GtkApiVersion}${POSTFIX}.pdb DESTINATION "bin" CONFIGURATIONS DEBUG)

install(DIRECTORY ./ DESTINATION include/gtk-${GtkApiVersion}/gdk
FILES_MATCHING PATTERN "*.h")
