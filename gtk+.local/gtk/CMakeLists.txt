if (MSVC80)
set (GTK_HOST "i686-pc-vc80")
elseif(MSVC90)
set (GTK_HOST "i686-pc-vc90")
elseif(MSVC10)
set (GTK_HOST "i686-pc-vc100")
endif (MSVC80)

add_definitions ( -DGTK_COMPILATION -DG_LOG_DOMAIN="Gtk"
-DGTK_HOST="${GTK_HOST}" -DGTK_PRINT_BACKENDS="file"
-DGTK_PRINT_PREVIEW_COMMAND="undefined-gtk-print-preview-command"
-DGTK_LIBDIR="/dummy/lib" -DGTK_DATADIR="/dummy/share"
-DGTK_DATA_PREFIX="/dummy" -DGTK_SYSCONFDIR="/dummy/etc"
-DVERSION="${GtkApiVersion}"
-DGTK_BINARY_VERSION="${GtkBinaryVersion}"
)

add_definitions( "-Dround=(int)" ) # round() is absent in math.h @ MS VC++

set ( GTK_SRCS
fnmatch.c
gen-paper-names.c
gtk.h
gtkaboutdialog.c
gtkaboutdialog.h
gtkaccelgroup.c
gtkaccelgroup.h
gtkaccelgroupprivate.h
gtkaccellabel.c
gtkaccellabel.h
gtkaccelmap.c
gtkaccelmap.h
gtkaccessible.c
gtkaccessible.h
gtkaction.c
gtkaction.h
gtkactiongroup.c
gtkactiongroup.h
gtkactivatable.c
gtkactivatable.h
gtkadjustment.c
gtkadjustment.h
gtkalignment.c
gtkalignment.h
gtkanimationdescription.c
gtkanimationdescription.h
gtkappchooser.c
gtkappchooser.h
gtkappchooserbutton.c
gtkappchooserbutton.h
gtkappchooserdialog.c
gtkappchooserdialog.h
gtkappchoosermodule.c
gtkappchoosermodule.h
gtkappchooseronline.c
gtkappchooseronline.h
gtkappchooseronlinepk.c
gtkappchooseronlinepk.h
gtkappchooserprivate.h
gtkappchooserwidget.c
gtkappchooserwidget.h
gtkapplication.c
gtkapplication.h
gtkarrow.c
gtkarrow.h
gtkaspectframe.c
gtkaspectframe.h
gtkassistant.c
gtkassistant.h
gtkbbox.c
gtkbbox.h
gtkbin.c
gtkbin.h
gtkbindings.c
gtkbindings.h
gtkbindingsprivate.h
gtkborder.c
gtkborder.h
gtkborderimage.c
gtkbox.c
gtkbox.h
gtkbuildable.c
gtkbuildable.h
gtkbuilder.c
gtkbuilder.h
gtkbuilderparser.c
gtkbuilderprivate.h
gtkbuiltincache.h
gtkbutton.c
gtkbutton.h
gtkbuttonprivate.h
gtkcalendar.c
gtkcalendar.h
gtkcellarea.c
gtkcellarea.h
gtkcellareabox.c
gtkcellareabox.h
gtkcellareaboxcontext.c
gtkcellareaboxcontextprivate.h
gtkcellareacontext.c
gtkcellareacontext.h
gtkcelleditable.c
gtkcelleditable.h
gtkcelllayout.c
gtkcelllayout.h
gtkcellrenderer.c
gtkcellrenderer.h
gtkcellrendereraccel.c
gtkcellrendereraccel.h
gtkcellrenderercombo.c
gtkcellrenderercombo.h
gtkcellrendererpixbuf.c
gtkcellrendererpixbuf.h
gtkcellrendererprogress.c
gtkcellrendererprogress.h
gtkcellrendererspin.c
gtkcellrendererspin.h
gtkcellrendererspinner.c
gtkcellrendererspinner.h
gtkcellrenderertext.c
gtkcellrenderertext.h
gtkcellrenderertoggle.c
gtkcellrenderertoggle.h
gtkcellview.c
gtkcellview.h
gtkcheckbutton.c
gtkcheckbutton.h
gtkcheckmenuitem.c
gtkcheckmenuitem.h
gtkclipboard.c
gtkclipboard.h
gtkcolorbutton.c
gtkcolorbutton.h
gtkcolorsel.c
gtkcolorsel.h
gtkcolorseldialog.c
gtkcolorseldialog.h
gtkcombobox.c
gtkcombobox.h
gtkcomboboxtext.c
gtkcomboboxtext.h
gtkcontainer.c
gtkcontainer.h
gtkcssparser.c
gtkcssprovider.c
gtkcssprovider.h
gtkcssproviderprivate.h
gtkcssselector.c
#gtkcssstringfuncs.c
gtkcsstypes.c
gtkdebug.h
gtkdialog.c
gtkdialog.h
gtkdnd.c
gtkdnd.h
gtkdndcursors.h
gtkdrawingarea.c
gtkdrawingarea.h
gtkeditable.c
gtkeditable.h
gtkentry.c
gtkentry.h
gtkentrybuffer.c
gtkentrybuffer.h
gtkentrycompletion.c
gtkentrycompletion.h
gtkentryprivate.h
gtkenums.h
gtkeventbox.c
gtkeventbox.h
gtkexpander.c
gtkexpander.h
gtkfilechooser.c
gtkfilechooser.h
gtkfilechooserbutton.c
gtkfilechooserbutton.h
gtkfilechooserdefault.c
gtkfilechooserdefault.h
gtkfilechooserdialog.c
gtkfilechooserdialog.h
gtkfilechooserembed.c
gtkfilechooserembed.h
gtkfilechooserentry.c
gtkfilechooserentry.h
gtkfilechooserprivate.h
gtkfilechooserutils.c
gtkfilechooserutils.h
gtkfilechooserwidget.c
gtkfilechooserwidget.h
gtkfilefilter.c
gtkfilefilter.h
gtkfilesystem.c
gtkfilesystem.h
gtkfilesystemmodel.c
gtkfilesystemmodel.h
gtkfixed.c
gtkfixed.h
gtkfontbutton.c
gtkfontbutton.h
gtkfontsel.c
gtkfontsel.h
gtkframe.c
gtkframe.h
gtkgradient.c
gtkgradient.h
gtkgrid.c
gtkgrid.h
gtkhandlebox.c
gtkhandlebox.h
gtkhbbox.c
gtkhbbox.h
gtkhbox.c
gtkhbox.h
gtkhpaned.c
gtkhpaned.h
gtkhscale.c
gtkhscale.h
gtkhscrollbar.c
gtkhscrollbar.h
gtkhseparator.c
gtkhseparator.h
gtkhsv.c
gtkhsv.h
gtkiconcache.c
gtkiconcache.h
gtkiconcachevalidator.c
gtkiconcachevalidator.h
gtkiconfactory.c
gtkiconfactory.h
gtkicontheme.c
gtkicontheme.h
gtkiconview.c
gtkiconview.h
gtkimage.c
gtkimage.h
gtkimagemenuitem.c
gtkimagemenuitem.h
gtkimageprivate.h
gtkimcontext.c
gtkimcontext.h
gtkimcontextsimple.c
gtkimcontextsimple.h
gtkimcontextsimpleseqs.h
gtkimmodule.c
gtkimmodule.h
gtkimmulticontext.c
gtkimmulticontext.h
gtkinfobar.c
gtkinfobar.h
gtkintl.h
gtkinvisible.c
gtkinvisible.h
gtkkeyhash.c
gtkkeyhash.h
gtklabel.c
gtklabel.h
gtklayout.c
gtklayout.h
gtklinkbutton.c
gtklinkbutton.h
gtkliststore.c
gtkliststore.h
gtklockbutton.c
gtkmain.c
gtkmain.h
gtkmainprivate.h
gtkmarshalers.c
gtkmarshalers.h
gtkmenu.c
gtkmenu.h
gtkmenubar.c
gtkmenubar.h
gtkmenuitem.c
gtkmenuitem.h
gtkmenuitemprivate.h
gtkmenuprivate.h
gtkmenushell.c
gtkmenushell.h
gtkmenushellprivate.h
gtkmenutoolbutton.c
gtkmenutoolbutton.h
gtkmessagedialog.c
gtkmessagedialog.h
gtkmisc.c
gtkmisc.h
gtkmnemonichash.c
gtkmnemonichash.h
gtkmodifierstyle.c
gtkmodifierstyle.h
gtkmodules.c
gtkmodules.h
gtkmountoperation.c
gtkmountoperation.h
gtkmountoperation-stub.c
gtkmountoperationprivate.h
gtknotebook.c
gtknotebook.h
gtknumerableicon.c
gtknumerableicon.h
gtknumerableiconprivate.h
gtkoffscreenwindow.c
gtkoffscreenwindow.h
gtkorientable.c
gtkorientable.h
gtkorientableprivate.h
gtkpagesetup.c
gtkpagesetup.h
gtkpaned.c
gtkpaned.h
gtkpango.c
gtkpango.h
gtkpapersize.c
gtkpapersize.h
gtkpathbar.c
gtkpathbar.h
gtkprint-win32.c
gtkprint-win32.h
gtkprintcontext.c
gtkprintcontext.h
gtkprintoperation.c
gtkprintoperation.h
gtkprintoperation-private.h
gtkprintoperation-win32.c
gtkprintoperationpreview.c
gtkprintoperationpreview.h
gtkprintsettings.c
gtkprintsettings.h
gtkprintutils.c
gtkprintutils.h
gtkprivate.h
gtkprogressbar.c
gtkprogressbar.h
gtkquery.c
gtkquery.h
gtkradioaction.c
gtkradioaction.h
gtkradiobutton.c
gtkradiobutton.h
gtkradiomenuitem.c
gtkradiomenuitem.h
gtkradiotoolbutton.c
gtkradiotoolbutton.h
gtkrange.c
gtkrange.h
gtkrbtree.c
gtkrbtree.h
gtkrc.c
gtkrc.h
gtkrecentaction.c
gtkrecentaction.h
gtkrecentchooser.c
gtkrecentchooser.h
gtkrecentchooserdefault.c
gtkrecentchooserdefault.h
gtkrecentchooserdialog.c
gtkrecentchooserdialog.h
gtkrecentchoosermenu.c
gtkrecentchoosermenu.h
gtkrecentchooserprivate.h
gtkrecentchooserutils.c
gtkrecentchooserutils.h
gtkrecentchooserwidget.c
gtkrecentchooserwidget.h
gtkrecentfilter.c
gtkrecentfilter.h
gtkrecentmanager.c
gtkrecentmanager.h
gtkroundedbox.c
gtkscale.c
gtkscale.h
gtkscalebutton.c
gtkscalebutton.h
gtkscaleprivate.h
gtkscrollable.c
gtkscrollable.h
gtkscrollbar.c
gtkscrollbar.h
gtkscrolledwindow.c
gtkscrolledwindow.h
gtksearchengine.c
gtksearchengine.h
gtksearchenginebeagle.c
gtksearchenginebeagle.h
gtksearchenginesimple.c
gtksearchenginesimple.h
gtksearchenginetracker.c
gtksearchenginetracker.h
gtkselection.c
gtkselection.h
gtkselectionprivate.h
gtkseparator.c
gtkseparator.h
gtkseparatormenuitem.c
gtkseparatormenuitem.h
gtkseparatortoolitem.c
gtkseparatortoolitem.h
gtksettings.c
gtksettings.h
gtksettingsprivate.h
gtkshadow.c
gtkshow.c
gtkshow.h
gtksizegroup.c
gtksizegroup.h
gtksizegroup-private.h
gtksizerequest.c
gtksizerequest.h
gtkspinbutton.c
gtkspinbutton.h
gtkspinner.c
gtkspinner.h
gtkstatusbar.c
gtkstatusbar.h
gtkstatusicon.c
gtkstatusicon.h
gtkstock.c
gtkstock.h
gtkstyle.c
gtkstyle.h
gtkstylecontext.c
gtkstylecontext.h
gtkstylecontextprivate.h
gtkstyleproperties.c
gtkstyleproperties.h
gtkstyleproperty.c
gtkstyleprovider.c
gtkstyleprovider.h
gtkswitch.c
gtkswitch.h
gtksymboliccolor.c
gtksymboliccolor.h
gtktable.c
gtktable.h
gtktearoffmenuitem.c
gtktearoffmenuitem.h
gtktestutils.c
gtktestutils.h
gtktextattributes.c
gtktextattributes.h
gtktextbtree.c
gtktextbtree.h
gtktextbuffer.c
gtktextbuffer.h
gtktextbufferrichtext.c
gtktextbufferrichtext.h
gtktextbufferserialize.c
gtktextbufferserialize.h
gtktextchild.c
gtktextchild.h
gtktextchildprivate.h
gtktextdisplay.c
gtktextdisplay.h
gtktextiter.c
gtktextiter.h
gtktextiterprivate.h
gtktextlayout.c
gtktextlayout.h
gtktextmark.c
gtktextmark.h
gtktextmarkprivate.h
gtktextsegment.c
gtktextsegment.h
gtktexttag.c
gtktexttag.h
gtktexttagprivate.h
gtktexttagtable.c
gtktexttagtable.h
gtktexttypes.c
gtktexttypes.h
gtktextutil.c
gtktextutil.h
gtktextview.c
gtktextview.h
gtkthemingengine.c
gtkthemingengine.h
gtktimeline.c
gtktimeline.h
gtktoggleaction.c
gtktoggleaction.h
gtktogglebutton.c
gtktogglebutton.h
gtktoggletoolbutton.c
gtktoggletoolbutton.h
gtktoolbar.c
gtktoolbar.h
gtktoolbutton.c
gtktoolbutton.h
gtktoolitem.c
gtktoolitem.h
gtktoolitemgroup.c
gtktoolitemgroup.h
gtktoolpalette.c
gtktoolpalette.h
gtktoolpaletteprivate.h
gtktoolshell.c
gtktoolshell.h
gtktooltip.c
gtktooltip.h
gtktrayicon.h
gtktreedatalist.c
gtktreedatalist.h
gtktreednd.c
gtktreednd.h
gtktreemenu.c
gtktreemenu.h
gtktreemodel.c
gtktreemodel.h
gtktreemodelfilter.c
gtktreemodelfilter.h
gtktreemodelsort.c
gtktreemodelsort.h
gtktreeprivate.h
gtktreeselection.c
gtktreeselection.h
gtktreesortable.c
gtktreesortable.h
gtktreestore.c
gtktreestore.h
gtktreeview.c
gtktreeview.h
gtktreeviewcolumn.c
gtktreeviewcolumn.h
gtktypebuiltins.c
gtktypebuiltins.h
gtkuimanager.c
gtkuimanager.h
gtkvbbox.c
gtkvbbox.h
gtkvbox.c
gtkvbox.h
gtkversion.h
gtkviewport.c
gtkviewport.h
gtkvolumebutton.c
gtkvolumebutton.h
gtkvpaned.c
gtkvpaned.h
gtkvscale.c
gtkvscale.h
gtkvscrollbar.c
gtkvscrollbar.h
gtkvseparator.c
gtkvseparator.h
gtkwidget.c
gtkwidget.h
gtkwidgetpath.c
gtkwidgetpath.h
gtkwidgetprivate.h
gtkwin32embed.c
gtkwin32embed.h
gtkwin32embedwidget.c
gtkwin32embedwidget.h
gtkwindow.c
gtkwindow.h
gtkwindowprivate.h
gtktypefuncs.c
)


