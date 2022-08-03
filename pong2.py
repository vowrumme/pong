# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import sys

w, h = 700 , 500                         # 画面サイズ 幅,高さ
rw, rh = 10, 50                          # ラケットサイズ 幅,高さ
white = (255,255,255)                    # 白のRGB値
black = (0,0,0)                          # 黒のRGB値
br = 7                                   # ボールの半径
fps = 60
bvx_max = 5                              # ボールの速度の最大値
winning_score = 10                       # 勝ち点


def main():
    # 各パラメータ
    hx, hy = 10, h//2                     # プレーヤーのラケットの中心位置
    hvx, hvy = 0, 0                       # プレーヤーのラケットのスピード
    cx, cy = w - 10 - rw, h // 2          # コンピューターのラケットの中心位置
    cvx, cvy = 0, 0                       # コンピューターのラケットのスピード
    bx, by = bx0, by0 = w // 2, h //2     # ボール位置、初めの位置
    hdy, cdy = 0 , 0                      # プレーヤーのラケットとボールの距離、
                                          # コンピューターのラケットとボールの距離
    bvx, bvy = bvx_max, 0                 # ボールのスピード
    hs, cs = 0, 0                         # プレーヤーとコンピューターのスコア

    # pygameの設定
    pygame.init()                                # Pygameの初期化
    screen = pygame.display.set_mode((w, h))     # 画面の大きさ
    pygame.display.set_caption("ピンポン")       # 画面タイトル
    font = pygame.font.SysFont(None, 40)         # 画面文字の設定

    run = True

    while run:

        # 画面全体を黒で塗りつぶす
        screen.fill(black)
        # 各オブジェクトの描画
        # 中央線の描画
        for i in range(10, h, h // 20):
            if i % 2 == 1:
                continue
            pygame.draw.rect(screen, white, (w//2 - 5, i, 10, h // 20))
        # プレイヤー側のラケット描画
        pygame.draw.rect(screen, white, (hx, hy, rw, rh))
        # コンピューター側のラケット描画
        pygame.draw.rect(screen, white, cx, cy, rw, rh))
        # ボールの描画
        pygame.draw.circle(screen, white, (bx, by), br)

        # プレイヤー側スコアの描画
        hs_text = font.render(f"{hs}", True, white)
        screen.blit(hs_text,(w//4 - hs_text.get_width() // 2, 20))
        # コンピューターのスコアの描画
        cs_text = font.render(f"{cs}", True, white)
        screen.blit(cs_text,(w * (3/4) - cs_text.get_width() // 2, 20))

        # 押されたキーを取得
        pressed_key = pygame.key.get_pressed()

        # プレイヤーのラケットの移動
        if pressed_key[K_UP]:
            hvy = -4
            hy += hvy
            if hy < 0:
                hy = 0
                hvy = 0
        elif pressed_key[K_DOWN]:
            hvy = 4
            hy += hvy
            if hy > h - rh
                hy = h -rh
                hvy = 0
        else:
            hvy = 0


        # コンピューターのラケットの移動
        if  by > cy:
            cy += 10
        if  by < cy:
            cy -= 10

        #コンピューターのラケットが画面からはみ出ないようにする
        if cy - rh // 2 <= 0:
            cy = rh // 2

        if cy + rh // 2 >= h:
            cy = h - rh // 2

        # ボールの移動
        bx += bvx
        by += bvy

        # ボールが上の壁にあたったかどうか
        if by - br < 0:
            by = 0
            bvy = -bvy
        elif by + br > h
            by = h -br
            bvy = -bvy

        # 得点の計算
　　　　if bx < 0:
            cs  += 1
            bvx = -bvx_max
            bvy = 0
            bx = bx0 
            by = by0
        elif bx > w
            hs  += 1
            bvx = bvx_max
            bvy = 0
            bx = bx0 

   
        # ラケットにあたったかどうか
        if bvx < 0:
            if bx - br <= hx + rw // 2 :
                if by >=  hy - rh // 2 and by <= hy + rh // 2:
                    bx = hx + rw // 2
                    bvx = -bvx
                    bvy = (hy - by)/((rh / 2) / bvx_max)
        else:
            if bx + br >= cx - rw // 2:
                if by >=  cy - rh // 2 and by <= cy + rh // 2: 
                    bx = cx - rw / 2
                    bvx = -bvx
                    bvy = (cy - by)/((rh / 2) / bvx_max)

        if bx < 0 : cs += 1
        elif bx > w : hs += 1

        # ボールが画面からはみ出ないようにする
        if (bx < 0 and bvx < 0) or (bx > w and bvx > 0):
            bvx = -bvx
        if (by < 0 and bvy < 0) or (by > h and bvy > 0):
            bvy = -bvy 


        # 勝敗の判定
        won = False                      # 勝負ついたか判定用変数　
        if hs >= winning_score:          # プレーヤーの勝利？
            won = True                   # 勝負ついた
            win_text = "You won!!"  # 勝敗結果
        elif cs >= winning_score:        # コンピューターの勝利？
            won = True                   # 勝負ついた
            win_text = "You lost!!"  # 勝負結果

        if won:                                                # 勝負ついたら
            text = font.render(win_text, 1, white)            # 勝敗結果の文設定
            screen.blit(text, (w//2 - text.get_width() //2
                             , h//2 - text.get_height()//2))   # 勝負結果表示
            run = False

        # 画面を更新
        pygame.display.update() 
        pygame.time.wait(30)

        for event in pygame.event.get():
            if event.type == QUIT:        # 閉じるボタンが押されたら終了
                run = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
