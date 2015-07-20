import datetime

def add_datetime_segment():
    try:
        fg = Color.DATETIME_FG
    except AttributeError:
        fg = Color.USERNAME_FG
    try:
        bg = Color.DATETIME_BG
    except AttributeError:
        bg = Color.USERNAME_BG

    datetime_segment = ' %s %s '
    datetime_char = u'\u25F7'
    datetime_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    powerline.append(datetime_segment % (datetime_char, datetime_time), fg, bg, None, bg)

add_datetime_segment()
