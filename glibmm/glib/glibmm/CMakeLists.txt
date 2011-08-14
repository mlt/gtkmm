set(GLIBMM_SRCS
arrayhandle.cc
balancedtree.cc
checksum.cc
class.cc
containers.cc
convert.cc
date.cc
debug.cc
dispatcher.cc
error.cc
exception.cc
exceptionhandler.cc
fileutils.cc
init.cc
interface.cc
iochannel.cc
keyfile.cc
main.cc
markup.cc
miscutils.cc
module.cc
nodetree.cc
object.cc
objectbase.cc
optioncontext.cc
optionentry.cc
optiongroup.cc
pattern.cc
property.cc
propertyproxy.cc
propertyproxy_base.cc
quark.cc
random.cc
regex.cc
sarray.cc
shell.cc
signalproxy.cc
signalproxy_connectionnode.cc
spawn.cc
streamiochannel.cc
stringutils.cc
thread.cc
threadpool.cc
timer.cc
timeval.cc
unicode.cc
uriutils.cc
ustring.cc
utility.cc
value.cc
value_basictypes.cc
value_custom.cc
valuearray.cc
variant.cc
variant_basictypes.cc
variantiter.cc
varianttype.cc
vectorutils.cc
wrap.cc
wrap_init.cc
)

add_definitions( -DGLIBMM_DLL -DGLIBMM_BUILD -D_WINDLL )
add_library(glibmm-${GLIBMM_VERSION} SHARED ${GLIBMM_SRCS} glibmm.def ../../${EXTRA}/glibmm/glibmm.rc)

add_custom_command (OUTPUT glibmm.def
COMMAND echo Will be generated later > glibmm.def
)
add_custom_command(TARGET glibmm-${GLIBMM_VERSION} PRE_LINK
COMMAND	gendef ${CMAKE_CURRENT_BINARY_DIR}/glibmm.def glibmm-${GLIBMM_VERSION}${POSTFIX}.dll ${CMAKE_CURRENT_BINARY_DIR}${CMAKE_FILES_DIRECTORY}/glibmm-${GLIBMM_VERSION}.dir/*.obj
)

target_link_libraries(glibmm-${GLIBMM_VERSION} glib-2.0.lib gobject-2.0.lib gmodule-2.0.lib
gio-2.0.lib sigc-${SIGC_VERSION})

install(TARGETS glibmm-${GLIBMM_VERSION}
LIBRARY DESTINATION "lib"
ARCHIVE DESTINATION "lib"
RUNTIME DESTINATION "bin")

install(FILES ${CMAKE_CURRENT_BINARY_DIR}/glibmm-${GLIBMM_VERSION}${POSTFIX}.pdb DESTINATION "bin" CONFIGURATIONS DEBUG)

install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/../../${EXTRA}/glibmm/glibmmconfig.h DESTINATION "lib/glibmm-${GLIBMM_VERSION}/include")

install(DIRECTORY ../ DESTINATION include/glibmm-${GLIBMM_VERSION}/ FILES_MATCHING PATTERN "*.h"
PATTERN "PaxHeaders*" EXCLUDE
)
#install(DIRECTORY ./ DESTINATION include/glibmm-${GLIBMM_VERSION}/glibmm/ FILES_MATCHING PATTERN "*.h")
