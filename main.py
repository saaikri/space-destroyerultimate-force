def on_a_pressed():
    global projectile2
    projectile2 = sprites.create_projectile_from_sprite(assets.image("""
        Bulllet
    """), mySprite, 0, -140)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    otherSprite.destroy(effects.ashes, 100)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    otherSprite2.destroy(effects.fire, 100)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

mySprite2: Sprite = None
projectile2: Sprite = None
mySprite: Sprite = None
effects.star_field.start_screen_effect()
info.set_life(4)
mySprite = sprites.create(assets.image("""
    SpaceCraft
"""), SpriteKind.player)
controller.move_sprite(mySprite)
mySprite.set_stay_in_screen(True)
mySprite.bottom = 120

def on_update_interval():
    global mySprite2
    mySprite2 = sprites.create(assets.image("""
        Astroid
    """), SpriteKind.enemy)
    mySprite2.set_position(randint(0, 160), 0)
    mySprite2.set_velocity(0, 50)
game.on_update_interval(1000, on_update_interval)

def on_forever():
    music.play_melody("C5 B A B C5 G A E ", 200)
    if info.life() < 0:
        music.set_volume(0)
forever(on_forever)
