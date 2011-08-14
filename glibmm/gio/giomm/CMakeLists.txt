set(GIOMM_SRCS
appinfo.cc
asyncinitable.cc
asyncresult.cc
bufferedinputstream.cc
bufferedoutputstream.cc
cancellable.cc
contenttype.cc
credentials.cc
datainputstream.cc
dataoutputstream.cc
dbusaddress.cc
dbusauthobserver.cc
dbusconnection.cc
dbuserror.cc
dbuserrorutils.cc
dbusinterfacevtable.cc
dbusintrospection.cc
dbusmessage.cc
dbusmethodinvocation.cc
dbusownname.cc
dbusproxy.cc
dbusserver.cc
dbussubtreevtable.cc
dbusutils.cc
dbuswatchname.cc
drive.cc
emblem.cc
emblemedicon.cc
enums.cc
error.cc
file.cc
fileattributeinfo.cc
fileattributeinfolist.cc
fileenumerator.cc
fileicon.cc
fileinfo.cc
fileinputstream.cc
fileiostream.cc
filemonitor.cc
filenamecompleter.cc
fileoutputstream.cc
filterinputstream.cc
filteroutputstream.cc
icon.cc
inetaddress.cc
inetsocketaddress.cc
init.cc
initable.cc
inputstream.cc
iostream.cc
loadableicon.cc
memoryinputstream.cc
memoryoutputstream.cc
mount.cc
mountoperation.cc
networkaddress.cc
networkservice.cc
outputstream.cc
proxy.cc
proxyaddress.cc
proxyresolver.cc
resolver.cc
seekable.cc
settings.cc
slot_async.cc
socket.cc
socketaddress.cc
socketaddressenumerator.cc
socketclient.cc
socketconnectable.cc
socketconnection.cc
socketcontrolmessage.cc
socketlistener.cc
socketservice.cc
srvtarget.cc
tcpconnection.cc
themedicon.cc
threadedsocketservice.cc
volume.cc
volumemonitor.cc
wrap_init.cc
)

add_definitions( -DGIOMM_DLL -DGIOMM_BUILD -D_WINDLL )
add_library(giomm-${GLIBMM_VERSION} SHARED ${GIOMM_SRCS} giomm.def ../../${EXTRA}/giomm/giomm.rc)
target_link_libraries(giomm-${GLIBMM_VERSION} glib-2.0.lib gobject-2.0.lib gmodule-2.0.lib
gio-2.0.lib sigc-${SIGC_VERSION} glibmm-${GLIBMM_VERSION})

#add_custom_target(giommdef DEPENDS gendef giomm.def )
add_custom_command (OUTPUT giomm.def
COMMAND ECHO Will be generated later > giomm.def
)
add_custom_command(TARGET giomm-${GLIBMM_VERSION} PRE_LINK
COMMAND	gendef ${CMAKE_CURRENT_BINARY_DIR}/giomm.def giomm-${GLIBMM_VERSION}${POSTFIX}.dll ${CMAKE_CURRENT_BINARY_DIR}${CMAKE_FILES_DIRECTORY}/giomm-${GLIBMM_VERSION}.dir/*.obj
)

install(TARGETS giomm-${GLIBMM_VERSION}
LIBRARY DESTINATION "lib"
ARCHIVE DESTINATION "lib"
RUNTIME DESTINATION "bin")

install(FILES ${CMAKE_CURRENT_BINARY_DIR}/giomm-${GLIBMM_VERSION}${POSTFIX}.pdb DESTINATION "bin" CONFIGURATIONS DEBUG)

install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/../../${EXTRA}/giomm/giommconfig.h DESTINATION "lib/giomm-${GLIBMM_VERSION}/include")

install(DIRECTORY ../ DESTINATION include/giomm-${GLIBMM_VERSION}/ FILES_MATCHING PATTERN "*.h"
PATTERN "PaxHeaders*" EXCLUDE
)
#install(DIRECTORY ./ DESTINATION include/giomm-${GLIBMM_VERSION}/giomm/ FILES_MATCHING PATTERN "*.h")
