# ディーラーボット

## 目標

スマホを使って1つのボタンを押すと、自動的に各プレイヤーに移動してカードを配る


## 必要なパーツ
- ラズベリーパイ
- DCモーター　x3
- L293Dドライバー x2
- ブレッドボードや 基板＋はんだつけ　
- タミヤ　タンク工作基本
- 回路のケーブル
- ディーラーボットのボディを作るためのマテリアル



## 動き方

- FLASKのウェブアプリケーションにWIFIで繋げて、プレイヤーがスマホで1つのボタンを押すだけで
  ディーラーボットは選ばれたプレイヤーに移動して適当な枚数を配ってくれる。
- 今度の[書いたコードは](https://github.com/kneckebrodet/dealerbot/blob/main/dealerbot.py)

## Workflow of the Project

- When the simulation is started, and any one of previous and next button is pressed the DC motor changes it's direction      accordingly.
- If next button is pressed, it will rotate clockwise. And if previous button is pressed, it will rotate anti-clockwise.


## Setup instructions

- Use Tinkercad
- Setup a circuit as shown in the circuit diagram in images folder
- Write the code as given
- Start simulation
- Press the next button on IR remote
- Observe rotational direction of DC motor
- Now, press the previous button on IR remote
- Observe the change in direction of DC motor.


## Output



[circuit diagram]:    https://github.com/vaishnavighiradkar/Controll_dc_motor_using_IR/blob/main/circuit%20diagram.png


//Click on view raw

[Simulation Video]:   https://github.com/vaishnavighiradkar/Controll_dc_motor_using_IR/blob/main/simulation%20video.zip

[ Source code ] :     https://github.com/vaishnavighiradkar/Controll_dc_motor_using_IR/blob/main/code.ino

## Author

[Vaishnavi Ghiradkar] : https://github.com/vaishnavighiradkar



