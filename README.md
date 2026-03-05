# 2026年現在モダンでベストプラクティスなCloud IDE(Codespace)開発環境
このプロジェクトは、フロントエンドとバックエンドを別々のリポジトリで管理し、この親リポジトリで Git Submodule として統合しています。


## 0. サブモジュールの追加(1回のみ)
1. ルートディレクトリ（.devcontainer がある場所）で以下を打つ
    ```
    mkdir frontend backend
    git submodule add https://github.com/ユーザー名/frontend.git frontend
    git submodule add https://github.com/ユーザー名/backend.git backend
    ```
2. `.gitmodules`が生成される
3. 親リポジトリの変更としてコミット&Push

## 1. 開発環境の起動
Codespaces が起動したら、まず初回のみサブモジュールの内容を同期する必要があります。
次にアプリケーション全体のコンテナを立ち上げます。
```
# サブモジュールの初期化と更新
git submodule update --init --recursive

# コンテナの起動
docker compose up -d 
```


これで、以下のポートが自動的に転送（Forward）され、プレビュー可能になります：
* **Frontend**: http://localhost:3000
* **Backend**: http://localhost:8000
* **Postgres**: localhost:5432


## 2. ソースコードの編集と反映
Codespaces 上でファイルを編集すると、docker-compose.yml の volumes 設定により、コンテナ内のコードも即座に更新されます。
* ホットリロード: Next.js や FastAPI 等を使用している場合、ファイルを保存（Ctrl+S）するだけで、ブラウザ上の表示や API の挙動が自動で更新されます。
* 注意: ライブラリの追加（npm install や pip install）をコンテナ内で行った場合は、必要に応じて docker compose restart を実行してください。

## 3. Git による変更の保存と Push
このリポジトリはサブモジュール構成です。「各ディレクトリ(子)」でコミットした後、「ルート(親)」でその更新を記録するという2段階の手順になります。

### ① フロントエンド/バックエンドの変更を Push する
それぞれのディレクトリに移動して作業します。

```
# 例：フロントエンドを修正する場合
cd frontend

# ここは通常通りの操作
git checkout -b feat/hogehoge
git add .
git commit -m "feat: 画面レイアウトの修正"
git push origin feat/hogehoge
```

### ② 親リポジトリに「更新したこと」を記録する
子リポジトリを Push しただけでは、この親リポジトリが指し示すバージョンは古いままです。親リポジトリ側でも「新しいバージョンを指すように」更新を記録します。

```
# ルートディレクトリに戻る
cd ..

# git status を打つと、frontend が「modified (new commits)」と表示されます
git status

# 親リポジトリとして更新をコミット
git add frontend
git commit -m "update: frontend submodule to latest feat/hogehoge"
git push origin main
```

### ※他の開発者が更新を取り込む場合
他の人がサブモジュールの指す位置を更新した場合は、以下のコマンドで手元のコードを同期します。

```
git pull
git submodule update --init --recursive
```

## 4. よく使うコマンド集
|操作|コマンド|
|---:|:---|
|コンテナのログ確認|`docker compose logs -f`|
|特定のコンテナに入る|`docker compose exec backend bash`|
|環境を完全に初期化|`docker compose down -v && docker compose up -d`|

# ディレクトリ構成
```
.
├── .devcontainer/
│   ├── devcontainer.json  <-- 開発環境の設定
│   └── Dockerfile         <-- 開発環境の細かな設定、パッケージインストールやOS設定
├── docker-compose.yml     <-- アプリ（DB, Front, Back）の定義、アプリケーションの構成図
├── frontend/              <-- フロントエンドのソースコード
├── backend/               <-- バックエンドのソースコード
└── (その他リポジトリのファイル)
```
