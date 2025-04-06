from ranger.gui.colorscheme import ColorScheme
from ranger.gui.color import *

# fg = #AFAFAF ≈ 248
# bg = #121212 ≈ 233

default_colors = 248, 233, 0  # fg, bg, attr

class Scheme(ColorScheme):
    progress_bar_color = 61  

    def use(self, context):
        fg, bg, attr = default_colors

        if context.reset:
            return fg, bg, attr

        if context.in_browser:
            fg = 248  # default foreground
            bg = 233  # dark bg
            if context.selected:
                attr |= reverse
            if context.empty or context.error:
                fg = 160  # red error
            if context.border:
                fg = 240
            if context.image:
                fg = 114
            if context.video:
                fg = 137
            if context.audio:
                fg = 174
            if context.document:
                fg = 109
            if context.directory:
                fg = 97
                attr |= bold
            if context.executable and not context.directory:
                fg = 144
                attr |= bold
            if context.link:
                fg = 110 if context.good else 160
            if context.marked:
                fg = 221
                attr |= bold
            if context.badinfo:
                fg = 160
        elif context.in_titlebar:
            attr |= bold
            if context.hostname:
                fg = 110 if context.good else 160
            elif context.directory:
                fg = 252
            elif context.tab:
                fg = 221 if context.good else 240
        elif context.in_statusbar:
            fg = 248
            bg = 233
            if context.permissions:
                fg = 110 if context.good else 160
            if context.marked:
                attr |= bold
                fg = 221
        elif context.in_taskview:
            fg = 248
            bg = 233

        return fg, bg, attr