set(gtk_public_h_sources 
gtk.h			
gtkx.h			
gtkaboutdialog.h	
gtkaccelgroup.h		
gtkaccellabel.h		
gtkaccelmap.h		
gtkaccessible.h		
gtkaction.h		
gtkactiongroup.h	
gtkactivatable.h	
gtkadjustment.h		
gtkalignment.h		
gtkappchooser.h		
gtkappchooserbutton.h	
gtkappchooserdialog.h	
gtkappchooserwidget.h	
gtkapplication.h	
gtkarrow.h		
gtkaspectframe.h	
gtkassistant.h		
gtkbbox.h		
gtkbin.h		
gtkbindings.h		
gtkborder.h		
gtkbox.h		
gtkbuilder.h		
gtkbuildable.h		
gtkbutton.h		
gtkcalendar.h		
gtkcellarea.h		
gtkcellareacontext.h	
gtkcellareabox.h	
gtkcelleditable.h	
gtkcelllayout.h		
gtkcellrenderer.h	
gtkcellrendereraccel.h	
gtkcellrenderercombo.h	
gtkcellrendererpixbuf.h	
gtkcellrendererprogress.h 
gtkcellrendererspin.h	
gtkcellrendererspinner.h
gtkcellrenderertext.h	
gtkcellrenderertoggle.h	
gtkcellview.h		
gtkcheckbutton.h	
gtkcheckmenuitem.h	
gtkclipboard.h		
gtkcolorbutton.h	
gtkcolorsel.h		
gtkcolorseldialog.h	
gtkcombobox.h		
gtkcomboboxtext.h	
gtkcontainer.h		
gtkcssprovider.h	
gtkdebug.h		
gtkdialog.h		
gtkdnd.h		
gtkdrawingarea.h	
gtkeditable.h		
gtkentry.h		
gtkentrybuffer.h	
gtkentrycompletion.h	
gtkenums.h		
gtkeventbox.h		
gtkexpander.h		
gtkfilechooser.h	
gtkfilechooserbutton.h	
gtkfilechooserdialog.h	
gtkfilechooserwidget.h	
gtkfilefilter.h		
gtkfixed.h		
gtkfontbutton.h		
gtkfontsel.h		
gtkframe.h		
gtkgradient.h		
gtkgrid.h		
gtkhandlebox.h		
gtkhbbox.h		
gtkhbox.h		
gtkhpaned.h		
gtkhscale.h		
gtkhscrollbar.h		
gtkhseparator.h		
gtkhsv.h		
gtkiconfactory.h	
gtkicontheme.h		
gtkiconview.h		
gtkimage.h		
gtkimagemenuitem.h	
gtkimcontext.h		
gtkimcontextsimple.h	
gtkimmodule.h		
gtkimmulticontext.h	
gtkinfobar.h		
gtkinvisible.h		
gtklabel.h		
gtklayout.h		
gtklinkbutton.h		
gtkliststore.h		
gtkmain.h		
gtkmenu.h		
gtkmenubar.h		
gtkmenuitem.h		
gtkmenushell.h		
gtkmenutoolbutton.h	
gtkmessagedialog.h	
gtkmisc.h		
gtkmodules.h		
gtkmountoperation.h	
gtknotebook.h		
gtknumerableicon.h	
gtkoffscreenwindow.h	
gtkorientable.h		
gtkpagesetup.h		
gtkpaned.h		
gtkpapersize.h		
gtkplug.h		
gtkprintcontext.h	
gtkprintoperation.h	
gtkprintoperationpreview.h 
gtkprintsettings.h	
gtkprogressbar.h	
gtkradioaction.h	
gtkradiobutton.h	
gtkradiomenuitem.h	
gtkradiotoolbutton.h	
gtkrange.h		
gtkrc.h			
gtkrecentaction.h	
gtkrecentchooser.h	
gtkrecentchooserdialog.h
gtkrecentchoosermenu.h	
gtkrecentchooserwidget.h
gtkrecentfilter.h	
gtkrecentmanager.h	
gtkscale.h		
gtkscalebutton.h	
gtkscrollable.h		
gtkscrollbar.h		
gtkscrolledwindow.h	
gtkselection.h		
gtkseparator.h		
gtkseparatormenuitem.h	
gtkseparatortoolitem.h	
gtksettings.h		
gtkshow.h		
gtksizegroup.h		
gtksizerequest.h	
gtksocket.h		
gtkspinbutton.h		
gtkspinner.h		
gtkstatusbar.h		
gtkstatusicon.h		
gtkstock.h		
gtkstylecontext.h	
gtkstyleproperties.h	
gtkstyleprovider.h	
gtkstyle.h		
gtkswitch.h		
gtksymboliccolor.h	
gtktable.h		
gtktearoffmenuitem.h	
gtktestutils.h		
gtktextattributes.h	
gtktextbuffer.h		
gtktextbufferrichtext.h	
gtktextchild.h		
gtktextdisplay.h	
gtktextiter.h		
gtktextmark.h		
gtktexttag.h		
gtktexttagtable.h	
gtktextview.h		
gtkthemingengine.h	
gtktoggleaction.h	
gtktogglebutton.h	
gtktoggletoolbutton.h	
gtktoolbar.h		
gtktoolbutton.h		
gtktoolitem.h		
gtktoolitemgroup.h	
gtktoolpalette.h	
gtktoolshell.h		
gtktooltip.h		
gtktreednd.h		
gtktreemodel.h		
gtktreemodelfilter.h	
gtktreemodelsort.h	
gtktreeselection.h	
gtktreesortable.h	
gtktreestore.h		
gtktreeview.h		
gtktreeviewcolumn.h	
gtkuimanager.h		
gtkvbbox.h		
gtkvbox.h		
gtkviewport.h		
gtkvolumebutton.h	
gtkvpaned.h		
gtkvscale.h		
gtkvscrollbar.h		
gtkvseparator.h		
gtkwidget.h		
gtkwidgetpath.h		
gtkwindow.h
)

