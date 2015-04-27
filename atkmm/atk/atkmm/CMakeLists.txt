set(ATKMM_SRCS
action.cc
component.cc
document.cc
editabletext.cc
hyperlink.cc
hypertext.cc
image.cc
implementor.cc
init.cc
noopobject.cc
object.cc
objectaccessible.cc
relation.cc
relationset.cc
selection.cc
stateset.cc
streamablecontent.cc
table.cc
text.cc
value.cc
wrap_init.cc
)

add_library(atkmm-${ATKMM_VERSION} SHARED ${ATKMM_SRCS} atkmm.def ../../${EXTRA}/atkmm/atkmm.rc)

add_custom_command (OUTPUT atkmm.def
COMMAND ECHO Will be generated later > atkmm.def
)
add_custom_command(TARGET atkmm-${ATKMM_VERSION} PRE_LINK
COMMAND	gendef ${CMAKE_CURRENT_BINARY_DIR}/atkmm.def $<TARGET_FILE_NAME:atkmm-${ATKMM_VERSION}> ${CMAKE_CURRENT_BINARY_DIR}/$<$<BOOL:${CMAKE_BUILD_TYPE}>:${CMAKE_FILES_DIRECTORY}>/atkmm-${ATKMM_VERSION}.dir/${CMAKE_CFG_INTDIR}/*.obj
)

target_link_libraries(atkmm-${ATKMM_VERSION} atk-1.0.lib glibmm-${GLIBMM_VERSION} giomm-${GLIBMM_VERSION} sigc-${SIGC_VERSION})

install(TARGETS atkmm-${ATKMM_VERSION}
LIBRARY DESTINATION "lib"
ARCHIVE DESTINATION "lib"
RUNTIME DESTINATION "bin")

install(FILES $<TARGET_PDB_FILE:atkmm-${ATKMM_VERSION}> DESTINATION "bin" CONFIGURATIONS DEBUG)

install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/../../${EXTRA}/atkmm/atkmmconfig.h DESTINATION "lib/atkmm-${ATKMM_VERSION}/include")

install(DIRECTORY ../ DESTINATION include/atkmm-${ATKMM_VERSION}/ FILES_MATCHING PATTERN "*.h"
PATTERN "src" EXCLUDE
PATTERN "private" EXCLUDE
PATTERN "PaxHeaders*" EXCLUDE
)
#install(DIRECTORY ./ DESTINATION include/atkmm-${ATKMM_VERSION}/atkmm/ FILES_MATCHING PATTERN "*.h")
