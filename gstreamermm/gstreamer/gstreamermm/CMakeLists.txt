include_directories(
     ${GlibEtcInstallRoot}/include/gstreamer-0.10
     ${GlibEtcInstallRoot}/include/libxml2
     ${CMAKE_SOURCE_DIR}/${XMLMM_DIR}
     ${CMAKE_SOURCE_DIR}/${XMLMM_DIR}/${EXTRA}/libxml++
     ..
)

add_definitions(-DLIBXMLPP_BUILD -DGSTREAMERMM_BUILD -D_WINDLL -DGLIBMM_DLL -DGLIBMM_MSC -DG_HAVE_ISO_VARARGS "-DGST_MINI_OBJECT_FLAG_RESERVED1=(1<<1)")

set(GSTREAMERMM_SRCS
adder.cc
alsamixer.cc
alsasink.cc
alsasrc.cc
audioclock.cc
audioconvert.cc
audiofilter.cc
audiorate.cc
audioresample.cc
audiosink.cc
audiosrc.cc
audiotestsrc.cc
baseaudiosink.cc
baseaudiosrc.cc
basesink.cc
basesrc.cc
basetransform.cc
bin.cc
buffer.cc
bufferlist.cc
bus.cc
caps.cc
capsfilter.cc
cddabasesrc.cc
cdparanoiasrc.cc
childproxy.cc
clock.cc
clockoverlay.cc
colorbalance.cc
colorbalancechannel.cc
decodebin.cc
decodebin2.cc
element.cc
elementfactory.cc
enums.cc
error.cc
event.cc
fakesink.cc
fakesrc.cc
fdsink.cc
fdsrc.cc
ffmpegcolorspace.cc
filesink.cc
filesrc.cc
filter.cc
format.cc
gdpdepay.cc
gdppay.cc
ghostpad.cc
giosink.cc
giosrc.cc
giostreamsink.cc
giostreamsrc.cc
gst_wrap_init.cc
handle_error.cc
identity.cc
index.cc
indexfactory.cc
init.cc
interface.cc
iterator.cc
message.cc
miniobject.cc
mixer.cc
mixeroptions.cc
mixertrack.cc
multifdsink.cc
multiqueue.cc
navigation.cc
object.cc
oggdemux.cc
oggmux.cc
pad.cc
padtemplate.cc
parse.cc
pipeline.cc
playbin.cc
playbin2.cc
plugin.cc
pluginfeature.cc
preset.cc
propertyprobe.cc
pushsrc.cc
query.cc
queue.cc
queue2.cc
registry.cc
ringbuffer.cc
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
tcpserversink.cc
tcpserversrc.cc
tee.cc
textoverlay.cc
textrender.cc
theoradec.cc
theoraenc.cc
theoraparse.cc
timeoverlay.cc
tuner.cc
tunerchannel.cc
tunernorm.cc
typefind.cc
typefindelement.cc
typefindfactory.cc
uridecodebin.cc
urihandler.cc
value.cc
version.cc
videoorientation.cc
videorate.cc
videoscale.cc
videosink.cc
videotestsrc.cc
volume.cc
vorbisdec.cc
vorbisenc.cc
vorbisparse.cc
vorbistag.cc
wrap.cc
wrap_init.cc
ximagesink.cc
xml.cc
xoverlay.cc
xvimagesink.cc
)

add_library(gstreamermm-${GSTREAMERMM_VERSION} SHARED ${GSTREAMERMM_SRCS} gstreamermm.def)

add_custom_command (OUTPUT gstreamermm.def
COMMAND ECHO Will be generated later > gstreamermm.def
)
add_custom_command(TARGET gstreamermm-${GSTREAMERMM_VERSION} PRE_LINK
COMMAND	gendef ${CMAKE_CURRENT_BINARY_DIR}/gstreamermm.def gstreamermm-${GSTREAMERMM_VERSION}${POSTFIX}.dll ${CMAKE_CURRENT_BINARY_DIR}${CMAKE_FILES_DIRECTORY}/gstreamermm-${GSTREAMERMM_VERSION}.dir/*.obj
)

target_link_libraries(gstreamermm-${GSTREAMERMM_VERSION} gstreamer-0.10.lib sigc-${SIGC_VERSION} gstinterfaces-0.10.lib glibmm-${GLIBMM_VERSION} xmlpp-${XMLMM_VERSION} gstaudio-0.10.lib gstbase-0.10.lib gstcdda-0.10.lib gstvideo-0.10.lib ) #glibmm-${GLIBMM_VERSION} giomm-${GLIBMM_VERSION}

install(TARGETS gstreamermm-${GSTREAMERMM_VERSION}
LIBRARY DESTINATION "lib"
ARCHIVE DESTINATION "lib"
RUNTIME DESTINATION "bin")

install(FILES ${CMAKE_CURRENT_BINARY_DIR}/gstreamermm-${GSTREAMERMM_VERSION}${POSTFIX}.pdb DESTINATION "bin" CONFIGURATIONS DEBUG)

install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/../gstreamermmconfig.h DESTINATION "lib/gstreamermm-${GSTREAMERMM_VERSION}/include")

install(DIRECTORY ../ DESTINATION include/gstreamermm-${GSTREAMERMM_VERSION}/ FILES_MATCHING PATTERN "*.h"
PATTERN "src" EXCLUDE
PATTERN "private" EXCLUDE
PATTERN "PaxHeaders*" EXCLUDE
)
