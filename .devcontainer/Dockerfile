# ベースイメージとして Python 3.11 を使用
FROM python:3.11-slim

# OS パッケージの更新と基本ツールのインストール
RUN apt-get update && apt-get install -y \
    git curl vim build-essential nodejs npm unzip && \
    rm -rf /var/lib/apt/lists/*

# 作業ディレクトリを設定
WORKDIR /workspace

# Pythonライブラリのインストール（requirements.txt がある場合のみ）
COPY requirements.txt ./
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# Databricks CLI のインストール
RUN bash -c "curl -fsSL https://raw.githubusercontent.com/databricks/setup-cli/main/install.sh | bash"

# デフォルトシェルをbashに設定
CMD ["/bin/bash"]