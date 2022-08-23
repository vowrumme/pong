# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import sys
import random


def main():
   #
   # 定数
   #
   COURT_W,COURT_H,COURT_BLANK=700, 500, 10                           # コートサイズ 幅,高さ,余白
   RACKET_W,RACKET_H=10,50                                            # ラケットサイズ 幅,高さ
   COLOR_WHITE=(255,255,255)                                          # 白のRGB値
   COLOR_BLACK=(0,0,0)                                                # 黒のRGB値
   COLOR_RED=(255,0,0)                                                # 赤のRGB値
   COLOR_GREEN=(0,255,0)                                              # 緑のRGB値
   COLOR_BLUE=(0,0,255)                                               # 青のRGB値
   FONT_SIZE_GAMEOVER=128                                             # GAMEOVERのフォントサイズ
   FONT_SIZE_WINMESSAGE=80                                            # 勝利メッセージのフォントサイズ
   FONT_SIZE_SCORE=64                                                 # スコアのフォントサイズ
   BALL_R=7                                                           # ボールの半径
   WIN_SCORE=10                                                       # 勝ち点
   BALL_SPEED_X_MIN,BALL_SPEED_X_MAX=8,15                             # ボールの左右スピードの最小値、最大値(横)
   BALL_SPEED_Y_MIN,BALL_SPEED_Y_MAX=0,5                              # ボールの上下スピードの最小値、最大値(縦)
   PLAYER_SPEED_Y_MAX,COMPUTER_SPEED_Y_MAX=4,5                        # プレーヤとコンピュータの上下スピードの最大値
   COMPUTER_MAX      = 1.0                                            # コンピュータの強さ（最強）
   COMPUTER_STRONG   = 0.9                                            # コンピュータの強さ（強い）
   COMPUTER_MIDDLE   = 0.7                                            # コンピュータの強さ（普通）
   COMPUTER_BEGINNER = 0.6                                            # コンピュータの強さ（弱い）
   COMPUTER_WEAK     = 0.5                                            # コンピュータの強さ（最弱）
   #
   # 変数
   #
   player_speed_y=0                                                       # プレーヤーの上下スピード
   player_x,player_y=COURT_W-COURT_BLANK-RACKET_W,COURT_H//2-RACKET_H//2  # プレーヤーの位置
   computer_x,computer_y=COURT_BLANK,COURT_H//2-RACKET_H//2               # コンピュータの位置
   computer_speed_y=0                                                     # コンピューターの上下スピード
   ball_x,ball_y=COURT_W//2,COURT_H//2-RACKET_H                           # ボール位置
   ball_speed_x,ball_speed_y=BALL_SPEED_X_MIN,BALL_SPEED_Y_MIN            # ボールの左右、上下スピード
   player_score,computer_score=0,0                                        # プレーヤーとコンピューターのスコア
   #
   # pygameの設定
   #
   pygame.init()                                                      # Pygameの初期化
   screen=pygame.display.set_mode((COURT_W,COURT_H))                  # 画面の大きさ
   pygame.display.set_caption("ピンポン")                              # 画面タイトル
   pygame.mouse.set_visible(False)                                    # マウスポインタを表示しない

   computer_level=COMPUTER_MAX
   run=True                                                           # 実行中かどうかの変数を真（True)"実行中"にしておく

   while run:                                                         # 実行中の間ずっと繰り返す 

      #
      # 各オブジェクトの描画
      #

      # 画面全体を黒で塗りつぶす
      screen.fill(COLOR_BLACK)

      # 中央線の描画
      for i in range(COURT_BLANK,COURT_H,COURT_H//20):
         if i % 2 == 1:
            continue
         pygame.draw.rect(screen,COLOR_WHITE,(COURT_W//2-5,i,10,COURT_H//20))
      # プレイヤー側のラケット描画
      pygame.draw.rect(screen,COLOR_WHITE,(player_x,player_y,RACKET_W,RACKET_H))
      # コンピューター側のラケット描画
      pygame.draw.rect(screen,COLOR_WHITE,(computer_x,computer_y,RACKET_W,RACKET_H))
      # ボールの描画
      pygame.draw.circle(screen,COLOR_WHITE,(ball_x,ball_y),BALL_R)
      print(f"(ball_x,ball_y,ball_speed_x,ball_speed_y):{(ball_x,ball_y,ball_speed_x,ball_speed_y)}")

      # スコアの描画
      font=pygame.font.SysFont(None,FONT_SIZE_SCORE)                     
      score_text=font.render(f"{computer_score}   {player_score}",True,COLOR_WHITE)
      screen.blit(score_text,(COURT_W//2-score_text.get_width()//2,20))

      #
      # プレイヤーの移動
      #

      #
      # キーボードの場合
      #
      # 押されたキーを取得
      #pressed_key=pygame.key.get_pressed()
      #
      # 矢印キー「↑」が押された場合
      #if pressed_key[K_UP]:
      #   # プレーヤーの移動スピードを上方向に設定
      #   player_speed_y=-PLAYER_SPEED_Y_MAX
      #   # プレーヤーの位置を上に移動
      #   player_y+=player_speed_y
      #   # プレーヤーの位置がコートの上をはみ出たら
      #   if player_y<0:
      #      # プレーヤーの位置をコートの上端にする
      #      player_y=0
      #      # プレーヤーの上下スピードを0にする
      #      player_speed_y=0
      # 矢印キー「↓」が押された場合
      #elif pressed_key[K_DOWN]:
      #   # プレーヤーの移動スピードを下方向に設定
      #   player_speed_y=PLAYER_SPEED_Y_MAX
      #   # プレーヤーの位置を下に移動
      #   player_y+=player_speed_y
      #   # プレーヤーの位置（ラケットの下端)がコートの下をはみ出たら
      #   if player_y>COURT_H-RACKET_H:
      #      # プレーヤーの位置をコートの下端（ラケットの長さ分上)にする
      #      player_y=COURT_H-RACKET_H
      #      # プレーヤーの上下スピードを0にする
      #      player_speed_y=0
      # キーが何も押されていない場合
      #else:
      #   # プレーヤーの移動スピードを0にする
      #   player_speed_y=0

      #
      # マウスの場合
      #
      
      # マウスの上下左右の位置を取得
      mouse_x,mouse_y = pygame.mouse.get_pos()
      # プレーヤーの上下位置をマウスの位置にする
      player_y = mouse_y
      # プレーヤーの位置が上を出た場合
      if player_y < 0:
         # プレーヤーの位置を上端にする
         player_y =0
      # プレーヤーの位置が下を出た場合
      if player_y > COURT_H - RACKET_H:
         player_y = COURT_H - RACKET_H

      #
      # コンピュータの移動
      #
      
      # コンピュータとボールの横の距離
      between_computer_and_ball_x = ball_x - computer_x + RACKET_W
      # コンピュータとボールの縦の距離
      between_computer_and_ball_y = ball_y - (computer_y + RACKET_H//2)
      # コンピュータとプレーヤーの横の距離
      between_computer_and_player_x = player_x - computer_x
      # コンピュータの移動スピードを決める
      computer_speed_y = 0
      # ボールの進行方向が左向きで、コンピュータとボールの距離がコンピュータの強さに応じて距離が縮まった場合：
      if ball_speed_x < 0 and between_computer_and_ball_x < between_computer_and_player_x * computer_level:
         # ボールがコンピュータより下にある場合
         if between_computer_and_ball_y > 0:
            # コンピュータのスピードはコンピュータの下向きの最速スピードとボールとの縦の距離の少ない方を設定する
            computer_speed_y = min(between_computer_and_ball_y,COMPUTER_SPEED_Y_MAX)
         # ボールがコンピュータより上にある場合
         else:
            # コンピュータのスピードはコンピュータの上向きの最速スピードとボールとの縦の距離の少ない方を設定する
            computer_speed_y = max(between_computer_and_ball_y,-COMPUTER_SPEED_Y_MAX)
      # コンピュータを移動する   
      computer_y += computer_speed_y 
      # コンピュータの位置が上を出た場合
      if computer_y < 0:
         # コンピュータの位置を上端にする
         computer_y =0
      # 位置が下を出た場合
      if computer_y > COURT_H - RACKET_H:
         # コンピュータの位置を下端にする
         computer_y = COURT_H - RACKET_H
   
      #
      # ボールの移動
      #
      # ボールの横の位置にボールのスピードを加える
      ball_x+=ball_speed_x
      # ボールの縦の位置にボールのスピードを加える
      ball_y+=ball_speed_y

      # ボールがコート上端を行き過ぎたら
      if ball_y<BALL_R :
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

      #
      # ラケットに当たったかどうか判定
      #

      # コンピュータのラケットに当たったかどうか判定
      # ボールの左端がコンピュータのラケットの右端を左に超えた場合　かつ
      # ボールの縦の中心がコンピュータのラケットの上端より下になっている場合　かつ
      # ボールの縦の中心がコンピュータのラケットの下端より上になっている場合
      if ball_x - BALL_R < computer_x + RACKET_W and ball_y > computer_y and ball_y < computer_y + RACKET_H:
         # ボールの横の位置をコンピュータのラケットの右側に接触（ボールの中心が半径分右）した位置にする
         ball_x = computer_x + RACKET_W + BALL_R
         # ボールの横の進行方向のスピードを反転（右）にしてスピード１０％増やす
         ball_speed_x *= -1.1
         # ボールの縦の進行方向のスピードはボールの上方向の最速値から下方向の範囲ででたらめ（乱数）な値を設定する
         ball_speed_y = random.randrange(-BALL_SPEED_Y_MAX, BALL_SPEED_Y_MAX )
      # プレーヤーのラケットにあたったかどうか判定
      # ボールの右端がプレーヤーのラケットの左端を右に超えた場合　かつ
      # ボールの縦の中心がプレーヤーのラケットの上端より下になっている場合　かつ
      # ボールの縦の中心がプレーヤーのラケットの下端より上になっている場合
      elif ball_x + BALL_R > player_x and ball_y > player_y and ball_y < player_y + RACKET_H: 
         # ボールの横の位置をプレーヤーのラケットの左に接触（ボールの中心が半径分左）した位置にする
         ball_x = player_x - BALL_R
         # ボールの横の進行方向のスピードを反転（左）にしてスピード１０％増やす
         ball_speed_x *= -1.1
         # ボールの縦の進行方向のスピードはボールの上方向の最速値から下方向の範囲ででたらめ（乱数）な値を設定する
         ball_speed_y = random.randrange(-BALL_SPEED_Y_MAX, BALL_SPEED_Y_MAX )
         
      # ボールの右へいくスピードが最速値を超えた場合
      if ball_speed_x > BALL_SPEED_X_MAX:
         # ボールの右へいくスピードを最速値にする
         ball_speed_x = BALL_SPEED_X_MAX
      # ボールの左へいくスピードが最速値を超えた場合         
      elif ball_speed_x < -BALL_SPEED_X_MAX:
         # ボールの左へいくスピードを最速値にする
         ball_speed_x = -BALL_SPEED_X_MAX
        
      #
      # スコアをつける
      #

      # ボールが左側を超えた場合
      if ball_x < 0:
         # プレーヤーのスコアを加算
         player_score += 1
         #　ボールの位置をプレーヤのラケット位置
         ball_x, ball_y= player_x - BALL_R, player_y + RACKET_H//2
         #　ボールのスピードを初期化
         ball_speed_x, ball_speed_y = -BALL_SPEED_X_MIN, BALL_SPEED_Y_MIN

      # ボールが右側を超えた場合
      elif ball_x > COURT_W:
         # コンピュータのスコアを加算
         computer_score += 1
         # ボールの位置をコンピュータのラケット位置
         ball_x, ball_y= computer_x + BALL_R, computer_y + RACKET_H//2
         #　ボールのスピードを初期化
         ball_speed_x, ball_speed_y = BALL_SPEED_X_MIN, BALL_SPEED_Y_MIN

      # GAME OVER判定
      # コンピュータかプレーヤーが勝ち点をとった場合

      if computer_score == WIN_SCORE or player_score == WIN_SCORE:
         # GAME OVER用フォント準備
         font=pygame.font.SysFont(None,FONT_SIZE_GAMEOVER)
         # GAME OVERメッセージ作成
         text=font.render("Game Over", True, COLOR_BLUE)
         # GAME OVERメッセージ表示
         screen.blit(text,(COURT_W//2-text.get_width()//2, COURT_H * 1//3))
         # 勝利メッセージ用フォント準備
         font=pygame.font.SysFont(None,FONT_SIZE_WINMESSAGE)
         # 勝利メッセージ用メッセージ作成
         text=font.render("You Win !!" if player_score==WIN_SCORE else "You Lost !!", True, COLOR_RED)
         # 勝利メッセージ表示       
         screen.blit(text,(COURT_W//2-text.get_width()//2, COURT_H * 2//3))
         # Game終了するため実行中かどうかの変数を実行終了（False）に設定
         run = False

      # 画面を更新
      pygame.display.update() 
      pygame.time.wait(30)

      for event in pygame.event.get():
         if event.type == QUIT:      # 閉じるボタンが押されたら終了
            run=False
         if event.type == KEYDOWN:
            if event.key == K_ESCAPE: #エスケープキーが押されたら終了
               pygame.quit()
               sys.exit()

   pygame.time.wait(6000)
   pygame.quit()
   sys.exit()

if __name__ == "__main__":
   main()
