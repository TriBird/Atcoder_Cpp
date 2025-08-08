## 概要
- online-judge-toolsを導入したWSL環境を想定
- 整備してないので普通には使えません。検索で来た人は申し訳ない。
- WatchかStarが来たら対応するかも
- Ratedで使う場合にはatcoder規約に注意

## How to Use
1. acinit [contest_id]で環境作成
1. コードを書く、デバッガも使用可能
1. actest [a-g]でチェック、全PASSならコードがクリップボードに自動コピーされる
1. 提出すれば良し

actestは直前に叩かれたacinitかaccdを参照して自動でディレクトリを選択する。  
accd [contest_id]でactestのディレクトリ参照を操作できる

以上