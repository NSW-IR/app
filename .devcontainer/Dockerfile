# ベースイメージとして Python 3.11 を使用
FROM python:3.11-slim

# OS パッケージの更新と基本ツールのインストール
RUN apt-get update && apt-get install -y \
    git curl vim build-essential && \
    rm -rf /var/lib/apt/lists/*

# 作業ディレクトリを設定
WORKDIR /workspace

# Python ライブラリをインストール（requirements.txt がある場合）
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt || true

# デフォルトのシェルをbashに設定
CMD ["bash"]

# Node.js と npm をインストール
RUN apt-get update && apt-get install -y \
    git curl vim build-essential nodejs npm && \
    rm -rf /var/lib/apt/lists/*