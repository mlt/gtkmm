set (DEMOS
appwindow.c		
assistant.c		
builder.c		
button_box.c		
changedisplay.c		
clipboard.c		
colorsel.c		
combobox.c		
dialog.c		
drawingarea.c		
editable_cells.c	
entry_buffer.c		
entry_completion.c	
expander.c  		
hypertext.c		
iconview.c		
iconview_edit.c		
images.c		
infobar.c		
links.c			
list_store.c		
menus.c			
offscreen_window.c	
offscreen_window2.c	
panes.c			
pickers.c		
pixbufs.c		
printing.c		
rotated_text.c		
search_entry.c		
sizegroup.c		
spinner.c		
stock_browser.c		
textview.c		
textscroll.c		
toolpalette.c		
tree_store.c		
ui_manager.c
)

set ( GTK_DEMO_SRCS
${DEMOS}
demo-common.h
main.c	
demos.h
)

configure_file(geninclude.pl.in ${CMAKE_CURRENT_SOURCE_DIR}/geninclude.pl)

add_custom_command(OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/demos.h
COMMAND	${PERL} geninclude.pl ${DEMOS} > demos.h
WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
)

add_executable (gtk3-demo ${GTK_DEMO_SRCS})

target_link_libraries (gtk3-demo gtk-${GtkApiVersion} libmsvcrt)

install(TARGETS gtk3-demo
LIBRARY DESTINATION "lib"
RUNTIME DESTINATION "bin")

install(FILES ${CMAKE_CURRENT_BINARY_DIR}/gtk3-demo.pdb DESTINATION "bin" CONFIGURATIONS DEBUG)

install(DIRECTORY ./ DESTINATION share/gtk-2.4/demo
# minimal invasion... until code fixed or patched
#DESTINATION share/gtk-${GtkApiVersion}/demo
FILES_MATCHING
PATTERN "*.c"
PATTERN "*.h"
PATTERN "*.ui"
PATTERN "*.jpg"
PATTERN "*.png"
PATTERN "*.gif"
)
