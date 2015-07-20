def add_fancy_newline_segment():
    try:
        fg = Color.FANCY_NEWLINE_FG
        bg = Color.FANCY_NEWLINE_BG
    except:
        fg = Color.HOSTNAME_FG
        bg = Color.HOSTNAME_BG

    try:
        tail_fg = Color.FANCY_NEWLINE_TAIL_FG
        tail_fg_adj = Color.FANCY_NEWLINE_TAIL_FG_OVER_RESET
        powerline.append(u'  \u21A9  ', fg, bg)
        powerline.append('', None, tail_fg_adj, None, tail_fg)
    except:
        powerline.append(u'  \u21A9  ', fg, bg, '')

    powerline.append('\n', None, 'reset', '')

add_fancy_newline_segment()
