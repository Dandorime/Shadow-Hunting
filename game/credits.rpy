transform scroll_up:
    yalign 1.2
    ease 12.0 yalign -0.5

transform fadein_t:
    alpha 0.0
    linear 0.3 alpha 1.0

transform fadeout_t:
    pause 10.0
    linear 2.0 alpha 0.0

screen credits_screen:
    tag menu

    add Solid("#000")

    vbox at scroll_up:
        xalign 0.5
        spacing 40

        text "Сосницкая Александра — нарративный дизайнер" at fadein_t, fadeout_t style "credit_text"
        text "Патриссия Цехарьяш — художник" at fadein_t, fadeout_t style "credit_text"
        text "Валеева Элина — продюсер" at fadein_t, fadeout_t style "credit_text"
        text "Гуляев Даниил — разработчик" at fadein_t, fadeout_t style "credit_text"
        text ""
        text "Музыка:" at fadein_t, fadeout_t style "credit_text"
        text "Chikoi the Maid — Pretendet" at fadein_t, fadeout_t style "credit_text"
        text ""
        text "Изображения фоны:" at fadein_t, fadeout_t style "credit_text"
        text "Krea" at fadein_t, fadeout_t style "credit_text"

    textbutton "Пропустить" action Return() xpos 0.95 ypos 0.05 anchor (0.5, 0.5)

    timer 12.0 action Return()

init python:
    style.credit_text = Style(style.default)
    style.credit_text.size = 40
    style.credit_text.color = "#FFFFFF"
    style.credit_text.outlines = [(2, "#000", 0, 0)]
    # style.credit_text.font = "fonts/YourFont.ttf"

label show_credits:
    play music "audio/music/Chikoi_The_Maid_-_Pretendet.mp3" volume 1.0
    call screen credits_screen
    stop music fadeout 2.0
    return
