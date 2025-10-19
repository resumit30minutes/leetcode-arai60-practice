# Pythonのheapqライブラリを読む

## リソース
- https://docs.python.org/ja/3/library/heapq.html
- https://github.com/python/cpython/blob/3.13/Lib/heapq.py
- https://github.com/python/cpython/blob/3.13/Lib/test/test_heapq.py

## ドキュメントを読む

### 教科書的なヒープの実装と違う点
- a. 
- b. 

### ヒープの初期化
- 通常のリストをheapify()でヒープ化できる
- 空リストをヒープとして操作できる

### 理論
- ヒープとは、全ての k について、要素を 0 から数えたときに、a[k] <= a[2*k+1] かつ a[k] <= a[2*k+2] となる配列
- 勝ち抜き戦の比喩 がよくわからない。勝ち抜き戦の話自体がピンとできてない
- 効率的なソートをするためのデータの保持の仕方を説明している
- 他のソートをする方法との比較


「heapは、startpos以上のすべてのインデックスでヒープです。ただし、posは例外かもしれません。posは、順序が崩れている可能性がある値を持つ葉のインデックスです。ヒープの不変条件を回復させます。」

```python
def heappush(heap, item):
    """Push item onto heap, maintaining the heap invariant."""
    heap.append(item)
    _siftdown(heap, 0, len(heap)-1)
```     

```python
# 'heap' is a heap at all indices >= startpos, except possibly for pos.  pos
# is the index of a leaf with a possibly out-of-order value.  Restore the
# heap invariant.
def _siftdown(heap, startpos, pos):
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem
```

- 入力
  - heap: List
  - startpos: int
    - startpos以上のインデックスの要素はヒープの不変条件を満たしている
  - pos: int
    - 不変条件を満たしていない例外の箇所
- 出力
  - 返り値なし
  - heapのデータを操作する

- ヒープの末尾に追加された要素など、本来あるべき場所よりも下層にある「小さい」要素を、親ノードと比較しながら適切な位置までせり上げていく処理です。


### 例を作ってみる
- ./test.py を参照
> ヒープとは、全ての k について、要素を 0 から数えたときに、a[k] <= a[2*k+1] かつ a[k] <= a[2*k+2] となる配列
```
     0
   1   2
 3   4    5
6 7 8 9 10 11
```