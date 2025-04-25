coclass 'qtopengl'

gl_arc_n=: 2101
gl_brush_n=: 2102
gl_brushnull_n=: 2103
gl_capture_n=: 2104
gl_caret_n=: 2105
gl_clear_n=: 2106
gl_clip_n=: 2107
gl_clipreset_n=: 2108
gl_cmds_n=: 2109
gl_cursor_n=: 2110
gl_ellipse_n=: 2111
gl_fill_n=: 2112
gl_font_n=: 2113
gl_font2_n=: 2114
gl_fontangle_n=: 2115
gl_lines_n=: 2116
gl_nodblbuf_n=: 2117
gl_paint_n=: 2118
gl_paintx_n=: 2119
gl_pen_n=: 2120
gl_pie_n=: 2121
gl_pixel_n=: 2122
gl_pixels_n=: 2123
gl_pixelsx_n=: 2124
gl_polygon_n=: 2125
gl_rect_n=: 2126
gl_rgb_n=: 2127
gl_rgba_n=: 2128
gl_sel_n=: 2129
gl_sel2_n=: 2130
gl_text_n=: 2131
gl_textcolor_n=: 2132
gl_textxy_n=: 2133
gl_waitgl_n=: 2134
gl_waitnative_n=: 2135
gl_windoworg_n=: 2136
gl_updategl_n=: 2137
gl_setlocale_n=: 2138
gl_qhandles_n=: 2139
gl_qwh_n=: 2140
gl_qpixelm_n=: 2141
gl_qpixels_n=: 2142
gl_qextent_n=: 2143
gl_qextentw_n=: 2144
gl_qtextmetrics_n=: 2145
gl_fontextent_n=: 2146
gl_qtype_n=: 2147
coclass 'qtopengl'

NB. gl2 overlay on opengl
NB. all drawing commands should be used inside paintz event only

