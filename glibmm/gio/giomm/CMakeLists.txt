set(GIOMM_SRCS
action.cc
actiongroup.cc
actionmap.cc
appinfo.cc
applaunchcontext.cc
application.cc
applicationcommandline.cc
asyncinitable.cc
asyncresult.cc
bufferedinputstream.cc
bufferedoutputstream.cc
cancellable.cc
charsetconverter.cc
contenttype.cc
converter.cc
converterinputstream.cc
converteroutputstream.cc
credentials.cc
datainputstream.cc
dataoutputstream.cc
dbusactiongroup.cc
dbusaddress.cc
dbusauthobserver.cc
dbusconnection.cc
dbuserror.cc
dbuserrorutils.cc
dbusinterface.cc
dbusinterfaceskeleton.cc
dbusinterfacevtable.cc
dbusintrospection.cc
dbusmenumodel.cc
dbusmessage.cc
dbusmethodinvocation.cc
dbusobject.cc
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
menu.cc
menuattributeiter.cc
menuitem.cc
menulinkiter.cc
menumodel.cc
mount.cc
mountoperation.cc
networkaddress.cc
networkservice.cc
notification.cc
outputstream.cc
permission.cc
pollableinputstream.cc
pollableoutputstream.cc
proxy.cc
proxyaddress.cc
proxyresolver.cc
remoteactiongroup.cc
resolver.cc
resource.cc
seekable.cc
settings.cc
simpleaction.cc
simpleactiongroup.cc
simplepermission.cc
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
socketsource.cc
srvtarget.cc
tcpconnection.cc
tcpwrapperconnection.cc
themedicon.cc
threadedsocketservice.cc
tlscertificate.cc
tlsclientconnection.cc
tlsconnection.cc
tlsdatabase.cc
tlsinteraction.cc
tlspassword.cc
tlsserverconnection.cc
volume.cc
volumemonitor.cc
wrap_init.cc
zlibcompressor.cc
zlibdecompressor.cc
)

add_definitions( -DGIOMM_DLL -DGIOMM_BUILD -D_WINDLL -DG_HAVE_ISO_VARARGS )
add_library(giomm-${GLIBMM_VERSION} SHARED ${GIOMM_SRCS} ../../${EXTRA}/giomm/giomm.rc)
target_link_libraries(giomm-${GLIBMM_VERSION} glib-2.0.dll gobject-2.0.dll gmodule-2.0.dll
gio-2.0.dll sigc-${SIGC_VERSION} glibmm-${GLIBMM_VERSION})

install(TARGETS giomm-${GLIBMM_VERSION}
LIBRARY DESTINATION "lib"
ARCHIVE DESTINATION "lib"
RUNTIME DESTINATION "bin")

install(FILES $<TARGET_PDB_FILE:giomm-${GLIBMM_VERSION}> DESTINATION "bin" CONFIGURATIONS DEBUG)

install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/../../${EXTRA}/giomm/giommconfig.h DESTINATION "lib/giomm-${GLIBMM_VERSION}/include")

install(DIRECTORY ../ DESTINATION include/giomm-${GLIBMM_VERSION}/ FILES_MATCHING PATTERN "*.h"
PATTERN "PaxHeaders*" EXCLUDE
)
#install(DIRECTORY ./ DESTINATION include/giomm-${GLIBMM_VERSION}/giomm/ FILES_MATCHING PATTERN "*.h")
