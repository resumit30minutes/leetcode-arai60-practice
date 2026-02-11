問題：[First Unique Character in a String - LeetCode](https://leetcode.com/problems/first-unique-character-in-a-string/description/)
参考：https://github.com/hayashi-ay/leetcode/pull/28/changes


目標: arai60を写経した後はもう一周するつもりなので、コメントやコードを読む時間をある程度は少なくしたい

string -> int

条件に当てはまる**一番初めの**インデックスを返す
- 条件. 文字列中に同じ文字が現れない

自分が思い浮かんだ解法
- 文字を索引としたインデックスのマップを作る
- 同じ文字が現れれば、ハッシュマップから削除
- 走査が終わった段階で、一番小さいインデックスを返す
	- 辞書は挿入順が保持されるので、それを利用できるかもしれない


### 他の人のコード・コメント集を読む
[387. First Unique Character in a String by hayashi-ay · Pull Request #28 · hayashi-ay/leetcode · GitHub](https://github.com/hayashi-ay/leetcode/pull/28/changes)
- 1st それぞれの文字列（の数値化） -> 出現数を長さ26のリストに記録
	- 文字列を走査して、条件に当てはまったら答えを返して終了
- 4-1 `next(iter)`

[leetcode/387/step2\_3.cpp at 1fdb87356938b312be64bae5583e0095d0bd3530 · colorbox/leetcode · GitHub](https://github.com/colorbox/leetcode/blob/1fdb87356938b312be64bae5583e0095d0bd3530/387/step2_3.cpp)
- ソートで
- 空間計算量が小さいのが利点? 読みやすさはハッシュマップの方が上と感じた

[Discord](https://discord.com/channels/1084280443945353267/1233603535862628432/1237823214168576112)
- LinkedHashMap

```
で、色々な方法があると思うんですが、「何の文字が、もう出現したかを書き留めておくホワイトボード」「まだ1回しかでていない文字とそれが出た日付の書かれたホワイトボード」があれば、「仕事にならない」とは叫ばないと思うんですよ。
で、終わったら条件に当てはまる文字を探すのです。ただ、他にどんな可能性がありますか?
```

[Discord](https://discord.com/channels/1084280443945353267/1195700948786491403/1231538588529852426)
- 重複の確認と、重複していない要素のインデックスを別のデータ構造で行っている
- 1つのハッシュマップでやるよりわかりやすい？
### 知らなかった/調べた知識
- `next()`, `iter()`
- LinkedHashMap
