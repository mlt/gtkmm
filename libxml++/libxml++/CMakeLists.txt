include_directories(
     ${GlibEtcInstallRoot}/include/libxml2
     ../${EXTRA}/libxml++
     ..
)

add_definitions(-DLIBXMLPP_BUILD -D_WINDLL -DGLIBMM_DLL -DGLIBMM_MSC)

set(XMLMM_SRCS
attribute.cc
nodes/cdatanode.cc
nodes/commentnode.cc
nodes/contentnode.cc
document.cc
parsers/domparser.cc
dtd.cc
validators/dtdvalidator.cc
nodes/element.cc
nodes/entityreference.cc
exceptions/exception.cc
exceptions/internal_error.cc
io/istreamparserinputbuffer.cc
keepblanks.cc
nodes/node.cc
noncopyable.cc
io/ostreamoutputbuffer.cc
io/outputbuffer.cc
exceptions/parse_error.cc
parsers/parser.cc
io/parserinputbuffer.cc
nodes/processinginstructionnode.cc
parsers/saxparser.cc
schema.cc
validators/schemavalidator.cc
nodes/textnode.cc
parsers/textreader.cc
validators/validator.cc
exceptions/validity_error.cc
)

add_library(xmlpp-${XMLMM_VERSION} SHARED ${XMLMM_SRCS} libxml++.def ../${EXTRA}/libxml++/libxml++.rc)
set_target_properties(xmlpp-${XMLMM_VERSION} PROPERTIES OUTPUT_NAME xml++-${XMLMM_VERSION})

add_custom_command (OUTPUT libxml++.def
COMMAND ECHO Will be generated later > libxml++.def
)
add_custom_command(TARGET xmlpp-${XMLMM_VERSION} PRE_LINK
COMMAND	gendef ${CMAKE_CURRENT_BINARY_DIR}/libxml++.def xml++-${XMLMM_VERSION}${POSTFIX}.dll
  ${CMAKE_CURRENT_BINARY_DIR}${CMAKE_FILES_DIRECTORY}/xmlpp-${XMLMM_VERSION}.dir/*.obj
  ${CMAKE_CURRENT_BINARY_DIR}${CMAKE_FILES_DIRECTORY}/xmlpp-${XMLMM_VERSION}.dir/io/*.obj 
  ${CMAKE_CURRENT_BINARY_DIR}${CMAKE_FILES_DIRECTORY}/xmlpp-${XMLMM_VERSION}.dir/nodes/*.obj 
  ${CMAKE_CURRENT_BINARY_DIR}${CMAKE_FILES_DIRECTORY}/xmlpp-${XMLMM_VERSION}.dir/parsers/*.obj 
  ${CMAKE_CURRENT_BINARY_DIR}${CMAKE_FILES_DIRECTORY}/xmlpp-${XMLMM_VERSION}.dir/validators/*.obj 
)

target_link_libraries(xmlpp-${XMLMM_VERSION} xml2.lib glibmm-${GLIBMM_VERSION} giomm-${GLIBMM_VERSION} sigc-${SIGC_VERSION})

install(TARGETS xmlpp-${XMLMM_VERSION}
LIBRARY DESTINATION "lib"
ARCHIVE DESTINATION "lib"
RUNTIME DESTINATION "bin")

install(FILES ${CMAKE_CURRENT_BINARY_DIR}/xml++-${XMLMM_VERSION}${POSTFIX}.pdb DESTINATION "bin" CONFIGURATIONS DEBUG)

install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/../${EXTRA}/libxml++/libxml++config.h DESTINATION "lib/libxml++-${XMLMM_VERSION}/include")

install(DIRECTORY ../ DESTINATION include/libxml++-${XMLMM_VERSION}/ FILES_MATCHING PATTERN "*.h"
PATTERN "src" EXCLUDE
PATTERN "private" EXCLUDE
PATTERN "PaxHeaders*" EXCLUDE
)
#install(DIRECTORY ./ DESTINATION include/libxml++-${XMLMM_VERSION}/libxml++/ FILES_MATCHING PATTERN "*.h")