add_custom_command (OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/gtk.def
COMMAND echo EXPORTS > gtk.def
COMMAND cl /EP -DG_OS_WIN32 -DGDK_WINDOWING_WIN32 -DG_GNUC_MALLOC= -DG_GNUC_CONST= -DG_GNUC_NULL_TERMINATED= -DG_GNUC_NORETURN=
		"-DG_GNUC_PRINTF=;G_GNUC_PRINTF" gtk.symbols >> gtk.def
#COMMAND nmake -f makefile.msc gtk.def
WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
)

# Workaround for command line length
#file(REMOVE ${CMAKE_CURRENT_SOURCE_DIR}/tmp)
#foreach( ff ${gtk_public_h_sources} )
#file(READ ${ff} cont)
#file(APPEND ${CMAKE_CURRENT_SOURCE_DIR}/tmp ${cont})
#endforeach(ff)

add_custom_command (OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/gtktypebuiltins.h ${CMAKE_CURRENT_SOURCE_DIR}/gtktypebuiltins.c
COMMAND	echo \#ifndef __GTK_TYPE_BUILTINS_H__ > gtktypebuiltins.h
COMMAND echo \#define __GTK_TYPE_BUILTINS_H__ >> gtktypebuiltins.h
COMMAND echo \#include \"glib-object.h\" >> gtktypebuiltins.h
COMMAND echo G_BEGIN_DECLS >> gtktypebuiltins.h
COMMAND ${PERL} ${GlibEtcInstallRoot}/bin/glib-mkenums
		--fprod "/* enumerations from \\"@filename@\\" */\\n"
		--vhead "GType @enum_name@_get_type (void);\\n\#define GTK_TYPE_@ENUMSHORT@ (@enum_name@_get_type())\\n"
		--ftail "G_END_DECLS\\n\\n\#endif /* __GTK_TYPE_BUILTINS_H__ */"
		${gtk_public_h_sources} >> gtktypebuiltins.h
#		tmp >> gtktypebuiltins.h
COMMAND ${PERL} ${GlibEtcInstallRoot}/bin/glib-mkenums
	--fhead \"\#define GTK_ENABLE_BROKEN\\n\#include \\"gtk.h\\"\\n\#include \\"gtkprivate.h\\"\"
	--fprod \"\\n/* enumerations from \"@filename@\" */\"
	--vhead "\"GType\\n@enum_name@_get_type (void)\\n{\\n  static GType etype = 0;\\n  if (etype == 0) {\\n    static const G@Type@Value values[] = {\""
	--vprod "\"      { @VALUENAME@, \\\"@VALUENAME@\\\", \\\"@valuenick@\\\" },\""
	--vtail "\"      { 0, NULL, NULL }\\n    };\\n    etype = g_\@type\@_register_static (\\\"@EnumName@\\\", values);\\n  }\\n  return etype;\\n}\\n\""
	${gtk_public_h_sources} > gtktypebuiltins.c
#	tmp > gtktypebuiltins.c
DEPENDS ${gtk_public_h_sources}
WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
)

