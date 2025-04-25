coclass 'qtprinter'

glzarc_n=: 2201
glzbrush_n=: 2202
glzbrushnull_n=: 2203
glzclear_n=: 2204
glzclip_n=: 2205
glzclipreset_n=: 2206
glzcmds_n=: 2207
glzellipse_n=: 2208
glzfill_n=: 2209
glzfont_n=: 2210
glzfont2_n=: 2211
glzfontangle_n=: 2212
glzfontextent_n=: 2213
glzlines_n=: 2214
glznodblbuf_n=: 2215
glzpen_n=: 2216
glzpie_n=: 2217
glzpixel_n=: 2218
glzpixels_n=: 2219
glzpixelsx_n=: 2220
glzpolygon_n=: 2221
glzrect_n=: 2222
glzrgb_n=: 2223
glzrgba_n=: 2224
glztext_n=: 2225
glztextcolor_n=: 2226
glztextxy_n=: 2227
glzwindoworg_n=: 2228
glzresolution_n=: 2229
glzcolormode_n=: 2230
glzduplexmode_n=: 2231
glzorientation_n=: 2232
glzoutputformat_n=: 2233
glzpageorder_n=: 2234
glzpapersize_n=: 2235
glzpapersource_n=: 2236
glzscale_n=: 2237
glzabortdoc_n=: 2238
glzenddoc_n=: 2239
glznewpage_n=: 2240
glzprinter_n=: 2241
glzstartdoc_n=: 2242
glzinitprinter_n=: 2243
glzqresolution_n=: 2244
glzqcolormode_n=: 2245
glzqduplexmode_n=: 2246
glzqorientation_n=: 2247
glzqoutputformat_n=: 2248
glzqpageorder_n=: 2249
glzqpapersize_n=: 2250
glzqpapersource_n=: 2251
glzqwh_n=: 2252
glzqmargins_n=: 2253
glzqextent_n=: 2254
glzqextentw_n=: 2255
glzqtextmetrics_n=: 2256
glzcapture=: 2257
glzcaret=: 2258
glzcursor=: 2259
glzqtype_n=: 2260
glzpaint_n=:  2261
glzpaintx_n=: 2262
glzsetlocale_n=: 2263
coclass 'qtprinter'

NB. gl2 on printer
NB. all drawing commands should be used for printer only

