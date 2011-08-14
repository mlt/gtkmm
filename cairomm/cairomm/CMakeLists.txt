set(CAIROMM_SRCS
context.cc
context_surface_quartz.cc
context_surface_win32.cc
context_surface_xlib.cc
device.cc
exception.cc
fontface.cc
fontoptions.cc
matrix.cc
path.cc
pattern.cc
private.cc
quartz_font.cc
quartz_surface.cc
region.cc
scaledfont.cc
surface.cc
win32_font.cc
win32_surface.cc
xlib_surface.cc
)

add_definitions( -DCAIROMM_BUILD )
add_library(cairomm-${CAIROMM_VERSION} SHARED ${CAIROMM_SRCS} cairomm.def ../${EXTRA}/cairomm/cairomm.rc)

add_custom_command (OUTPUT cairomm.def
COMMAND ECHO Will be generated later > cairomm.def
)
add_custom_command(TARGET cairomm-${CAIROMM_VERSION} PRE_LINK
COMMAND	gendef ${CMAKE_CURRENT_BINARY_DIR}/cairomm.def cairomm-${CAIROMM_VERSION}${POSTFIX}.dll ${CMAKE_CURRENT_BINARY_DIR}${CMAKE_FILES_DIRECTORY}/cairomm-${CAIROMM_VERSION}.dir/*.obj
)

target_link_libraries(cairomm-${CAIROMM_VERSION} cairo.lib cairo-gobject.lib sigc-${SIGC_VERSION})

install(FILES ${CMAKE_CURRENT_BINARY_DIR}/cairomm-${CAIROMM_VERSION}${POSTFIX}.pdb DESTINATION "bin" CONFIGURATIONS DEBUG)

install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/../${EXTRA}/cairomm/cairommconfig.h DESTINATION "lib/cairomm-${CAIROMM_VERSION}/include")

install(TARGETS cairomm-${CAIROMM_VERSION}
LIBRARY DESTINATION "lib"
ARCHIVE DESTINATION "lib"
RUNTIME DESTINATION "bin")

install(DIRECTORY ./ DESTINATION include/cairomm-${CAIROMM_VERSION}/cairomm/ FILES_MATCHING PATTERN "*.h"
PATTERN "PaxHeaders*" EXCLUDE
)
