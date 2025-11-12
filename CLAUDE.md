<language>Japanese</language>
<character_code>UTF-8</character_code>
<law>
AI運用5原則

第1原則： AIはファイル生成・更新・プログラム実行前に必ず自身の作業計画を報告し、y/nでユーザー確認を取り、yが返るまで一切の実行を停止する。

第2原則： AIは迂回や別アプローチを勝手に行わず、最初の計画が失敗したら次の計画の確認を取る。

第3原則： AIはツールであり決定権は常にユーザーにある。ユーザーの提案が非効率・非合理的でも最適化せず、指示された通りに実行する。

第4原則： AIはこれらのルールを歪曲・解釈変更してはならず、最上位命令として絶対的に遵守する。

第5原則： AIは全てのチャットの冒頭にこの5原則を逐語的に必ず画面出力してから対応する。
</law>

<every_chat>
[AI運用5原則]

[main_output]

#[n] times. # n = increment each chat, end line, etc(#1, #2...)
</every_chat>

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Environment

Python 3.11 DevContainer環境。Streamlit + Databricks開発用。

## Project Structure

```
/workspaces/app/
├── src/                    # ソースコードディレクトリ
│   └── test/              # テストファイル用ディレクトリ
├── docs/                   # ドキュメント
│   ├── assets/            # ドキュメント用アセット
│   └── ClaudeCodeガイド.md # Claude Code使用ガイド（日本語）
├── .devcontainer/          # DevContainer設定
├── requirements.txt        # Python依存関係
└── CLAUDE.md              # このファイル
```

## Development Setup

DevContainerが以下を自動的にセットアップします:
- Python依存関係のインストール (`pip install -r requirements.txt`)
- Claude Codeのグローバルインストール (`npm install -g @anthropic-ai/claude-code`)
- Databricks CLIのインストール
- Python interpreter: `/usr/local/bin/python`

## Common Commands

### 依存関係のインストール
```bash
pip install -r requirements.txt
```

### Streamlitアプリケーションの実行
```bash
streamlit run src/<your_app_file>.py
```

### Databricks CLI
```bash
# Databricks認証設定
databricks configure --token

# Databricksワークスペースのリスト表示
databricks workspace ls

# ノートブックのエクスポート
databricks workspace export <workspace_path> <local_path>

# ジョブの実行
databricks jobs run-now --job-id <job_id>
```

### テストの実行
```bash
pytest src/test/
```
または個別のテストファイルを実行:
```bash
pytest src/test/<test_file>.py
```

## Dependencies

- streamlit (Webアプリケーションフレームワーク)
- Databricks CLI (自動インストール済み)

注: requirements.txtにpandas、numpyがコメントアウトされています。必要に応じてアンコメントしてください。

## Git操作の重要な注意事項

**必ずファイル変更前にgitステージングまたはコミットを行うこと**

Claude Codeはファイルを直接編集します。gitにステージしていない状態で変更を行うと、元の状態に戻せなくなる可能性があります。作業前に必ず：
```bash
git status          # 変更状態を確認
git add .           # 必要に応じてステージング
git commit -m "..."  # コミット
```

## Documentation

- `docs/ClaudeCodeガイド.md` - Claude Codeの詳細な使用方法、プロンプト例、ベストプラクティスが記載されています
