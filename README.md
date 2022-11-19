# ディーラーボット

## 目標

スマホを使って1つのボタンを押すと、自動的に各プレイヤーに移動してカードを配る


## 必要なパーツ
- ラズベリーパイ 4b
- Anker PowerCore 10000
- 単3電池 x4
- DCモーター　x3
- L293Dドライバー x2
- ブレッドボードや 基板＋はんだつけ　
- タミヤ　タンク工作基本
- 回路のケーブル
- ディーラーボットのボディを作るためのマテリアル


## 動き方

- FLASKのウェブアプリケーションにWIFIで繋げて、プレイヤーがスマホで1つのボタンを押すだけで
  ディーラーボットは選ばれたプレイヤーに移動して適当な枚数を配ってくれる。
- 今度の書いた[「コード」](https://github.com/kneckebrodet/dealerbot/blob/main/dealerbot.py)は真っ直ぐに前向きと後ろ向きに移動しているが、
  自分が好きな方向や各ゲームのための動き方を簡単に設定することができる。


## プロジェクトの作り方手順

- FLASK のライブラリをラズベリーパイにインストールする （ターミナルで「pip install flask」) 
- [1番目の回路を組み合わせ](https://github.com/kneckebrodet/dealerbot/blob/main/%E5%9B%9E%E8%B7%AF%E7%94%BB%E5%83%8F/DualMotors.jpg)(タイヤのための回路)
- 作った回路とディーラーボットの下部分を組み合わせ
- [2番目の回路を組み合わせ](https://github.com/kneckebrodet/dealerbot/blob/main/%E5%9B%9E%E8%B7%AF%E7%94%BB%E5%83%8F/DealerArm.jpg)(ディーラーアームのための回路)
- ディーラーボットの上部分を組み合わせ
-  [「HTMLコードを書く」](https://github.com/kneckebrodet/dealerbot/blob/main/home.html)と[「ソースコードを書く」](https://github.com/kneckebrodet/dealerbot/blob/main/dealerbot.py)


## 操作

スマホでラズベリーパイとの同じWIFIをつなげて、"http://0.0.0.0:5000/" のURLを入れて、ホームページのボタンで操作をすることができる


## リンク

[ ProtoPedia ] :               https://protopedia.net/prototype/3484

[ Source code (python) ] :     https://github.com/kneckebrodet/dealerbot/blob/main/dealerbot.py

[ Source code (html) ] :       https://github.com/kneckebrodet/dealerbot/blob/main/home.html


## 作者

[Kneckebrodet] : https://github.com/kneckebrodet
