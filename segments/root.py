def add_root_indicator_segment():
    root_indicators = {
        'bash': ' \\$ ',
        'zsh': ' \\$ ',
        'bare': ' $ ',
    }
    fg = Color.CMD_PASSED_FG
    bg = Color.CMD_PASSED_BG
    if powerline.args.prev_error != 0:
        fg = Color.CMD_FAILED_FG
        bg = Color.CMD_FAILED_BG

    try:
        bg2 = Color.CMD_PASSED_BG2
        if powerline.args.prev_error != 0:
            bg2 = Color.CMD_FAILED_BG2
        powerline.append(root_indicators[powerline.args.shell], fg, bg, None, bg2)
    except:
        powerline.append(root_indicators[powerline.args.shell], fg, bg)

add_root_indicator_segment()