chkgl2=: 13!:8@3:^:(0&<)@>@{.

NB. =========================================================
glzarc=: chkgl2 @: (('"',libjqt,'" glzarc >',(IFWIN#'+'),' i *i') cd <) "1
glzbrush=: chkgl2 @: (('"',libjqt,'" glzbrush >',(IFWIN#'+'),' i')&cd bind '') "1
glzbrushnull=: chkgl2 @: (('"',libjqt,'" glzbrushnull >',(IFWIN#'+'),' i')&cd bind '') "1
glzclear=: chkgl2 @: (('"',libjqt,'" glzclear >',(IFWIN#'+'),' i')&cd bind '') "1
glzclip=: chkgl2 @: (('"',libjqt,'" glzclip >',(IFWIN#'+'),' i *i') cd <) "1
glzclipreset=: chkgl2 @: (('"',libjqt,'" glzclipreset >',(IFWIN#'+'),' i')&cd bind '') "1
glzcmds=: chkgl2 @: (('"',libjqt,'" glzcmds >',(IFWIN#'+'),' i *i i') cd (;#)) "1
glzellipse=: chkgl2 @: (('"',libjqt,'" glzellipse >',(IFWIN#'+'),' i *i') cd <@:<.) "1
glzfill=: chkgl2 @: (('"',libjqt,'" glzfill >',(IFWIN#'+'),' i *i') cd <@:<.) "1
glzfont=: chkgl2 @: (('"',libjqt,'" glzfont >',(IFWIN#'+'),' i *c') cd <@,) "1
glzfont2=: chkgl2 @: (('"',libjqt,'" glzfont2 >',(IFWIN#'+'),' i *i i') cd (;#)@:<.) "1
glzfontangle=: chkgl2 @: (('"',libjqt,'" glzfontangle >',(IFWIN#'+'),' i i')&cd) "1
glzfontextent=: chkgl2 @: (('"',libjqt,'" glzfontextent >',(IFWIN#'+'),' i *c') cd <@,) "1
glzlines=: chkgl2 @: (('"',libjqt,'" glzlines >',(IFWIN#'+'),' i *i i') cd (;#)) "1
glznodblbuf=: chkgl2 @: (('"',libjqt,'" glznodblbuf >',(IFWIN#'+'),' i i') cd {.@(,&0)) "1
glzpen=: chkgl2 @: (('"',libjqt,'" glzpen >',(IFWIN#'+'),' i *i') cd <@:(2&{.)) "1
glzpie=: chkgl2 @: (('"',libjqt,'" glzpie >',(IFWIN#'+'),' i *i') cd <) "1
glzpixel=: chkgl2 @: (('"',libjqt,'" glzpixel >',(IFWIN#'+'),' i *i') cd <) "1
glzpixels=: chkgl2 @: (('"',libjqt,'" glzpixels >',(IFWIN#'+'),' i *i i') cd (;#)@:<.) "1
glzpixelsx=: chkgl2 @: (('"',libjqt,'" glzpixelsx >',(IFWIN#'+'),' i *i') cd <@:<.) "1
glzpolygon=: chkgl2 @: (('"',libjqt,'" glzpolygon >',(IFWIN#'+'),' i *i i') cd (;#)@:<.) "1
glzrect=: chkgl2 @: (('"',libjqt,'" glzrect >',(IFWIN#'+'),' i *i') cd <) "1
glzrgb=: chkgl2 @: (('"',libjqt,'" glzrgb >',(IFWIN#'+'),' i *i') cd <@:<.) "1
glzrgba=: chkgl2 @: (('"',libjqt,'" glzrgba >',(IFWIN#'+'),' i *i') cd <@:<.) "1
glztext=: chkgl2 @: (('"',libjqt,'" glztext >',(IFWIN#'+'),' i *c') cd <@,) "1
glztextcolor=: chkgl2 @: (('"',libjqt,'" glztextcolor >',(IFWIN#'+'),' i')&cd bind '') "1
glztextxy=: chkgl2 @: (('"',libjqt,'" glztextxy >',(IFWIN#'+'),' i *i') cd <@:<.) "1
glzwindoworg=: chkgl2 @: (('"',libjqt,'" glzwindoworg >',(IFWIN#'+'),' i *i') cd <@:<.) "1

glzresolution=: chkgl2 @: (('"',libjqt,'" glzresolution >',(IFWIN#'+'),' i i')&cd) "1
glzcolormode=: chkgl2 @: (('"',libjqt,'" glzcolormode >',(IFWIN#'+'),' i i')&cd) "1
glzduplexmode=: chkgl2 @: (('"',libjqt,'" glzduplexmode >',(IFWIN#'+'),' i i')&cd) "1
glzorientation=: chkgl2 @: (('"',libjqt,'" glzorientation >',(IFWIN#'+'),' i i')&cd) "1
glzoutputformat=: chkgl2 @: (('"',libjqt,'" glzoutputformat >',(IFWIN#'+'),' i i')&cd) "1
glzpageorder=: chkgl2 @: (('"',libjqt,'" glzpageorder >',(IFWIN#'+'),' i i')&cd) "1
glzpapersize=: chkgl2 @: (('"',libjqt,'" glzpapersize >',(IFWIN#'+'),' i i')&cd) "1
glzpapersource=: chkgl2 @: (('"',libjqt,'" glzpapersource >',(IFWIN#'+'),' i i')&cd) "1

glzscale=: chkgl2 @: (('"',libjqt,'" glzscale >',(IFWIN#'+'),' i *f') cd <) "1

glzabortdoc=: chkgl2 @: (('"',libjqt,'" glzabortdoc >',(IFWIN#'+'),' i')&cd bind '') "1
glzenddoc=: chkgl2 @: (('"',libjqt,'" glzenddoc >',(IFWIN#'+'),' i')&cd bind '') "1
glznewpage=: chkgl2 @: (('"',libjqt,'" glznewpage >',(IFWIN#'+'),' i')&cd bind '') "1
glzprinter=: chkgl2 @: (('"',libjqt,'" glzprinter >',(IFWIN#'+'),' i *c') cd <@,) "1
glzstartdoc=: chkgl2 @: (('"',libjqt,'" glzstartdoc >',(IFWIN#'+'),' i *c *c') cd 2: {. boxopen) "1

glzinitprinter=: chkgl2 @: (('"',libjqt,'" glzinitprinter >',(IFWIN#'+'),' i')&cd bind '') "1

glzqresolution=: (('"',libjqt,'" glzqresolution >',(IFWIN#'+'),' i')&cd bind '') "1
glzqcolormode=: (('"',libjqt,'" glzqcolormode >',(IFWIN#'+'),' i')&cd bind '') "1
glzqduplexmode=: (('"',libjqt,'" glzqduplexmode >',(IFWIN#'+'),' i')&cd bind '') "1
glzqorientation=: (('"',libjqt,'" glzqorientation >',(IFWIN#'+'),' i')&cd bind '') "1
glzqoutputformat=: (('"',libjqt,'" glzqoutputformat >',(IFWIN#'+'),' i')&cd bind '') "1
glzqpageorder=: (('"',libjqt,'" glzqpageorder >',(IFWIN#'+'),' i')&cd bind '') "1
glzqpapersize=: (('"',libjqt,'" glzqpapersize >',(IFWIN#'+'),' i')&cd bind '') "1
glzqpapersource=: (('"',libjqt,'" glzqpapersource >',(IFWIN#'+'),' i')&cd bind '') "1

NB. =========================================================
glzqwh=: 3 : 0"1
wh=. 2#1.1-1.1
chkgl2 cdrc=. ('"',libjqt,'" glzqwh  ',(IFWIN#'+'),' i *f i') cd wh;y
1{::cdrc
)

NB. =========================================================
glzqmargins=: 3 : 0"1
ltrb=. 4#1.1-1.1
chkgl2 cdrc=. ('"',libjqt,'" glzqmargins  ',(IFWIN#'+'),' i *f i') cd ltrb;y
1{::cdrc
)

NB. =========================================================
NB. TODO
glzqextent=: 3 : 0"1
wh=. 2#2-2
chkgl2 cdrc=. ('"',libjqt,'" glzqextent  ',(IFWIN#'+'),' i *c *i') cd (,y);wh
2{::cdrc
)

NB. =========================================================
NB. TODO
glzqextentw=: 3 : 0"1
y=. y,(LF~:{:y)#LF [ y=. ,y
w=. (+/LF=y)#2-2
chkgl2 cdrc=. ('"',libjqt,'" glzqextentw  ',(IFWIN#'+'),' i *c *i') cd y;w
2{::cdrc
)

NB. =========================================================
NB. font information: Height, Ascent, Descent, InternalLeading, ExternalLeading, AverageCharWidth, MaxCharWidth
NB. TODO
glzqtextmetrics=: 3 : 0"1
tm=. 7#2-2
chkgl2 cdrc=. ('"',libjqt,'" glzqtextmetrics  ',(IFWIN#'+'),' i *i') cd <tm
1{::cdrc
)

NB. =========================================================
3 : 0''
if. WDCB_jqtide_ do.
  chkgl2=: ]
  glzarc=: 11 !: glzarc_n
  glzbrush=: 11 !: glzbrush_n
  glzbrushnull=: 11 !: glzbrushnull_n
  glzclear=: 11 !: glzclear_n
  glzclip=: 11 !: glzclip_n
  glzclipreset=: 11 !: glzclipreset_n
  glzcmds=: 11 !: glzcmds_n
  glzellipse=: 11 !: glzellipse_n
  glzfill=: 11 !: glzfill_n
  glzfont=: 11 !: glzfont_n
  glzfont2=: 11 !: glzfont2_n
  glzfontangle=: 11 !: glzfontangle_n
  glzfontextent=: 11 !: glzfontextent_n
  glzlines=: 11 !: glzlines_n
  glznodblbuf=: 11 !: glznodblbuf_n
  glzpen=: 11 !: glzpen_n
  glzpie=: 11 !: glzpie_n
  glzpixel=: 11 !: glzpixel_n
  glzpixels=: 11 !: glzpixels_n
  glzpixelsx=: 11 !: glzpixelsx_n
  glzpolygon=: 11 !: glzpolygon_n
  glzrect=: 11 !: glzrect_n
  glzrgb=: 11 !: glzrgb_n
  glzrgba=: 11 !: glzrgba_n
  glztext=: 11 !: glztext_n
  glztextcolor=: 11 !: glztextcolor_n
  glztextxy=: 11 !: glztextxy_n
  glzwindoworg=: 11 !: glzwindoworg_n
  glzresolution=: 11 !: glzresolution_n
  glzcolormode=: 11 !: glzcolormode_n
  glzduplexmode=: 11 !: glzduplexmode_n
  glzorientation=: 11 !: glzorientation_n
  glzoutputformat=: 11 !: glzoutputformat_n
  glzpageorder=: 11 !: glzpageorder_n
  glzpapersize=: 11 !: glzpapersize_n
  glzpapersource=: 11 !: glzpapersource_n
  glzscale=: 11 !: glzscale_n @: ([: <. 1000.0&*)
  glzabortdoc=: 11 !: glzabortdoc_n
  glzenddoc=: 11 !: glzenddoc_n
  glznewpage=: 11 !: glznewpage_n
  glzprinter=: 11 !: glzprinter_n @: (a.&i.)
  glzstartdoc=: 11 !: glzstartdoc_n @: ;@:((# , a.&i.)&.>)
  glzinitprinter=: 11 !: glzinitprinter_n
  glzqresolution=: 11 !: glzqresolution_n
  glzqcolormode=: 11 !: glzqcolormode_n
  glzqduplexmode=: 11 !: glzqduplexmode_n
  glzqorientation=: 11 !: glzqorientation_n
  glzqoutputformat=: 11 !: glzqoutputformat_n
  glzqpageorder=: 11 !: glzqpageorder_n
  glzqpapersize=: 11 !: glzqpapersize_n
  glzqpapersource=: 11 !: glzqpapersource_n
  glzqwh=: (%&1000.0) @: (11 !: glzqwh_n)
  glzqmargins=: (%&1000.0) @: (11 !: glzqmargins_n)
  glzqextent=: 11 !: glzqextent_n
  glzqextentw=: 11 !: glzqextentw_n
  glzqtextmetrics=: 11 !: glzqtextmetrics_n
  glzcapture=: 11 !: glzcapture_n
  glzcaret=: 11 !: glzcaret_n
  glzcursor=: 11 !: glzcursor_n
  glzqtype=: 11 !: glzqtype_n
end.
EMPTY
)

NB. =========================================================
NB. enum Qprinter::ColorMode
QPrinter_Color=: 1     NB.   print in color if available, otherwise in grayscale.
QPrinter_GrayScale=: 0     NB.   print in grayscale, even on color printers.

NB. enum Qprinter::DuplexMode
QPrinter_DuplexNone=: 0     NB.   Single sided (simplex) printing only.
QPrinter_DuplexAuto=: 1     NB.   The printer's default setting is used to determine whether duplex printing is used.
QPrinter_DuplexLongSide=: 2     NB.   Both sides of each sheet of paper are used for printing. The paper is turned over its longest edge before the
QPrinter_DuplexShortSide=: 3     NB.   Both sides of each sheet of paper are used for printing. The paper is turned over its shortest edge before the second side is printed

NB. enum Qprinter::Orientation
QPrinter_Portrait=: 0     NB.   the page's height is greater than its width.
QPrinter_Landscape=: 1     NB.   the page's width is greater than its height.

NB. enum Qprinter::OutputFormat
QPrinter_NativeFormat=: 0     NB.   QPrinter will print output using a method defined by the platform it is running on. This mode is the default
QPrinter_PdfFormat=: 1     NB.   QPrinter will generate its output as a searchable PDF file. This mode is the default when printing to a
QPrinter_PostScriptFormat=: 2     NB.   QPrinter will generate its output as in the PostScript format.


NB. enum Qprinter::PageOrder
QPrinter_FirstPageFirst=: 0     NB.   the lowest-numbered page should be printed first.
QPrinter_LastPageFirst=: 1     NB.   the highest-numbered page should be printed first.

NB. enum Qprinter::PaperSize
QPrinter_A0=: 5     NB.   841 x 1189 mm
QPrinter_A1=: 6     NB.   594 x 841 mm
QPrinter_A2=: 7     NB.   420 x 594 mm
QPrinter_A3=: 8     NB.   297 x 420 mm
QPrinter_A4=: 0     NB.   210 x 297 mm, 8.26 x 11.69 inches
QPrinter_A5=: 9     NB.   148 x 210 mm
QPrinter_A6=: 10    NB.   105 x 148 mm
QPrinter_A7=: 11    NB.   74 x 105 mm
QPrinter_A8=: 12    NB.   52 x 74 mm
QPrinter_A9=: 13    NB.   37 x 52 mm
QPrinter_B0=: 14    NB.   1000 x 1414 mm
QPrinter_B1=: 15    NB.   707 x 1000 mm
QPrinter_B2=: 17    NB.   500 x 707 mm
QPrinter_B3=: 18    NB.   353 x 500 mm
QPrinter_B4=: 19    NB.   250 x 353 mm
QPrinter_B5=: 1     NB.   176 x 250 mm, 6.93 x 9.84 inches
QPrinter_B6=: 20    NB.   125 x 176 mm
QPrinter_B7=: 21    NB.   88 x 125 mm
QPrinter_B8=: 22    NB.   62 x 88 mm
QPrinter_B9=: 23    NB.   33 x 62 mm
QPrinter_B10=: 16    NB.   31 x 44 mm
QPrinter_C5E=: 24    NB.   163 x 229 mm
QPrinter_Comm10E=: 25    NB.   105 x 241 mm, U.S. Common 10 Envelope
QPrinter_DLE=: 26    NB.   110 x 220 mm
QPrinter_Executive=: 4     NB.   7.5 x 10 inches, 190.5 x 254 mm
QPrinter_Folio=: 27    NB.   210 x 330 mm
QPrinter_Ledger=: 28    NB.   431.8 x 279.4 mm
QPrinter_Legal=: 3     NB.   8.5 x 14 inches, 215.9 x 355.6 mm
QPrinter_Letter=: 2     NB.   8.5 x 11 inches, 215.9 x 279.4 mm
QPrinter_Tabloid=: 29    NB.   279.4 x 431.8 mm
QPrinter_Custom=: 30    NB.   Unknown, or a user defined size.

NB. enum Qprinter::PaperSource
NB. Warning: This is currently only implemented for Windows.
QPrinter_Auto=: 6
QPrinter_Cassette=: 11
QPrinter_Envelope=: 4
QPrinter_EnvelopeManual=: 5
QPrinter_FormSource=: 12
QPrinter_LargeCapacity=: 10
QPrinter_LargeFormat=: 9
QPrinter_Lower=: 1
QPrinter_MaxPageSource=: 13
QPrinter_Middle=: 2
QPrinter_Manual=: 3
QPrinter_OnlyOne=: 0
QPrinter_Tractor=: 7
QPrinter_SmallFormat=: 8

NB. enum Qprinter::Unit
QPrinter_Millimeter=: 0
QPrinter_Point=: 1
QPrinter_Inch=: 2
QPrinter_Pica=: 3
QPrinter_Didot=: 4
QPrinter_Cicero=: 5
QPrinter_DevicePixel=: 6

glzinitprinter ::0:''  NB. initialise session printer
