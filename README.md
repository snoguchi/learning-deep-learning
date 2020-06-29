# learning-deep-learning

オライリーの[ゼロから作るDeep Learning](https://www.oreilly.co.jp/books/9784873117584/)を読んだ＆写経したメモ

![](https://www.oreilly.co.jp/books/images/picture978-4-87311-758-4.gif)

## Python
- [numpy気持ち悪い](numpy.ipynb)

## ch02
- パーセプトロンで論理回路
  - 単層パーセプトロンでANDやORなどの論理回路を表現できる
  - 単層パーセプトロンではXORは表現できない
  - 2層のパーセプトロンではXORを表現できる
- 単層 vs 多層
  - 単層のパーセプトロン = 線形領域しか表現できない
  - 多層のパーセプトロン = 非線形領域を表現できる = XORのような難しい？問題を解ける

## ch03
- 3.2 活性化関数
  - ノードに入力された入力信号の総和を出力信号に変換する関数
    - ステップ関数（線形）
    - シグモイド関数（非線形）
    - ReLU関数（非線形）
  - 多層パーセプトロン＝ニューラルネットでは、活性化関数は非線形でないと意味がない
    - 線形関数だと多層は一層にまとめられちゃって隠れ層の意味がなくなるから
- 3.3 多次元配列演算
  - ニューラルネットの計算（入力信号から出力信号を算出する）を効率的に実行するために必要
  - 例えば、1層目が784個、2層目が100個のニューラルネットは、重みパラメータが 784 x 100 個出てくるので、これを(784, 100)の行列として扱い、行列演算が最適化されたnumpyで演算できると早かったりするのだろう
- 3.5 出力層
  - 出力層の特別な活性化関数
    - 回帰問題 → 恒等関数
    - 分類問題 → ソフトマックス関数（出力値の総和に対する割合、出力が確率になる）
- 3.6.3 バッチ処理
  - 入力信号を「束」にまとめる
  - コンピュータで計算するときの効率にメリットがある（ライブラリの最適化など）

## ch04
- 4.2 損失関数
  - ニューラルネットワークの性能の悪さを示す指標。現在のニューラルネットが教師データに対してどれだけ適合してないかを表す
- 4.2.3 ミニバッチ学習
  - 訓練データの一部（＝ミニバッチ）を抽出して（一部のデータを全体の近似として）学習を行うこと
- 4.4 勾配
  - すべての変数の偏微分をベクトルとしてまとめたもの
  - 関数のある地点において「関数の値を最も減らす方向」
  - 必ずしも関数の最小値ではないことに注意
- 4.4.1 勾配法
  - 現在の場所から勾配方向に一定の距離だけ進む、を繰り返して、関数の値を徐々に小さくしていく
  - ニューラルネットの学習＝損失関数の値を最小化する問題を解くのに使われる
- 4.4.1 学習率
  - 勾配法で進む距離（勾配に対する係数）。ハイパーパラメータの一種
- 4.5 確率的勾配降下法

## ch05
- 計算グラフ
  - 逆方向の伝搬により「微分」を効率よく計算できる
  - 微分：リンゴの値段が "少しだけ" 値上がりした場合に、支払金額がどれだけ増加するか、ということを表したもの
  - つまり：NNにおいて、重み(`W`)が "少しだけ" 変化した場合に、損失関数がどれくらい変化するか、が効率よく計算できる