add_custom_target (gtktypebuiltins DEPENDS gtktypebuiltins.c gtktypebuiltins.h)

file(TO_NATIVE_PATH ${GlibEtcInstallRoot}/bin bin)
set(PATH_STRING "$ENV{PATH}\\;${bin}\\bin")
STRING(REPLACE "\\;" ";" PATH_STRING "${PATH_STRING}")
STRING(REPLACE ";" "\\;" PATH_STRING "${PATH_STRING}")
#set(ENV{PATH} "${PATH_STRING}")

add_custom_command (OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/gtkbuiltincache.h
COMMAND set \"PATH=${PATH_STRING}\"
COMMAND gtk-update-icon-cache --force --ignore-theme-index --source builtin_icons stock-icons > gtkbuiltincache.h
#DEPENDS gtk-update-icon-cache
WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
)

add_executable( gtk-update-icon-cache updateiconcache.c )
target_link_libraries(gtk-update-icon-cache gdk-${GtkApiVersion} modules-input
 pangowin32-1.0 atk-1.0 comctl32 libmsvcrt )

add_custom_target(gtkbuiltincache DEPENDS gtk-update-icon-cache ${CMAKE_CURRENT_SOURCE_DIR}/gtkbuiltincache.h )

add_custom_command (OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/gtkmarshalers.h ${CMAKE_CURRENT_SOURCE_DIR}/gtkmarshalers.c
COMMAND	${GlibEtcInstallRoot}/bin/glib-genmarshal --prefix=_gtk_marshal gtkmarshalers.list --header >>gtkmarshalers.h
COMMAND	${GlibEtcInstallRoot}/bin/glib-genmarshal --prefix=_gtk_marshal gtkmarshalers.list --body >gtkmarshalers.c
DEPENDS gtkmarshalers.list
WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
)

