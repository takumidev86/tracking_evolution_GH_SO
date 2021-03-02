# tracking_evolution_GH_SO

This repository is a tool to determine if GitHub, written in python3, is keeping up with the evolution of StackOverflow.

# Abstract

SOTorrent の情報あるいは今回用いたスクリプトを解読して変更履歴を追う

# dev memo

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
