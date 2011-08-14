set(PANGOMM_SRCS
attributes.cc
attriter.cc
attrlist.cc
cairofontmap.cc
color.cc
context.cc
coverage.cc
font.cc
fontdescription.cc
fontface.cc
fontfamily.cc
fontmap.cc
fontmetrics.cc
fontset.cc
glyph.cc
glyphstring.cc
init.cc
item.cc
language.cc
layout.cc
layoutiter.cc
layoutline.cc
layoutrun.cc
rectangle.cc
renderer.cc
tabarray.cc
wrap_init.cc
)

add_definitions( -DPANGOMM_BUILD -D_WINDLL )
add_library(pangomm-${PANGOMM_VERSION} SHARED ${PANGOMM_SRCS} pangomm.def ../../${EXTRA}/pangomm/pangomm.rc)

add_custom_command (OUTPUT pangomm.def
COMMAND echo Will be generated later > pangomm.def
)
add_custom_command(TARGET pangomm-${PANGOMM_VERSION} PRE_LINK
COMMAND	gendef ${CMAKE_CURRENT_BINARY_DIR}/pangomm.def pangomm-${PANGOMM_VERSION}${POSTFIX}.dll ${CMAKE_CURRENT_BINARY_DIR}${CMAKE_FILES_DIRECTORY}/pangomm-${PANGOMM_VERSION}.dir/*.obj
)

target_link_libraries(pangomm-${PANGOMM_VERSION} pango-1.0.lib cairomm-${CAIROMM_VERSION} pangocairo-1.0.lib glibmm-${GLIBMM_VERSION} sigc-${SIGC_VERSION})

install(TARGETS pangomm-${PANGOMM_VERSION}
LIBRARY DESTINATION "lib"
ARCHIVE DESTINATION "lib"
RUNTIME DESTINATION "bin")

install(FILES ${CMAKE_CURRENT_BINARY_DIR}/pangomm-${PANGOMM_VERSION}${POSTFIX}.pdb DESTINATION "bin" CONFIGURATIONS DEBUG)

install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/../../${EXTRA}/pangomm/pangommconfig.h DESTINATION "lib/pangomm-${PANGOMM_VERSION}/include")

install(DIRECTORY ../ DESTINATION include/pangomm-${PANGOMM_VERSION}/ FILES_MATCHING PATTERN "*.h"
PATTERN "PaxHeaders*" EXCLUDE
PATTERN "private" EXCLUDE
)
#install(DIRECTORY ./ DESTINATION include/pangomm-${PANGOMM_VERSION}/pangomm/ FILES_MATCHING PATTERN "*.h")
