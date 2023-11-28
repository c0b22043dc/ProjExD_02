import sys
import pygame as pg
import random


WIDTH, HEIGHT = 1600, 900


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    enn = pg.Surface((20,20))  #練習１　一片が２０の正方形を描画
    pg.draw.circle(enn, (255, 0, 0), (10, 10), 10 )  #半径１０の赤い円の描画
    enn.set_colorkey((0, 0, 0))  #黒の透明化
    enn_rct = enn.get_rect()
    enn_rct.centerx = random.randint(0,WIDTH)
    enn_rct.centery = random.randint(0,HEIGHT)
    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        screen.blit(enn,enn_rct)
        pg.display.update()
        tmr += 1
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()