add_custom_command (OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/gtktypefuncs.c
COMMAND echo /*none*/ > gtktypefuncs.c
WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
)

add_library(gtk-${GtkApiVersion} SHARED ${GTK_SRCS} gtk.def gtk-win32.rc)

#set_target_properties(gtk-win32 PROPERTIES
#				IMPORT_SUFFIX "-${GtkApiVersion}.lib"
#)

target_link_libraries(gtk-${GtkApiVersion} gdk-${GtkApiVersion} modules-input
 pangowin32-1.0 atk-1.0 comctl32 )

install(TARGETS gtk-${GtkApiVersion}
LIBRARY DESTINATION "lib"
ARCHIVE DESTINATION "lib"
RUNTIME DESTINATION "bin")

install(FILES ${CMAKE_CURRENT_BINARY_DIR}/gtk-${GtkApiVersion}${POSTFIX}.pdb DESTINATION "bin" CONFIGURATIONS DEBUG)

install(DIRECTORY ./ DESTINATION include/gtk-${GtkApiVersion}/gtk
FILES_MATCHING PATTERN "*.h")

install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/org.gtk.Settings.FileChooser.gschema.xml
${GlibEtcInstallRoot}/share/glib-2.0/schemas/gschema.dtd
DESTINATION share/glib-2.0/schemas)
install(CODE "execute_process(COMMAND ${GlibEtcInstallRoot}/bin/glib-compile-schemas.exe . WORKING_DIRECTORY ${CMAKE_INSTALL_PREFIX}/share/glib-2.0/schemas)")
