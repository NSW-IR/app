# Claude codeとは
- ターミナル上で動作するAIコーディング支援ツール
- 自然言語での指示に基づいてコードの生成、編集、テスト、Git操作などを支援する

# 導入方法
- 前提条件
    - 事前にanthropicアカウントを発行、ProまたはMaxライセンスを購入する必要あり

1. 作業ディレクトリに移動して下記コマンドを実行、ClaudeCodeをインストールする
    - linuxの場合
        - ``` curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash - ```
        - ``` sudo apt-get install -y nodejs ```
        - ``` sudo npm install -g @anthropic-ai/claude-code ```
    - Windowsの場合
        - ``` npm install @anthropic-ai/claude-code@latest ```

1. 下記コマンドでclaude起動
    - linuxの場合
        - ``` claude ```
    - Windowsの場合
        - ``` npx claude ```

1. テーマ設定

    ```1. Choose the text style that looks best with your terminal:```
    - 見栄えの設定のため好みのモードを選択。こだわりがないのであれば 1.Dark modeを選択

1. ログイン

    1. ```Select login method:```
        - '1. Claude account with ～　を選択
        - ブラウザが開くので「承認」　※anthropicにログインしていない場合はログイン
        - エラーなどになる場合下記のメッセージ配下のURLにアクセスし
            - ``` Browser didn't open? Use the url below to sign in:```
            - そこからCopy codeしたものを、vscode側の```Paste code here if prompt```にペースト

        - ``` Login successful. Press Enter to continue…```が表示されればログイン成功。Enterで続ける
        - **※2. Anthropic Console account を選択するとAPIによる従量課金での利用となってしまうので必ず1.を選択すること**

1. ``` Security notes:```
    - Enter

1. ``` Use Claude Code's terminal setup? ```
    - ``` 1. Yes, use recommended settings ```を選択

1. ```Welcome to Claude Code!   ```が表示されればセットアップ完了

1. セットアップ後、/status　と入力
    - Accountの項に「Login Method: Claude Pro/Max Account」と表示されていればOK

- 追記：直近のアップデートでセキュリティポリシーが変更され、以下のダイアログが表示されるように
    - ```Please select how you`d like to continue```
    - ```Your choice takes effect immediately upon confirmation.```
    - **コードを学習に使用するかの選択肢になるので、必ず「2.Accept terms ・ Help improve Claude: OFF」を選択**
    - 誤って「1」を選択した場合、下記URLにアクセスして「チャットやコーディングセッションのデータをAnthropic AIモデルの訓練と改善に使用することを許可します。」トグルをOFFにすること
    - https://claude.ai/settings/data-privacy-controls 


# 禁止事項
- 【実施禁止】``` claude --dangerously-skip-permissions ```
    - コマンド確認を全スキップさせるオプション
        - 意図しない破壊的なアクションやセキュリティ的に致命的な漏洩につながる可能性があるため禁止

- 【実施禁止】開発者パートナーシップに参加する
    - https://console.anthropic.com/settings/privacy
        - Join our Development Partner Program to help improve Claude
    - トークン消費が割引になるがI/OがLLMの学習に使用されるようになるため禁止

# 大前提
- claude codeが作成したコードであってもプロジェクト上は製造者が製造したコードとして扱うためその責任を持つこと
    - 必ず自動生成/修正されたコード内容はすべて理解/把握する
    - レビュー時や単体試験時に「そこはAIが勝手に作ったのでわかりません」という状況になるのはNG

- 生成されたコードは過信しない
    - 構文エラー/論理バグ/セキュリティ脆弱性/既存パーツへの配慮不足などのリスクがあるため、必ず内容を精査してから使用すること
    - 期待する成果の6-7割ほどの出来のものが出力されるぐらいの心構えをしておくこと

# 使用方法
## Claude Code使用開始前の初期設定について
- CLAUDE.md
    - ルートディレクトリに配置、PJ内での決まり事を記載することで処理のたびにClaude Codeが記載内容を読込み、ルールを順守してくれる
    - 記載内容はPJ単位に異なるため調整が必要、例として以下のような内容を記載する
        - 使用するコマンドやスクリプト（ビルド、テスト、リント等）
        - ファイル作成・編集ルール
        - その他、守ってほしい振る舞いや制約等（パスワードはコード中にハードコーディングしないこと…など）

- setting.json
    - ルートディレクトリに配置、Claude codeの細かい設定が可能
    - 特にシステムコマンドの権限管理は要設定
    - 基本的にはコマンド実行前にユーザー側へ確認を行うが、allowに設定したコマンドは確認無しで実行するようになり、denyに設定したコマンドは実行不可となる
    - 使用頻度の高いコマンドはallowに設定し、「rm -rf」等の破壊的な操作を行うコマンドはdenyに設定しておく

## 命令方法
- ![alt text](./参考画像/claudeUI.png)
    - Consoleに命令を入力
    - ChatGPTのように質問するのではなくコード生成を支持する使い方がメイン。指示すると既存コードをgrepして解釈し、必要なコードをすべてファイルとして格納してくれる
        - Consoleへ出力するのではなく実コードファイルとして作成、更新することが可能
        - 修正を内容についてはgitの差分で確認する
        - **gitにステージしていない状態で変更を行うと元の状態に戻せなくなるため注意すること**

## 作業計画
- 作業の実施前にclaude codeは作業の実施計画を立てる。内容が問題ない場合は「y」と一言返す。（yesの意図が伝わるのであれば「お願いします」とかでもよい）
- 問題がある場合は「n」と返す。一緒にどこがだめかも併記する（n checkstyleMainのほかにbuildエラーも確認　など）

```
  CheckStyleエラーを直すために以下の作業を実行します：

  1. checkstyleMainタスクを実行してエラー内容を確認
  2. 発見されたエラーを修正
  3. 修正後に再度checkstyleMainを実行して問題解決を確認

  この計画で進めてよろしいですか？ (y/n)
