# fastapi-security

このプロジェクトはFastAPIのセキュリティ機能をサンプル実装しています。
DockerおよびDocker Composeを使用して環境を構築します。

# インプットドキュメント
https://fastapi.tiangolo.com/features/#security-and-authentication

# セキュリティ各機能

## HTTP Basic
ユーザー名とパスワードを使用してアクセスを制限するシンプルな認証方法です。

## OAuth2 (also with JWT tokens)
OAuth2（JWTトークン対応）
OAuth2は、トークンベースの認証を提供する標準プロトコルです。

### トークン発行フロー
ユーザーがフロントエンドでユーザー名とパスワードを入力。
バックエンドの/tokenエンドポイントに送信。
バックエンドがトークン（通常はJWT）を生成し返却。

### JWTトークンの利用
トークンには有効期限などの情報が含まれ、リクエスト時にAuthorization: Bearer <token>として送信されます。

## API keys
APIキー認証
APIキーは、リクエストごとにクライアント識別用のキーを送信することでアクセス制御を行います。


## ChatGPTで生成
FastAPIは、APIのセキュリティ (認証や認可)を比較的簡単に実装できるよう、多彩なツールと仕組みを提供しています。以下に、FastAPIで利用可能な主なセキュリティ機能をリストアップします。

### 1. OAuth2を用いた認証

#### OAuth2PasswordBearer
クライアントから送られるAuthorizationヘッダーの「Bearer」 トークンを自動的に抽出し、依存性として利用可能にします。これにより、認証済みリクエストの処理を簡単に行えます。

#### OAuth2PasswordRequestForm
ユーザー名とパスワードを含むログインフォームのデータを受け取るための依存性で、トークン発行用エンドポイントなどで活用されます。

#### JWTトークンとの連携
OAuth2のフローを利用しながら、JWT (JSON Web Token) を使って認証情報を安全に管理するパターンがよく用いられます。

### 2. HTTPベースの認証

#### HTTP Basic認証 (HTTPBasic)
シンプルなユーザー名とパスワードによる認証を実現するため、「fastapi.security.HTTPBasic を使ってHTTP Basic認証を実装できます。

#### HTTP Bearer認証 (HTTPBearer)
Bearer トークン方式の認証を簡単に扱うためのクラスで、Authorizationヘッダーからトークンを抽出して検証することが可能です。

### 3. APIキー認証
FastAPIはAPIキーによる認証を複数の方法でサポートしており、以下のクラスが用意されています。

#### APIKeyHeader
リクエストヘッダーからAPIキーを抽出して認証に利用します。

#### APIKeyQuery
クエリパラメータからAPIキーを受け取ります。

#### APIKeyCookie
Cookieに含まれるAPIキーを利用して認証処理を行います。

### 4. OpenAPIセキュリティスキームの統合
FastAPIは、上記の各種セキュリティ方法をOpenAPI仕様に統合し、対話型ドキュメント (Swagger Ul やReDoc) 上で「Authorize」 ボタンを自動生成します。これにより、開発時に各エンドポイントのセキュリティ設定が視覚的に確認でき、クライアント側も簡単に認証情報を入力できるようになります。

### 5. 依存性注入によるセキュリティ機能の利用
FastAPIの依存性注入システムを利用することで、セキュリティに関する共通のロジック(たとえば、 現在のユーザー情報の取得や認証状態の確認)を一元管理し、各パスオペレーションに容易に組み込むことができます。これにより、コードの重複を避け、セキュアな設計を効率的に実装できます。

### 6. Starletteのセキュリティ機能の活用
FastAPIはStarletteをベースとしているため、Starletteが提供するセッション Cookieの管理などの追加のセキュリティ機能も利用できます。これにより、必要に応じたより高度な認証・認可の仕組みを構築可能です。



## ディレクトリ構成
|--.gitignore
|--Dockerfile
|--README.md
|--docker-compose.yml
|--main.py
|--requirements.txt
|--routers
|  |--httpbasic.py


## セットアップ

### 必要なツール

- Docker
- Docker Compose

### 手順

1. リポジトリをクローンします。

    ```sh
    git clone <リポジトリURL>
    cd fastapi-security
    ```

2. Dockerイメージをビルドし、コンテナを起動します。

    ```sh
    docker compose up --build
    ```

3. ブラウザで `http://localhost:8000` にアクセスします。

## APIエンドポイント


### 認証なしエンドポイント
curl -X GET http://127.0.0.1:8000

### HTTPBasic
curl -X 'POST' \
  'http://localhost:8000/httpbasic' \
  -H 'accept: application/json' \
  -H 'Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=' \
  -d ''

### APIKeyHeader
curl -X 'GET' \
  'http://localhost:8000/apikeyheader' \
  -H "x-key: your_api_key_here"

### HTTP Credentials
curl -X 'GET' \
  'http://localhost:8000/http_auth_credentials' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer secret-token'