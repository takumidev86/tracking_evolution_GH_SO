# tracking_evolution_GH_SO

This repository is a tool to determine if GitHub, written in python3, is keeping up with the evolution of StackOverflow.

# Abstract

SOTorrent の情報あるいは今回用いたスクリプトを解読して変更履歴を追う

# dev command memo

これを使うと文字を含むコミットを表示することができる

```bash
git log -S  "python"
```

```json
~/w/tracking_evolution_GH_SO ❯❯❯ git log -S  "python"

commit cc5ededfcf56d1be1db5fc030056c8896771be3d
Author: takumidev86 <takumidevelopment86@gmail.com>
Date:   Wed Mar 3 01:52:56 2021 +0900
```

[git log のフォーマットを指定する - Qiita](https://qiita.com/harukasan/items/9149542584385e8dea75)

```bash
#色々オプションをつけてコミット情報を出力
~/w/tracking_evolution_GH_SO ❯❯❯ git log --pretty=format:"[%ad] %h %an %cd"
[Wed Mar 3 02:16:05 2021 +0900] 0fc51f4 takumidev86 Wed Mar 3 02:16:05 2021 +0900
[Wed Mar 3 01:52:56 2021 +0900] cc5eded takumidev86 Wed Mar 3 01:52:56 2021 +0900

#文字列を含む(-S) コミット時間を出力
~/w/tracking_evolution_GH_SO ❯❯❯ git log -S  "python" --pretty=format:" %cd"
 Wed Mar 3 01:52:56 2021 +0900

# stackoverflow.comが含まれるコミットを検索
~/w/G/j2objc-gradle ❯❯❯ git log -S  "stackoverflow.com" --pretty=format:"[%ad] %h %an %cd"
[Sat Jan 9 17:14:55 2016 -0800] 4a1f876 Bruno Bowden Tue Jan 12 00:20:49 2016 -0800
[Sat Oct 24 17:36:58 2015 -0700] 0da1235 Bruno Bowden Sat Oct 24 17:44:27 2015 -0700
[Wed Oct 21 15:19:08 2015 -0700] e33e86e Bruno Bowden Thu Oct 22 17:42:17 2015 -0700
[Tue Aug 25 16:31:06 2015 -0700] a3cb3e2 Bruno Bowden Wed Aug 26 02:41:59 2015 -0700
[Sun Aug 23 18:01:46 2015 -0700] 0593019 Bruno Bowden Sun Aug 23 22:19:15 2015 -0700
[Mon Jun 29 11:28:09 2015 -0700] cc47a2b Bruno Bowden Tue Jul 14 07:25:41 2015 -0700
[Tue Jun 2 16:41:41 2015 -0700] 5aa63ff Bruno Bowden Tue Jun 2 17:54:06 2015 -0700
[Wed Apr 22 23:35:31 2015 -0700] 321e5ae Bruno Bowden Wed Apr 22 23:35:31 2015 -0700
[Mon Apr 13 12:12:49 2015 -0700] 347dbc3 Bruno Bowden Mon Apr 13 12:12:49 2015 -0700
[Fri Apr 10 15:17:40 2015 +0200] bed7005 Confile Fri Apr 10 15:17:40 2015 +0200
```

# 設計

- SO の履歴：
  - SOTorrent の情報あるいは今回用いたスクリプトを解読して変更履歴を追う
- GH の履歴：
  - git log コマンド等を使って SO のリンクが追加されたタイミングを追う
    - https://qiita.com/genre/items/86cf7802c4abc6fa4c1e
- 処理手順
  - １．SO のリンクが GH 側に追加されたタイミングを基に，SO の再利用元のバージョンを特定する（追加されたタイミングより古い中で最新のバージョン）
  - ２．SO 側の再利用元のバージョンが最新版か判定を行う
    - 再利用元バージョン＝ SO の最新版の場合
      - ユーザは最新の SO 投稿を利用している →（処理終了）
    - 再利用元バージョン！＝ SO の最新版の場合
      - SO 投稿が進化しているので，さらに追跡する必要あり（STEP3 へ）
  - ３．SO のリンクが追加されているファイルの変更履歴を追い，GH 側が SO の進化を反映しているか調査する
    - ファイルの変更履歴を `git log -p` 等で追う（リンクの追加タイミングより新しい履歴のみ）
    - ファイルが変更されてない場合：
      - GH 側は SO 側の変更を取り込んでいない →（処理終了）
    - ファイルが変更されている場合
      - 変更履歴を目視で確認し，SO 側の最新の変更を取り込んでいるか判定 →（処理終了）
