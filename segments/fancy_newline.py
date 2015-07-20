def add_fancy_newline_segment():
    try:
        fg = Color.FANCY_NEWLINE_FG
        bg = Color.FANCY_NEWLINE_BG
        bg2 = Color.FANCY_NEWLINE_BG2
        sc = Color.FANCY_NEWLINE_SC
    except:
        fg = Color.HOSTNAME_FG
        bg = Color.HOSTNAME_BG
        bg2 = Color.HOSTNAME_BG
        sc = Color.HOSTNAME_BG

    powerline.append(u'  \u21A9  ', fg, bg)
    powerline.append('', None, bg2, None, sc)
    powerline.append('\n', None, 'reset', '')

add_fancy_newline_segment()