chkgl2=: 13!:8@3:^:(0&<)@>@{.

NB. =========================================================
gl_arc=: chkgl2 @: (('"',libjqt,'" gl_arc >',(IFWIN#'+'),' i *i') cd <) "1
gl_brush=: chkgl2 @: (('"',libjqt,'" gl_brush >',(IFWIN#'+'),' i')&cd bind '') "1
gl_brushnull=: chkgl2 @: (('"',libjqt,'" gl_brushnull >',(IFWIN#'+'),' i')&cd bind '') "1
gl_capture=: chkgl2 @: (('"',libjqt,'" gl_capture >',(IFWIN#'+'),' i i')&cd) "1
gl_caret=: chkgl2 @: (('"',libjqt,'" gl_caret >',(IFWIN#'+'),' i *i') cd <) "1
gl_clear=: chkgl2 @: (('"',libjqt,'" gl_clear >',(IFWIN#'+'),' i')&cd bind '') "1
gl_clip=: chkgl2 @: (('"',libjqt,'" gl_clip >',(IFWIN#'+'),' i *i') cd <) "1
gl_clipreset=: chkgl2 @: (('"',libjqt,'" gl_clipreset >',(IFWIN#'+'),' i')&cd bind '') "1
gl_cmds=: chkgl2 @: (('"',libjqt,'" gl_cmds >',(IFWIN#'+'),' i *i i') cd (;#)) "1
gl_cursor=: chkgl2 @: (('"',libjqt,'" gl_cursor >',(IFWIN#'+'),' i i')&cd) "1
gl_ellipse=: chkgl2 @: (('"',libjqt,'" gl_ellipse >',(IFWIN#'+'),' i *i') cd <@:<.) "1
gl_fill=: chkgl2 @: (('"',libjqt,'" gl_fill >',(IFWIN#'+'),' i *i') cd <@:<.) "1
gl_font=: chkgl2 @: (('"',libjqt,'" gl_font >',(IFWIN#'+'),' i *c') cd <@,) "1
gl_font2=: chkgl2 @: (('"',libjqt,'" gl_font2 >',(IFWIN#'+'),' i *i i') cd (;#)@:<.) "1
gl_fontangle=: chkgl2 @: (('"',libjqt,'" gl_fontangle >',(IFWIN#'+'),' i i')&cd) "1
gl_lines=: chkgl2 @: (('"',libjqt,'" gl_lines >',(IFWIN#'+'),' i *i i') cd (;#)) "1
gl_nodblbuf=: chkgl2 @: (('"',libjqt,'" gl_nodblbuf >',(IFWIN#'+'),' i i') cd {.@(,&0)) "1
gl_paint=: chkgl2 @: (('"',libjqt,'" gl_paint >',(IFWIN#'+'),' i')&cd bind '') "1
gl_paintx=: chkgl2 @: (('"',libjqt,'" gl_paintx >',(IFWIN#'+'),' i')&cd bind '') "1
gl_pen=: chkgl2 @: (('"',libjqt,'" gl_pen >',(IFWIN#'+'),' i *i') cd <@:(2&{.)) "1
gl_pie=: chkgl2 @: (('"',libjqt,'" gl_pie >',(IFWIN#'+'),' i *i') cd <) "1
gl_pixel=: chkgl2 @: (('"',libjqt,'" gl_pixel >',(IFWIN#'+'),' i *i') cd <) "1
gl_pixels=: chkgl2 @: (('"',libjqt,'" gl_pixels >',(IFWIN#'+'),' i *i i') cd (;#)@:<.) "1
gl_pixelsx=: chkgl2 @: (('"',libjqt,'" gl_pixelsx >',(IFWIN#'+'),' i *i') cd <@:<.) "1
gl_polygon=: chkgl2 @: (('"',libjqt,'" gl_polygon >',(IFWIN#'+'),' i *i i') cd (;#)@:<.) "1
gl_rect=: chkgl2 @: (('"',libjqt,'" gl_rect >',(IFWIN#'+'),' i *i') cd <) "1
gl_rgb=: chkgl2 @: (('"',libjqt,'" gl_rgb >',(IFWIN#'+'),' i *i') cd <@:<.) "1
gl_rgba=: chkgl2 @: (('"',libjqt,'" gl_rgba >',(IFWIN#'+'),' i *i') cd <@:<.) "1
gl_sel=: chkgl2 @: (('"',libjqt,'" gl_sel >',(IFWIN#'+'),' i x')&cd) "1
gl_sel2=: chkgl2 @: (('"',libjqt,'" gl_sel2 >',(IFWIN#'+'),' i *c') cd <@,) "1
gl_text=: chkgl2 @: (('"',libjqt,'" gl_text >',(IFWIN#'+'),' i *c') cd <@,) "1
gl_textcolor=: chkgl2 @: (('"',libjqt,'" gl_textcolor >',(IFWIN#'+'),' i')&cd bind '') "1
gl_textxy=: chkgl2 @: (('"',libjqt,'" gl_textxy >',(IFWIN#'+'),' i *i') cd <@:<.) "1
gl_waitgl=: chkgl2 @: (('"',libjqt,'" gl_waitgl >',(IFWIN#'+'),' i')&cd bind '') "1
gl_waitnative=: chkgl2 @: (('"',libjqt,'" gl_waitnative >',(IFWIN#'+'),' i')&cd bind '') "1
gl_windoworg=: chkgl2 @: (('"',libjqt,'" gl_windoworg >',(IFWIN#'+'),' i *i') cd <@:<.) "1
gl_updategl=: chkgl2 @: (('"',libjqt,'" gl_updategl >',(IFWIN#'+'),' i x')&cd) "1

gl_setlocale=: chkgl2 @: (('"',libjqt,'" gl_setlocale >',(IFWIN#'+'),' i *c') cd <@,@>) "1

NB. =========================================================
gl_qhandles=: 3 : 0"1
hs=. 3#2-2
chkgl2 cdrc=. ('"',libjqt,'" gl_qhandles  ',(IFWIN#'+'),' i *x') cd <hs
1{::cdrc
)

NB. =========================================================
gl_qwh=: 3 : 0"1
wh=. 2#2-2
chkgl2 cdrc=. ('"',libjqt,'" gl_qwh  ',(IFWIN#'+'),' i *i') cd <wh
1{::cdrc
)

NB. =========================================================
NB. return matrix of pixels
NB. wh is limited to pixmap size
NB. -1 in w or h means read to end
gl_qpixelm=: 3 : 0"1
n=. */ 2{.2}.y
pix=. n#2-2
shape=. 2#2-2
chkgl2 cdrc=. ('"',libjqt,'" gl_qpixelm  ',(IFWIN#'+'),' i *i *i *i') cd y;shape;pix
(2&{:: $ 3&{::) cdrc
)

NB. =========================================================
NB. result is in opengl_ form
NB. pixels top to bottom, RGB24
NB. TODO
gl_qpixels=: 3 : 0"1
n=. */ 2{.2}.y
pix=. n#2-2
chkgl2 cdrc=. ('"',libjqt,'" gl_qpixels  ',(IFWIN#'+'),' i *i *i') cd y;pix
2{::cdrc
)

NB. =========================================================
NB. TODO
gl_qextent=: 3 : 0"1
wh=. 2#2-2
chkgl2 cdrc=. ('"',libjqt,'" gl_qextent  ',(IFWIN#'+'),' i *c *i') cd (,y);wh
2{::cdrc
)

NB. =========================================================
NB. TODO
gl_qextentw=: 3 : 0"1
y=. y,(LF~:{:y)#LF [ y=. ,y
w=. (+/LF=y)#2-2
chkgl2 cdrc=. ('"',libjqt,'" gl_qextentw  ',(IFWIN#'+'),' i *c *i') cd y;w
2{::cdrc
)

NB. =========================================================
NB. font information: Height, Ascent, Descent, InternalLeading, ExternalLeading, AverageCharWidth, MaxCharWidth
NB. TODO
gl_qtextmetrics=: 3 : 0"1
tm=. 7#2-2
chkgl2 cdrc=. ('"',libjqt,'" gl_qtextmetrics  ',(IFWIN#'+'),' i *i') cd tm
1{::cdrc
)

NB. =========================================================
3 : 0''
if. WDCB_jqtide_ do.
  chkgl2=: ]
  gl_arc=: 11 !: gl_arc_n
  gl_brush=: 11 !: gl_brush_n
  gl_brushnull=: 11 !: gl_brushnull_n
  gl_capture=: 11 !: gl_capture_n
  gl_caret=: 11 !: gl_caret_n
  gl_clear=: 11 !: gl_clear_n
  gl_clip=: 11 !: gl_clip_n
  gl_clipreset=: 11 !: gl_clipreset_n
  gl_cmds=: 11 !: gl_cmds_n
  gl_cursor=: 11 !: gl_cursor_n
  gl_ellipse=: 11 !: gl_ellipse_n
  gl_fill=: 11 !: gl_fill_n
  gl_font=: 11 !: gl_font_n
  gl_font2=: 11 !: gl_font2_n
  gl_fontangle=: 11 !: gl_fontangle_n
  gl_lines=: 11 !: gl_lines_n
  gl_nodblbuf=: 11 !: gl_nodblbuf_n
  gl_paint=: 11 !: gl_paint_n
  gl_paintx=: 11 !: gl_paintx_n
  gl_pen=: 11 !: gl_pen_n
  gl_pie=: 11 !: gl_pie_n
  gl_pixel=: 11 !: gl_pixel_n
  gl_pixels=: 11 !: gl_pixels_n
  gl_pixelsx=: 11 !: gl_pixelsx_n
  gl_polygon=: 11 !: gl_polygon_n
  gl_rect=: 11 !: gl_rect_n
  gl_rgb=: 11 !: gl_rgb_n
  gl_rgba=: 11 !: gl_rgba_n
  gl_sel=: (11 !: gl_sel_n)`(11 !: gl_sel2_n)@.(2=3!:0)
  gl_sel2=: 11 !: gl_sel2_n
  gl_text=: 11 !: gl_text_n
  gl_textcolor=: 11 !: gl_textcolor_n
  gl_textxy=: 11 !: gl_textxy_n
  gl_waitgl=: 11 !: gl_waitgl_n
  gl_waitnative=: 11 !: gl_waitnative_n
  gl_windoworg=: 11 !: gl_windoworg_n
  gl_updategl=: 11 !: gl_updategl_n
  gl_setlocale=: 11 !: gl_setlocale_n
  gl_qhandles=: 11 !: gl_qhandles_n
  gl_qwh=: 11 !: gl_qwh_n
  gl_qpixelm=: 11 !: gl_qpixelm_n
  gl_qpixels=: 11 !: gl_qpixels_n
  gl_qextent=: 11 !: gl_qextent_n
  gl_qextentw=: 11 !: gl_qextentw_n
  gl_qtextmetrics=: 11 !: gl_qtextmetrics_n
  gl_fontextent=: 11 !: gl_fontextent_n
  gl_qtype=: 11 !: gl_qtype_n
end.
EMPTY
)
