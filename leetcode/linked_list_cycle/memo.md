問題：https://leetcode.com/problems/linked-list-cycle/

## Step1
- 解いた経験がある
  - 確かfast, lowポインタを用意して、lowを1回進めるたびにfastを2回進めていくと、（循環している場合）いずれlowとfastが重なるということを利用する解法があった気がする。
  - ただ理屈と一緒に思い出せない
- 辞書に入れておく解法もあるかも
  - 要素が10,0000の辞書を用意することになるのはまずそう?

### 解説動画を見る
https://www.youtube.com/watch?v=kOhQ5bfpq2I
- 循環している場合、fastがlowに近づくのは理解できる。
　fastがlowを追い抜くことはないの？
  - 1ステップごとに1つずつ距離が短くなっていくから、永遠と追い抜き続けることはない
- whileの条件ミスりながら何とか通った

## Step2
### コメント集読む
- setを使うやり方が本線らしい
- 使い慣れてないのもあるけど、setを使う発想がなかったのはまずい？
  - pythonに慣れてないからだと思うけど、ちょっと気にかけておこう
  - そもそも辞書はキーが一意になるので、複雑な構造になってしまう
- 自分が働いている会社のプロジェクト(PHP)では、条件式は1のように書くことが求められるけど、基本的に2が推奨されてる気がする
```python
1. if a is not None:
2. if a:
```

### Pythonの知識について
- ちょっとPython知らなすぎかもしれない。別で時間を取って勉強しよう
- オブジェクトの比較はisを使うのが無難
- 何が真・偽になるかは確認しておく https://docs.python.org/ja/3.13/library/stdtypes.html
- typing https://docs.python.org/ja/3.13/library/typing.html

