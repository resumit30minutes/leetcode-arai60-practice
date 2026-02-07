問題：https://leetcode.com/problems/unique-email-addresses/description/
参考：https://github.com/hayashi-ay/leetcode/pull/25/changes

## Step1
- 途中から自分で解いてみた。
- フラグを使って1文字ずつ処理する方法と、特殊な文字が来たときに、その文字に対応するルールをまとめ適用するか判断が分かれそう

- local name
  - '.', 削除
  - 	- '+', それ以降の文字列を削除
- domain name

string list -> int

### 手作業・シフトを組んだ作業の指示
- 1文字ずつ見ていく
- 特殊な文字に


### 他の人のコード・コメントを読む

[929. Unique Email Addresses by colorbox · Pull Request #28 · colorbox/leetcode · GitHub](https://github.com/colorbox/leetcode/pull/28#discussion_r1844242082)
- 変数の破壊的な変更について
  - ある値をコピー・そのコピー値を渡した関数内では破壊的変更している
  - 整合性をとる
[929. Unique Email Addresses by seal-azarashi · Pull Request #14 · seal-azarashi/leetcode · GitHub](https://github.com/seal-azarashi/leetcode/pull/14/changes#r1676988400)
[929 Unique Email Addresses by Yoshiki-Iwasa · Pull Request #13 · Yoshiki-Iwasa/Arai60 · GitHub](https://github.com/Yoshiki-Iwasa/Arai60/pull/13#discussion_r1649832719)
- ユースケースを考える
- コーディング練習だと割と抜けてしまうかも。acceptされるか・読みやすさを考えがち
- ローカル部分・ドメイン部分が存在するかはまず確認していいかも
[Unique email addresses by SuperHotDogCat · Pull Request #30 · SuperHotDogCat/coding-interview · GitHub](https://github.com/SuperHotDogCat/coding-interview/pull/30#discussion_r1646552062)
- RFCを読もう
- Internet Message Formatかな？
  - [メールに関する主要なRFCとは？ 違反しがちなポイントをチェック - ベアメールブログ](https://baremail.jp/blog/2024/05/14/3791/)
[Add 929. Unique Email Addresses by t0hsumi · Pull Request #14 · t0hsumi/leetcode · GitHub](https://github.com/t0hsumi/leetcode/pull/14#discussion_r1929544842)
> 比較のために正規化しているため canonicalize のほうが良いと思います。内部的な冗長さの削減のために正規化するのを normalize と呼ぶようです。
