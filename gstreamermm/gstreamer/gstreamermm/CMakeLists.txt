include_directories(
     ${GlibEtcInstallRoot}/include/gstreamer-1.0
     ${GlibEtcInstallRoot}/include/libxml2
     ${CMAKE_SOURCE_DIR}/${XMLMM_DIR}
     ${CMAKE_SOURCE_DIR}/${XMLMM_DIR}/${EXTRA}/libxml++
     ..
)

add_definitions(-DLIBXMLPP_BUILD -DGSTREAMERMM_BUILD -D_WINDLL -DGLIBMM_DLL -DGLIBMM_MSC)

set(GSTREAMERMM_SRCS
adder.cc
allocator.cc
alsasink.cc
alsasrc.cc
appsink.cc
appsrc.cc
audiobasesink.cc
audiobasesrc.cc
audioclock.cc
audioconvert.cc
audiofilter.cc
audioformat.cc
audioinfo.cc
audiorate.cc
audioringbuffer.cc
audiosink.cc
audiosrc.cc
audiotestsrc.cc
basesink.cc
basesrc.cc
basetransform.cc
bin.cc
buffer.cc
bufferlist.cc
bus.cc
caps.cc
capsfeatures.cc
capsfilter.cc
cdparanoiasrc.cc
childproxy.cc
clock.cc
clockoverlay.cc
colorbalance.cc
colorbalancechannel.cc
context.cc
decodebin.cc
discoverer.cc
discovererinfo.cc
element.cc
elementfactory.cc
enums.cc
error.cc
event.cc
fakesink.cc
fakesrc.cc
fdsink.cc
fdsrc.cc
filesink.cc
filesrc.cc
format.cc
funnel.cc
ghostpad.cc
giosink.cc
giosrc.cc
giostreamsink.cc
giostreamsrc.cc
handle_error.cc
identity.cc
init.cc
inputselector.cc
iterator.cc
mapinfo.cc
memory.cc
message.cc
miniobject.cc
multiqueue.cc
navigation.cc
object.cc
oggdemux.cc
oggmux.cc
outputselector.cc
pad.cc
padtemplate.cc
parse.cc
pipeline.cc
playbin.cc
plugin.cc
pluginfeature.cc
preset.cc
pushsrc.cc
query.cc
queue.cc
queue2.cc
registry.cc
sample.cc
segment.cc
streamvolume.cc
structure.cc
subtitleoverlay.cc
systemclock.cc
taglist.cc
tagsetter.cc
task.cc
taskpool.cc
tcpclientsink.cc
tcpclientsrc.cc
tcpserversrc.cc
tee.cc
textoverlay.cc
textrender.cc
theoradec.cc
theoraenc.cc
theoraparse.cc
timeoverlay.cc
typefind.cc
typefindelement.cc
typefindfactory.cc
uridecodebin.cc
urihandler.cc
valve.cc
value.cc
version.cc
videoorientation.cc
videooverlay.cc
videorate.cc
videoscale.cc
videosink.cc
videotestsrc.cc
vorbisdec.cc
vorbisenc.cc
vorbisparse.cc
vorbistag.cc
wrap_init.cc
ximagesink.cc
)

add_library(gstreamermm-${GSTREAMERMM_VERSION} SHARED ${GSTREAMERMM_SRCS} gstreamermm.def)

add_custom_command (OUTPUT gstreamermm.def
COMMAND ECHO Will be generated later > gstreamermm.def
)
add_custom_command(TARGET gstreamermm-${GSTREAMERMM_VERSION} PRE_LINK
COMMAND	gendef ${CMAKE_CURRENT_BINARY_DIR}/gstreamermm.def $<TARGET_FILE_NAME:gstreamermm-${GSTREAMERMM_VERSION}> ${CMAKE_CURRENT_BINARY_DIR}/$<$<BOOL:${CMAKE_BUILD_TYPE}>:${CMAKE_FILES_DIRECTORY}>/gstreamermm-${GSTREAMERMM_VERSION}.dir/${CMAKE_CFG_INTDIR}/*.obj
)

target_link_libraries(gstreamermm-${GSTREAMERMM_VERSION} gstreamer-1.0 sigc-${SIGC_VERSION} glibmm-${GLIBMM_VERSION} xmlpp-${XMLMM_VERSION} gstaudio-1.0 gstbase-1.0 gstvideo-1.0 gstpbutils-1.0) #glibmm-${GLIBMM_VERSION} giomm-${GLIBMM_VERSION}

install(TARGETS gstreamermm-${GSTREAMERMM_VERSION}
LIBRARY DESTINATION "lib"
ARCHIVE DESTINATION "lib"
RUNTIME DESTINATION "bin")

install(FILES $<TARGET_PDB_FILE:gstreamermm-${GSTREAMERMM_VERSION}> DESTINATION "bin" CONFIGURATIONS DEBUG)

install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/../gstreamermmconfig.h DESTINATION "lib/gstreamermm-${GSTREAMERMM_VERSION}/include")

install(DIRECTORY ../ DESTINATION include/gstreamermm-${GSTREAMERMM_VERSION}/ FILES_MATCHING PATTERN "*.h"
PATTERN "src" EXCLUDE
PATTERN "private" EXCLUDE
PATTERN "PaxHeaders*" EXCLUDE
)
