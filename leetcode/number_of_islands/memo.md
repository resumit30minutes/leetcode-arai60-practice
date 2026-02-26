型
```
List[List[str]] -> int
```

問題文を読む
- 縦m x 横nのグリッドが与えられる
- "1" = 土地, "0" = 水とする
- 隣接する土地を縦横につないでいったのを1つの島とする（隣接するものはつないでいくので島の周りは水）
- grid外はすべて水とする
- 島の数を答えよ

  
まず想像したこと
- 解法の想像
  - 配列を走査していっって"1"を見つけたとき、それは必ず島の一部
    - なので、上下に探索して隣接している"1"を再帰的に"0"にしていく
    - 島の数のカウントを=+1
  - こうすれば解けるのでは

#### コードを読む
[200. Number of Islands by hayashi-ay · Pull Request #33 · hayashi-ay/leetcode · GitHub](https://github.com/hayashi-ay/leetcode/pull/33/changes)
- Union Find, 幅優先探索BFSで解く解法があった
- n^2 は避けられない。発見済みの島かどうかをどう記録しておくか

#### コメント集を読む
[200. Number of Islands by ichika0615 · Pull Request #9 · ichika0615/arai60 · GitHub](https://github.com/ichika0615/arai60/pull/9#discussion_r1954436002)
指摘
- UnionFind にそれぞれ抽象的には「初期化」「2つが繋がっているので繋いでくれ」「ある陸地の親はどこか」を連絡している
- しかし、実際に頼んでいることは、一般的な自然数添字の UnionFind へのお願い
- もうちょっと楽にしたいことを伝えられるはず

[Create 200. Number of Islands.md by quinn-sasha · Pull Request #18 · quinn-sasha/leetcode · GitHub](https://github.com/quinn-sasha/leetcode/pull/18#discussion_r1997515140)
キューを利用して訪問済みの島を記録するときの問題

[200. Number of Islands by sakupan102 · Pull Request #18 · sakupan102/arai60-practice · GitHub](https://github.com/sakupan102/arai60-practice/pull/18#discussion_r1582241335)
- 構造の把握 numIslands: `List[List[int]] -> int`
  - number_of_islands: 島の数
  - visited: 陸であると確認済みの座標一覧
  - inside_island: 範囲内か
  - is_island: 島の一部か
  - visit_island: ある起点座標（陸）から、同じ島の一部の座標を記録せよ
  - : すべての座標について、島の一部であり未確認な 物を見つけた場合、
    - 同じ島の一部である座標をすべて記録せよ
    - 島の数を1つ増やせ
- visit_islandの入力に「必ず陸の座標が渡される」とい暗黙の想定を持ち込んでいる




### 調べたこと
UnionFind
[素集合データ構造 - Wikipedia](https://ja.wikipedia.org/wiki/%E7%B4%A0%E9%9B%86%E5%90%88%E3%83%87%E3%83%BC%E3%82%BF%E6%A7%8B%E9%80%A0)
- UnionFindに対して行われる操作
  - Find: 特定の要素がどの集合に属しているかを求める。2つの要素が同じ集合に属しているかの判定にも使われる。
  - Union: 2つの集合を1つに統合する。
- 計算量を減らす工夫（後で詳しく学習）
  - union by size
  - 経路圧縮
