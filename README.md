# fastapi-security

このプロジェクトは、FastAPIを使用してAPIキー認証を実装したサンプルアプリケーションです。DockerおよびDocker Composeを使用して環境を構築します。

# FastAPI Security Tools
https://fastapi.tiangolo.com/ja/reference/security/

## API Key Security Schemes
APIキー認証
fastapi.security.APIKeyHeader
https://fastapi.tiangolo.com/ja/reference/security/#fastapi.security.APIKeyHeader

## HTTP Authentication Schemes
Basic認証
fastapi.security.HTTPBasic
https://fastapi.tiangolo.com/advanced/security/http-basic-auth/

## HTTP Credentials

https://fastapi.tiangolo.com/ja/reference/security/#fastapi.security.HTTPAuthorizationCredentials

## OAuth2 Authentication


## OAuth2 Security Scopes in Dependencies

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