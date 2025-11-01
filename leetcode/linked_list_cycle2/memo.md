# 142. Linked List Cycle II
https://leetcode.com/problems/linked-list-cycle-ii/description/

## Step1
### 問題の理解
- サイクルが始まるノードを探す
- set()にノードを入れていくやり方なら、簡単に書けるだろう

## Step2
### コードの整えについてのコメント集
- 関数化の仕方を注目してコードを読んで勉強する


### 他の方のコードを読む
https://github.com/hayashi-ay/leetcode/pull/18
- step1訪れたノードの集合を`seen`と命名している
  - 配列などは複数形にしたくなるけど、あまり重要ではないのか？
    - 命名において、読み手が何をわかっているか/いないかを把握できていない
- step2
  - set()を使ったコード
    - 「訪れたことのあるノードか」の判定の位置を気にしている。自然な処理の流れかどうかを気にしている
  - フロイドの循環検出法を使った解法
    - slow とfastポインタが合流したノードを返す処理を関数化
    - 関数の切り分け方がわかりやすいと感じた

https://github.com/MasukagamiHinata/Arai60/pull/5
- https://github.com/MasukagamiHinata/Arai60/pull/5/files#r2423337900
  - `has_cycle()`でTuple[bool, Optional[ListNode]] を返す関数化を行う改善案が自分の頭の中になかった

- https://github.com/docto-rin/leetcode/pull/1/files
  - 一歩ずつノードを進ませる手続きを関数化している
