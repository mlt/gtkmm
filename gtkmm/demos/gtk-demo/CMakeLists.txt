set(GTKMMDEMO_SRCS
demo-common.cc
demowindow.cc
example_appwindow.cc
example_buttonbox.cc
example_change_display.cc
example_colorsel.cc
example_dialog.cc
example_drawingarea.cc
example_flowbox.cc
example_gestures.cc
example_headerbar.cc
example_icontheme.cc
example_iconview.cc
example_images.cc
example_menus.cc
example_overlay.cc
example_panes.cc
example_pixbufs.cc
example_sizegroup.cc
example_stack.cc
example_stacksidebar.cc
example_textview.cc
example_treeview_editable_cells.cc
example_treeview_liststore.cc
example_treeview_treestore.cc
main.cc
textwidget.cc
)

add_definitions(-DHAVE_GETC_UNLOCKED -Dgetc_unlocked=getc)

add_executable(gtkmm3-demo ${GTKMMDEMO_SRCS} )

target_link_libraries(gtkmm3-demo gtkmm-${GTKMM_VERSION} gdkmm-${GTKMM_VERSION} glibmm-${GLIBMM_VERSION} giomm-${GLIBMM_VERSION} atkmm-${ATKMM_VERSION} pangomm-${PANGOMM_VERSION} sigc-${SIGC_VERSION} cairomm-${CAIROMM_VERSION} ) #gtk-${GtkApiVersion})

install(TARGETS gtkmm3-demo
LIBRARY DESTINATION "lib"
ARCHIVE DESTINATION "lib"
RUNTIME DESTINATION "bin")

install(FILES $<TARGET_PDB_FILE:gtkmm3-demo> DESTINATION "bin" CONFIGURATIONS DEBUG)

install(DIRECTORY ./ DESTINATION share/gtkmm-3.0/demo
# minimal invasion... until code fixed or patched
#DESTINATION share/gtkmm-${GTKMM_VERSION}/demo
FILES_MATCHING
PATTERN "*.cc"
PATTERN "*.h"
PATTERN "*.ui"
PATTERN "*.jpg"
PATTERN "*.png"
PATTERN "*.gif"
)
