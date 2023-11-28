import sys
import pygame as pg
import random


WIDTH, HEIGHT = 1600, 900
delta = {
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (+5, 0)
}
def check_bound(rct: pg.Rect) -> tuple[bool, bool]:  #練習４　爆弾判定
    yoko, tate = True, True
    if rct.left < 0 or WIDTH < rct.right:
        yoko = False
    if rct.top < 0 or HEIGHT < rct.bottom:
        tate = False
    return yoko, tate




def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rct = kk_img.get_rect()  #練習３こうかとんSurfaceのrect抽出
    kk_rct.center = 900, 400  #練習３：こうかとんの初期座標
    enn = pg.Surface((20,20))  #練習１　一片が２０の正方形を描画
    pg.draw.circle(enn, (255, 0, 0), (10, 10), 10 )  #半径１０の赤い円の描画
    enn.set_colorkey((0, 0, 0))  #黒の透明化
    enn_rct = enn.get_rect()
    enn_rct.centerx = random.randint(0,WIDTH)
    enn_rct.centery = random.randint(0,HEIGHT)
    vx, vy = +5, +5  #練習２　爆弾の移動
    clock = pg.time.Clock()
    tmr = 0
    while True:
        
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        if kk_rct.colliderect(enn_rct):  #練習５こうかとんの衝突
            print("Game Over")
            return
        key_lst = pg.key.get_pressed() #キーが押されたら
        sum_mv = [0, 0]
        for k, tpl in delta.items():
            if key_lst[k]:
                sum_mv[0] += tpl[0]
                sum_mv[1] += tpl[1]
        screen.blit(bg_img, [0, 0])
        kk_rct.move_ip(sum_mv[0], sum_mv[1])
        if check_bound(kk_rct) !=(True, True):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])
        screen.blit(kk_img, kk_rct) #練習３　こうかとんの移動
        enn_rct.move_ip(vx,vy)
        yoko, tate = check_bound(enn_rct)
        if not yoko:  #横にはみ出たら
            vx *= -1
        if not tate:  #縦にはみ出たら
            vy *= -1
        enn_rct.move_ip(vx, vy)
        screen.blit(enn,enn_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)
        


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()