```

## コマンド実行確認
- claude codeはlinuxコマンドの実行前にユーザに確認を取る
    - 実行しても問題ない場合：1を選択
    - 実行しても問題ない、かつ今後同じコマンドの確認をスキップする場合：2を選択
    - 実行NGの場合：3を選択

```
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Bash command                                                                                                                                        │
│                                                                                                                                                     │
│   cat build.gradle                                                                                                                                  │
│   Display contents of build.gradle file using cat command                                                                                           │
│                                                                                                                                                     │
│ Do you want to proceed?                                                                                                                             │
│ ❯ 1. Yes                                                                                                                                            │
│   2. Yes, and don't ask again for cat commands in /workspaces/app                                                                                   │
│   3. No, and tell Claude what to do differently (esc)                                                                                               │
╰─────────────────────────────────────────────────────────
```

## 処理を止める
- Esc二回入力で処理を止める。
    - 処理を止めてもその途中までの作業内容がロールバックするわけではないので注意

# プロンプト例

## 0ベースから機能作成
- 画面設計書をPDF化してXXX.pdfとして開発環境上に設置

- ```@XXX.pdf この設計書を見て機能を実装して。stocksetを参照して作成すること```
    - サンプルとなる機能を例示するのがポイント。和名（棚卸管理）ではなくpackage名（stockset）で提示してあげること

## セルフレビュー
- ``` 〇〇機能をXXX機能と比較してレビューして ```

## 機能修正
- ```XXXのプルダウンリストの取得は共通関数のXXXXを使って。取得時のcategorycodeにはXXXXXを渡すこと```

## エラー修正
- エラー内容を貼り付ける（どこでエラーが出ているかわかる範囲まで貼り付ける）
    - 大量にテキストを貼り付けると[Pasted text #1 +XXX lines]とコンソールに入力されているように見える。長いので省略表示されているだけで実際には正常に入力できている

## レビュー指摘修正
- ``` https://techhub-gitlab01.sardine-swarm.net/IM/md/app/-/merge_requests/86  このmergeリクエストのコメントに対して修正して。コメントの取得にはgithubAPIを使用すること。 ```
    - 全コメントをまとめて修正してくれるので便利だが修正内容は鵜呑みにしないこと。見当違いの修正を行っている可能性あり。

## checkstyle/buildエラーの修正
- ``` checkstyle/buildエラーを修正して ```

## 別ブランチ参照
- ``` feature/req-XXXX のブランチにあるXX機能の商品検索モーダル（XXX）を真似して、現在のブランチのXXX画面のXXXX項目に同じモーダルを組み込んで  ```

# コツやノウハウ
## 画像を送る
- ターミナル上から画像を直接アップはできないが、スクリーンショットの画像を開発環境に置き、そのファイルパスを連携するとClaude codeが画像を読み込める

## 連続した会話が苦手であることを意識する
- Claudecodeに関わらずLLMは連続した会話が苦手で、最新の発言を優先的に処理し、過去の命令はその重要度に関わらず失念しやすい
    - 一度の応答ごとに記憶喪失になり、都度これまでの会話履歴から流れを汲み取っているイメージ
- 「前に言ったことを覚えていない」のは当たり前なので重要前提事項があるなら都度連携をする

## より具体性的な指示を出す
- 具体度の低いあいまいな指示を出すと、意図していない対応を行いやすい
- 指示内容については可能な限り具体的に指示を出すのが望ましい

## 画面生成には見本を見せる
- 画像の参照はある程度できるが微妙にその通りに作ってくれない
- サンプル機能やデザインHTMLを参照させるなど見本のコードを見せるとよい

## トークン制限
- claude codeにはトークン制限があり、上限に達するとエラーを返す
- このトークンは5時間サイクルの使用量で換算されており、その時間内で上限に達すると次にサイクルに入るまで使用制限がかかる
    - 後述の拡張思考モードでがっつり製造すると2時間ほどで上限に達する感触

## 拡張思考モード（ultrathink）
- 命令に「ultrathink」という文字を入れると拡張思考モードで処理を行う
- 拡張思考ではより深くまで思考した上でアクションを行うのでかなり丁寧かつ的確な動きをする
- ただし通常の10倍のほどのトークンを消費してしまい上記トークン制限がかかりやすくなるため、なかなかclaudecodeが解決してくれないバグや大規模なリファクタリングなどに限定することをおすすめ
    - または業務終了の直前にultrathinkで依頼するなど

## 会話の再開
- 以前の会話を再開したい場合はターミナルから下記実施で履歴を選択
    -   ``` claude --resume ```

## 会話の開始方法
- ターミナルから下記実施で新規で会話を開始
    -   ``` claude ```

- またはvscodeのファイルタブの右上あたり、オレンジのウニみたいなマーク(![alt text](./参考画像/claudeIcon.png))からも開始可能

    - ![alt text](./参考画像/claude起動方法.png)
    - ウニマークから起動した場合のみ、vscodeと連動してファイルの選択状態などもclaude codeに送られるようになるのでソースの該当箇所を選択して「ここ直して」というような使い方もできるようになる