# ベースイメージとして Python 3.11 を使用
FROM python:3.11-slim

# OS パッケージの更新と基本ツールのインストール
RUN apt-get update && apt-get install -y \
    git curl vim build-essential nodejs npm unzip && \
    rm -rf /var/lib/apt/lists/*

# 作業ディレクトリを設定
WORKDIR /workspace

# Python 仮想環境（venv）の作成
RUN python -m venv /workspace/.venv

# venv を有効化して pip を最新化
RUN . /workspace/.venv/bin/activate && pip install --upgrade pip

# 環境変数でデフォルトPythonパスを venv に切り替え
ENV PATH="/workspace/.venv/bin:$PATH"

# Python ライブラリのインストール
COPY requirements.txt ./ 
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# Databricks CLI のインストール
RUN bash -c "curl -fsSL https://raw.githubusercontent.com/databricks/setup-cli/main/install.sh | bash"

# Databricks Connect のインストール
RUN pip install databricks-connect

# デフォルトシェルをbashに設定
CMD ["/bin/bash"]