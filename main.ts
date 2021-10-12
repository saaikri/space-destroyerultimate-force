controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    projectile2 = sprites.createProjectileFromSprite(assets.image`Bulllet`, mySprite, 0, -140)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    otherSprite.destroy(effects.ashes, 100)
    info.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    otherSprite.destroy(effects.fire, 100)
    info.changeLifeBy(-1)
})
let mySprite2: Sprite = null
let projectile2: Sprite = null
let mySprite: Sprite = null
effects.starField.startScreenEffect()
info.setLife(4)
mySprite = sprites.create(assets.image`SpaceCraft`, SpriteKind.Player)
controller.moveSprite(mySprite)
mySprite.setStayInScreen(true)
mySprite.bottom = 120
game.onUpdateInterval(1000, function () {
    mySprite2 = sprites.create(assets.image`Astroid`, SpriteKind.Enemy)
    mySprite2.setPosition(randint(0, 160), 0)
    mySprite2.setVelocity(0, 50)
})
forever(function () {
    music.playMelody("C5 B A B C5 G A E ", 200)
    if (info.life() < 0) {
        music.setVolume(0)
    }
})
