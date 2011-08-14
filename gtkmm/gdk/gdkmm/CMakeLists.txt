set(GDKMM_SRCS
color.cc
cursor.cc
device.cc
devicemanager.cc
display.cc
displaymanager.cc
dragcontext.cc
event.cc
general.cc
pixbuf.cc
pixbufanimation.cc
pixbufanimationiter.cc
pixbufformat.cc
pixbufloader.cc
rectangle.cc
rgba.cc
screen.cc
timecoord.cc
types.cc
visual.cc
window.cc
wrap_init.cc
)

add_definitions( -DGDKMM_DLL -DGDKMM_BUILD -D_WINDLL )
add_library(gdkmm-${GTKMM_VERSION} SHARED ${GDKMM_SRCS} gdkmm.def ../../${EXTRA}/gdkmm/gdkmm.rc)

add_custom_command (OUTPUT gdkmm.def
COMMAND echo Will be generated later > gdkmm.def
)
add_custom_command(TARGET gdkmm-${GTKMM_VERSION} PRE_LINK
COMMAND	gendef ${CMAKE_CURRENT_BINARY_DIR}/gdkmm.def gdkmm-${GTKMM_VERSION}${POSTFIX}.dll ${CMAKE_CURRENT_BINARY_DIR}${CMAKE_FILES_DIRECTORY}/gdkmm-${GTKMM_VERSION}.dir/*.obj
)

target_link_libraries(gdkmm-${GTKMM_VERSION} glibmm-${GLIBMM_VERSION} giomm-${GLIBMM_VERSION} sigc-${SIGC_VERSION} cairomm-${CAIROMM_VERSION} gtk-${GtkApiVersion})

install(TARGETS gdkmm-${GTKMM_VERSION}
LIBRARY DESTINATION "lib"
ARCHIVE DESTINATION "lib"
RUNTIME DESTINATION "bin")

install(FILES ${CMAKE_CURRENT_BINARY_DIR}/gdkmm-${GTKMM_VERSION}${POSTFIX}.pdb DESTINATION "bin" CONFIGURATIONS DEBUG)

install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/../../${EXTRA}/gdkmm/gdkmmconfig.h DESTINATION "lib/gdkmm-${GTKMM_VERSION}/include")

install(DIRECTORY ../ DESTINATION include/gdkmm-${GTKMM_VERSION}/
FILES_MATCHING PATTERN "*.h"
PATTERN "src" EXCLUDE
PATTERN "private" EXCLUDE
PATTERN "PaxHeaders.31493" EXCLUDE
)
#install(DIRECTORY ./ DESTINATION include/gdkmm-${GTKMM_VERSION}/gdkmm/ FILES_MATCHING PATTERN "*.h"
#PATTERN "src" EXCLUDE
#PATTERN "private" EXCLUDE
#PATTERN "PaxHeaders.31493" EXCLUDE
#)
