# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import sys
import random


def main():
   # 定数
   COURT_W,COURT_H=700 ,500                                           # 画面サイズ 幅,高さ
   RACKET_W,RACKET_H=10,50                                            # ラケットサイズ 幅,高さ
   COLOR_WHITE=(255,255,255)                                          # 白のRGB値
   COLOR_BLACK=(0,0,0)                                                # 黒のRGB値
   BALL_R=7                                                           # ボールの半径
   WIN_SCORE=10                                                       # 勝ち点
   BALL_SPEED_X_MIN,BALL_SPEED_X_MAX=7,12                             # ボールの左右スピードの最小値、最大値(横)
   BALL_SPEED_Y_MIN,BALL_SPEED_Y_MAx=0,3                              # ボールの上下スピードの最小値、最大値(縦)
   PLAYER_SPEED_Y_MAX,COMP_SPEED_Y_MAX=4,5                            # プレーヤとコンピュータの上下スピードの最大値
   # 変数
   player_x,player_y=10,COURT_H//2-RACKET_H//2                        # プレーヤーの位置
   player_speed_y=0                                                   # プレーヤーの上下スピード
   comp_x,comp_y=COURT_W-10-RACKET_W,COURT_H//2-RACKET_H//2           # コンピューターの位置
   comp_speed_y=0                                                     # コンピューターの上下スピード
   ball_x,ball_y=COURT_W//2,COURT_H//2-RACKET_H                       # ボール位置
   ball_speed_x,ball_speed_y=BALL_SPEED_X_MIN,BALL_SPEED_Y_MIN        # ボールの左右、上下スピード
   player_score,comp_score=0,0                                        # プレーヤーとコンピューターのスコア

   # pygameの設定
   pygame.init()                                                      # Pygameの初期化
   screen=pygame.display.set_mode((COURT_W,COURT_H))                  # 画面の大きさ
   pygame.display.set_caption("ピンポン")                             # 画面タイトル
   font=pygame.font.SysFont(None,120)                                 # 画面文字の設定

   run=True                                                           # 実行中かどうかの変数を真（True)"実行中"にしておく

   while run:                                                         # 実行中の間ずっと繰り返す 

      # 画面全体を黒で塗りつぶす
      screen.fill(COLOR_BLACK)
      # 各オブジェクトの描画
      # 中央線の描画
      for i in range(10,COURT_H,COURT_H//20):
         if i % 2 == 1:
            continue
         pygame.draw.rect(screen,COLOR_WHITE,(COURT_W//2-5,i,10,COURT_H//20))
      # プレイヤー側のラケット描画
      pygame.draw.rect(screen,COLOR_WHITE,(player_x,player_y,RACKET_W,RACKET_H))
      # コンピューター側のラケット描画
      pygame.draw.rect(screen,COLOR_WHITE,(comp_x,comp_y,RACKET_W,RACKET_H))
      # ボールの描画
      pygame.draw.circle(screen,COLOR_WHITE,(ball_x,ball_y),BALL_R)

      # プレイヤー側スコアの描画
      player_score_text=font.render(f"{player_score}",True,COLOR_WHITE)
      screen.blit(player_score_text,(COURT_W//4-player_score_text.get_width()//2,20))
      # コンピューターのスコアの描画
      comp_score_text=font.render(f"{comp_score}",True,COLOR_WHITE)
      screen.blit(comp_score_text,(COURT_W*(3/4)-comp_score_text.get_width()//2,20))

      # 押されたキーを取得
      pressed_key=pygame.key.get_pressed()

      # プレイヤーの移動
      # 矢印キー「↑」が押された場合
      if pressed_key[K_UP]:
         # プレーヤーの移動スピードを上方向に設定
         player_speed_y=-PLAYER_SPEED_Y_MAX
         # プレーヤーの位置を上に移動
         player_y+=player_speed_y
         # プレーヤーの位置がコートの上をはみ出たら
         if player_y<0:
            # プレーヤーの位置をコートの上端にする
            player_y=0
            # プレーヤーの上下スピードを0にする
            player_speed_y=0
      # 矢印キー「↓」が押された場合
      elif pressed_key[K_DOWN]:
         # プレーヤーの移動スピードを下方向に設定
         player_speed_y=PLAYER_SPEED_Y_MAX
         # プレーヤーの位置を下に移動
         player_y+=player_speed_y
         # プレーヤーの位置（ラケットの下端)がコートの下をはみ出たら
         if player_y>COURT_H-RACKET_H:
            # プレーヤーの位置をコートの下端（ラケットの長さ分上)にする
            player_y=COURT_H-RACKET_H
            # プレーヤーの上下スピードを0にする
            player_speed_y=0
      # キーが何も押されていない場合
      else:
         # プレーヤーの移動スピードを0にする
         player_speed_y=0

      # コンピューターの移動
      # コンピュータの上下の真ん中の位置
      comp_y_mid=comp_y+RACKET_H/2
 
      # ボールとコンピュータの上下の距離
      ball-comp_y=ball_y-comp_y_mid
  
      # ボールがコンピュータの真ん中より下にあって、距離がコンピュータの上下スピードの最大値以上離れていた場合
      if ball-comp_y<-COMP_SPEED_Y_MAX
         # コンピュータの上下スピードを上方向の最大値にする
         comp_speed_y=-COMP_SPEED_Y_MAX
      # ボールがコンピュータの真ん中より上にあって、距離がコンピュータの上下スピードの最大速度以上離れていた場合
      elif ball-comp_y>COMP_SPEED_Y_MAX
         # コンピュータの上下スピードを下方向の最速値にする
         comp_speed_y=COMP_SPEED_Y_MAX
      # ボールがコンピュータの真ん中より上下スピードの最大値、最小値以内にある場合
      else:
         # コンピュータの上下スピードをボールとコンピュータの上下距離にする
         comp_speed_y=ball-comp_y
      # コンピュータの位置を移動
      comp_y += comp_speed_y

      # コンピュータの位置がコートの上をはみ出たら
      if comp_y< 0:
         # コンピュータの位置をコートの上端にする
         comp_y=0
         # コンピュータの上下スピードを0にする
         comp_speed_y=0
      # コンピュータの位置（ラケットの下端)がコートの下をはみ出たら
      elif comp_y+RACKET_H>COURT_H
         # コンピュータの位置をコートの下端（ラケットの長さ分上)にする
         comp_y=COURT_H-RACKET_H

      # ボールの移動
      ball_x+=ball_speed_x
      ball_y+=ball_speed_y

      # ボールがコート上端を行き過ぎたら
      if ball_y-BALL_R<0:
         # ボールの上下位置ををコート上端(ボールの中心がコートの上端よりボールの半径分下）
         ball_y=BALL_R
         # ボールの上下スピードを下向き（反転）にする
         ball_speed_y=-1 * ball_speed_y
      # ボールが下端を行き過ぎたら
      elif ball_y + BALL_R > COURT_H:
         # ボール上下位置をコート下端(ボールの中心がコートの下端よりボールの半径分上）
         ball_y=COURT_H-BALL_R
         # ボールの上下スピードを下向き（反転）にする
         ball_speed_y=-1 * ball_speed_y

      # プレーヤーのラケットにあたったかどうか
      # ボールの右端（ボールの中心からボールの半径分右）がコートの中心より左だったら
      if ball_x+BALL_R<COURT_W/2:
         # ボールの左端（ボールの中心からボールの半径分左）がプレーヤのラケットの右端より左　かつ
         # ボールの右端（ボールの中心からボールの半径分右）がプレーヤのラケットの左端より右　かつ
         # ボールの下端（ボールの中心からボールの半径分下）がプレーヤのラケットの上端より下　かつ
         # ボールの上端（ボールの中心からボールの半径分上）がプレーヤのラケットの下端より上　だったら
         if ball_x-BALL_R<player_x+RACKET_W and ball_x+BALL_R>player_x and ball_y+BALL_R>player_y and ball_y-BALL_R<player_y+RACKET_H:
            ball_speed_x=random.randrange(BALL_SPEED_X_MIN,BALL_SPEED_X_MAX)
            ball_speed_y+=player_speed_y/2
            ball_y+=ball_speed_y
      # コンピューターのラケットにあたったかどうか
      else:
         if ball_x+BALL_R>comp_x and ball_x-BALL_R<comp_x+RACKET_W and ball_y+BALL_R>comp_y and ball_y-BALL_R<comp_y+RACKET_H:
             ball_speed_x=-(random.randrange(BALL_SPEED_X_MIN,BALL_SPEED_X_MAX))
             ball_speed_y+=comp_speed_y/2
             ball_y+=ball_speed_y

      # 得点が入ったかどうか
      win=False
      if ball_x<0:
         ball_x,ball_y=COURT_W//2,COURT_H//2-RACKET_H
         ball_speed_x=-BALL_SPEED_X_MIN
         ball_speed_y=0
         player_y=COURT_H//2-RACKET_H//2
         comp_y=COURT_H//2-RACKET_H//2
         comp_score+=1
         if comp_score==WIN_SCORE:
            win=True
            win_text='You Lost!'
      elif ball_x>COURT_W:
         ball_x,ball_y=COURT_W//2,COURT_H//2-RACKET_H
         ball_speed_x=BALL_SPEED_X_MIN
         ball_speed_y=0
         player_y=COURT_H//2-RACKET_H//2
         comp_y=COURT_H//2-RACKET_H//2
         player_score+=1
         if player_score==WIN_SCORE:
            win=True
            win_text='You Win!!'

      if win:                                              # 勝負ついたら
         text=font.render(win_text,1,COLOR_WHITE)                # 勝敗結果の文設定
         screen.blit(text,(COURT_W//2-text.get_width()//2
                      ,COURT_H//2-text.get_height()//2))   # 勝負結果表示
         run=False

      # 画面を更新
      pygame.display.update() 
      pygame.time.wait(30)

      for event in pygame.event.get():
         if event.type == QUIT:      # 閉じるボタンが押されたら終了
            run=False

   pygame.time.wait(600)
   pygame.quit()
   sys.exit()

if __name__ == "__main__":
   main()
