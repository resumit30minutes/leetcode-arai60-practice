問題：https://leetcode.com/problems/max-area-of-island/description/
参考：https://github.com/t0hsumi/leetcode/blob/088154cf58cb3d6418e634913094aee9a1f1dca7/695.%20Max%20Area%20of%20Island.md

### 問題の整理
- `List[List[int]] -> int`
- 縦横で地続きになっている土地=島
- 島の中で、一番多い土地の数

[[200.Number of Islands]]と解法は変わらないように見える
	- 確認済みの島の管理＋島の土地の数のカウント
### コメント・コードを読む
- [695. Max Area of Island by hayashi-ay · Pull Request #34 · hayashi-ay/leetcode · GitHub](https://github.com/hayashi-ay/leetcode/pull/34/changes)を読む

[Add 695. Max Area of Island.md by t0hsumi · Pull Request #19 · t0hsumi/leetcode · GitHub](https://github.com/t0hsumi/leetcode/pull/19#discussion_r1934929811)
> 同じ意味のものが繰り返しているときには [] のほうが多い気がします。Tuple も immutable という点ではいいかもしれません。

[695. Max Area of Island by colorbox · Pull Request #32 · colorbox/leetcode · GitHub](https://github.com/colorbox/leetcode/pull/32#discussion_r1898178545)
>stack に追加する前に範囲チェックをするのも一つです。  
問題によっては計算量が変わることもあります。
そうすると、範囲チェックをして追加という、同じ処理が繰り返されるので関数化をしたりラムダにしたりするのがいいでしょう。
