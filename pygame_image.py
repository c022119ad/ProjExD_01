import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")#練習1背景画像Surfaceの生成
    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img,True,False)#練習2こうかとんSurefaceの反転
    kk_imgs = [pg.transform.rotozoom(kk_img,i,1.0) for i in range (10)]#練習3こうかとんSurfaceリストの生成
    kk_imgs+=([pg.transform.rotozoom(kk_img,10-i,1.0) for i in range (10)])
    bg_img_mir = pg.transform.flip(bg_img,True,False)
    bg_imgs = [bg_img,bg_img_mir]
    c = 0
    tmr = 0
    mir0 = 0
    mir1 = 1
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        x = (tmr%1600)
        
        screen.blit(bg_imgs[mir0],[-x,0])
        #if c <1600:
         #   screen.blit(bg_img, [-x, 0])#練習4背景画像表示 
        #else:
         #   screen.blit(bg_img_mir,[-x,0])
        screen.blit(bg_imgs[mir1],[1600-x, 0])#練習6動く背景画像
        screen.blit(kk_imgs[tmr%20],[300,200])#こうかとん生成
        pg.display.update()
        tmr += 1
        c += 1
        if int((tmr/1600))%2 == 0:
            mir0 = 0
            mir1 = 1
        else:
            mir0 = 1
            mir1 = 0
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()