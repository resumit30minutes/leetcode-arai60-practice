## Step1
- 先頭のノードの値を足す。10以上であればそれを考慮して足し続ける
- 17分

## Step2
- 参考：https://github.com/hayashi-ay/leetcode/pull/24/files
- ノードがNoneの時の場合の処理が違う
- 返り値の命名を変更してみた
- 繰り上がりが発生するかどうかのif文は残しておいた。けど、やはり↓のやり方のほうが簡潔でいいのだろうか
```python
current.next = ListNode(total % 10)
carry = total // 10
```
- 'x is not None'が無ければ不安なのは、Pythonに慣れてなくてどういう真偽値の判定の仕様なのかちゃんと調べてないからだろう。後で調べる