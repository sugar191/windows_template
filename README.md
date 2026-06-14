# Windows GUI App Template

CustomTkinter + PyInstaller による個人用Windows GUIアプリのテンプレートリポジトリです。

## 新しいプロジェクトを作る手順

### 1. リポジトリを作成

GitHubの本リポジトリページで **「Use this template」→「Create a new repository」** を選択し、新しいリポジトリを作成します。

### 2. clone

```bash
git clone https://github.com/<your-username>/<new-repo-name>
cd <new-repo-name>
```

### 3. 仮想環境を作成して依存パッケージをインストール

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 4. VSCodeのインタープリターパスを設定

`.vscode/settings.json` の `python.defaultInterpreterPath` を新しい仮想環境のパスに変更します。

```json
{
    "python.defaultInterpreterPath": "C:\\path\\to\\your\\.venv\\Scripts\\python.exe"
}
```

または VSCode のコマンドパレット（`Ctrl+Shift+P`）→「Python: Select Interpreter」で設定します。

### 5. 開発・実行

- **デバッグ実行**: `F5`
- **EXEビルド**: `Ctrl+Shift+B`（出力は `dist/<プロジェクト名>.exe`）

### アイコンを設定する場合

1. `assets/icon.ico` を用意する
2. `.vscode/tasks.json` のアイコン関連コメント4行を外す
3. `main.py` のアイコン関連コメント3行を外す

これにより、exeファイルのアイコンとウィンドウのアイコンが両方反映されます。
