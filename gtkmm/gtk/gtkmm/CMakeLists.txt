set(GTKMM_SRCS
aboutdialog.cc
accelgroup.cc
accelkey.cc
accellabel.cc
accelmap.cc
action.cc
actiongroup.cc
activatable.cc
adjustment.cc
alignment.cc
appchooser.cc
appchooserbutton.cc
appchooserdialog.cc
appchooserwidget.cc
arrow.cc
aspectframe.cc
assistant.cc
bin.cc
border.cc
box.cc
buildable.cc
builder.cc
button.cc
buttonbox.cc
calendar.cc
cellarea.cc
cellareabox.cc
cellareacontext.cc
celleditable.cc
celllayout.cc
cellrenderer.cc
cellrenderer_generation.cc
cellrendereraccel.cc
cellrenderercombo.cc
cellrendererpixbuf.cc
cellrendererprogress.cc
cellrendererspin.cc
cellrendererspinner.cc
cellrenderertext.cc
cellrenderertoggle.cc
cellview.cc
checkbutton.cc
checkmenuitem.cc
clipboard.cc
colorbutton.cc
colorselection.cc
combobox.cc
comboboxtext.cc
container.cc
cssprovider.cc
dialog.cc
drawingarea.cc
editable.cc
entry.cc
entrybuffer.cc
entrycompletion.cc
enums.cc
eventbox.cc
expander.cc
filechooser.cc
filechooserbutton.cc
filechooserdialog.cc
filechooserwidget.cc
filefilter.cc
fixed.cc
fontbutton.cc
fontselection.cc
frame.cc
grid.cc
handlebox.cc
iconfactory.cc
iconinfo.cc
iconset.cc
iconsource.cc
icontheme.cc
iconview.cc
image.cc
imagemenuitem.cc
infobar.cc
invisible.cc
label.cc
layout.cc
linkbutton.cc
liststore.cc
listviewtext.cc
main.cc
menu.cc
menubar.cc
menuitem.cc
menushell.cc
menutoolbutton.cc
messagedialog.cc
misc.cc
notebook.cc
numerableicon.cc
object.cc
offscreenwindow.cc
orientable.cc
pagesetup.cc
#pagesetupunixdialog.cc
paned.cc
papersize.cc
#plug.cc
printcontext.cc
#printer.cc
#printjob.cc
printoperation.cc
printoperationpreview.cc
printsettings.cc
#printunixdialog.cc
progressbar.cc
radioaction.cc
radiobutton.cc
radiobuttongroup.cc
radiomenuitem.cc
radiotoolbutton.cc
range.cc
recentaction.cc
recentchooser.cc
recentchooserdialog.cc
recentchoosermenu.cc
recentchooserwidget.cc
recentfilter.cc
recentinfo.cc
recentmanager.cc
requisition.cc
scale.cc
scalebutton.cc
scrollable.cc
scrollbar.cc
scrolledwindow.cc
selectiondata.cc
selectiondata_private.cc
separator.cc
separatormenuitem.cc
separatortoolitem.cc
settings.cc
sizegroup.cc
#socket.cc
spinbutton.cc
spinner.cc
statusbar.cc
statusicon.cc
stock.cc
stockid.cc
stockitem.cc
stylecontext.cc
styleprovider.cc
switch.cc
table.cc
targetentry.cc
targetlist.cc
tearoffmenuitem.cc
textattributes.cc
textbuffer.cc
textchildanchor.cc
textiter.cc
textmark.cc
texttag.cc
texttagtable.cc
textview.cc
toggleaction.cc
togglebutton.cc
toggletoolbutton.cc
toolbar.cc
toolbutton.cc
toolitem.cc
toolitemgroup.cc
toolpalette.cc
toolshell.cc
tooltip.cc
treedragdest.cc
treedragsource.cc
treeiter.cc
treemodel.cc
treemodelcolumn.cc
treemodelfilter.cc
treemodelsort.cc
treepath.cc
treerowreference.cc
treeselection.cc
treesortable.cc
treestore.cc
treeview.cc
treeview_private.cc
treeviewcolumn.cc
uimanager.cc
viewport.cc
volumebutton.cc
widget.cc
widgetpath.cc
window.cc
wrap_init.cc
)

add_definitions( -DGTKMM_DLL -DGTKMM_BUILD -D_WINDLL )
add_library(gtkmm-${GTKMM_VERSION} SHARED ${GTKMM_SRCS} gtkmm.def ../../${EXTRA}/gtkmm/gtkmm.rc)

add_custom_command (OUTPUT gtkmm.def
COMMAND echo Will be generated later > gtkmm.def
)
add_custom_command(TARGET gtkmm-${GTKMM_VERSION} PRE_LINK
COMMAND	gendef ${CMAKE_CURRENT_BINARY_DIR}/gtkmm.def gtkmm-${GTKMM_VERSION}${POSTFIX}.dll ${CMAKE_CURRENT_BINARY_DIR}${CMAKE_FILES_DIRECTORY}/gtkmm-${GTKMM_VERSION}.dir/*.obj
)

target_link_libraries(gtkmm-${GTKMM_VERSION} gdkmm-${GTKMM_VERSION} glibmm-${GLIBMM_VERSION} giomm-${GLIBMM_VERSION} atkmm-${ATKMM_VERSION} pangomm-${GLIBMM_VERSION} sigc-${SIGC_VERSION} cairomm-${CAIROMM_VERSION} gtk-${GtkApiVersion})

install(TARGETS gtkmm-${GTKMM_VERSION}
LIBRARY DESTINATION "lib"
ARCHIVE DESTINATION "lib"
RUNTIME DESTINATION "bin")

install(FILES ${CMAKE_CURRENT_BINARY_DIR}/gtkmm-${GTKMM_VERSION}${POSTFIX}.pdb DESTINATION "bin" CONFIGURATIONS DEBUG)

install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/../../${EXTRA}/gtkmm/gtkmmconfig.h DESTINATION "lib/gtkmm-${GTKMM_VERSION}/include")

install(DIRECTORY ../ DESTINATION include/gtkmm-${GTKMM_VERSION}/ FILES_MATCHING PATTERN "*.h"
PATTERN "src" EXCLUDE
PATTERN "private" EXCLUDE
PATTERN "PaxHeaders*" EXCLUDE
)
#install(DIRECTORY ./ DESTINATION include/gtkmm-${GTKMM_VERSION}/gtkmm/ FILES_MATCHING PATTERN "*.h")
