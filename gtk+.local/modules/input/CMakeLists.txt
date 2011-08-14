add_definitions ( -DINCLUDE_IM_am_et -DINCLUDE_IM_cedilla
-DINCLUDE_IM_cyrillic_translit -DINCLUDE_IM_ime -DINCLUDE_IM_inuktitut
-DINCLUDE_IM_ipa -DINCLUDE_IM_multipress -DINCLUDE_IM_thai
-DINCLUDE_IM_ti_er -DINCLUDE_IM_ti_et -DINCLUDE_IM_viqr
-DMULTIPRESS_CONFDIR="/dummy/etc/gtk-${GtkApiVersion}"
-DMULTIPRESS_LOCALEDIR="/dummy/share"
)

set (INPUT_SRCS
gtkimcontextime.c
gtkimcontextime.h
gtkimcontextmultipress.c
gtkimcontextmultipress.h
gtkimcontextthai.c
gtkimcontextthai.h
imam-et.c
imcedilla.c
imcyrillic-translit.c
imime.c
iminuktitut.c
imipa.c
imm-extra.h
immultipress.c
imthai.c
imti-er.c
imti-et.c
imviqr.c
thai-charprop.c
thai-charprop.h
)

add_library(modules-input STATIC ${INPUT_SRCS})
