# chapter_screens.rpy
init python:
    # Настройки по умолчанию
    chapter_font = "DejaVuSans.ttf"
    # chapter_sound = "audio/chapter_open.ogg"

transform bg_fade:
    alpha 0.0
    easein 1.5 alpha 0.8

transform shadow_fade(delay=0.0, fade_time=1.5):
    alpha 0.0 yoffset 30
    pause delay
    easein fade_time alpha 1.0 yoffset 0
    pause 1.5
    easeout 1.0 alpha 0.0 yoffset -20

screen shadow_chapter(title, subtitle="", duration=5.0):
    zorder 200
    modal True
    
    add Solid("#000000") at bg_fade
    
    vbox:
        align (0.5, 0.5)
        spacing 25
        text title:
            font chapter_font
            size 60
            color "#FFFFFF"
            outlines [ (3, "#000000DD", 0, 0) ]
            at shadow_fade(0.2, 1.8)
        
        if subtitle:
            text subtitle:
                font chapter_font
                size 35
                color "#AAAAAA"
                italic True
                outlines [ (2, "#000000DD", 0, 0) ]
                at shadow_fade(0.7, 1.2)
    
    timer duration action [Hide("shadow_chapter"), Return()]