# fastapi-security

このプロジェクトは、FastAPIを使用してAPIキー認証を実装したサンプルアプリケーションです。DockerおよびDocker Composeを使用して環境を構築します。

## ディレクトリ構成
|--.gitignore 
|--Dockerfile 
|--docker-compose.yml 
|--main.py 
|--README.md 
|--requirements.txt


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
    docker-compose up --build
    ```

3. ブラウザで `http://localhost:8000` にアクセスします。

## APIエンドポイント

### 認証付きエンドポイント

- `GET /secure-endpoint`

  APIキーを使用して認証されたユーザーのみがアクセスできます。

  ```sh
  curl -H "access_token: your_api_key" http://localhost:8000/secure-endpoint


### 認証なしエンドポイント
curl -X GET http://127.0.0.1:8000

curl -X GET http://127.0.0.1:8000/users/

curl -X GET http://127.0.0.1:8000/users/1

curl -X GET http://127.0.0.1:8000/items/

curl -X POST \
  http://127.0.0.1:8000/items/ \
  -H 'Content-Type: application/json' \
  -d '{ "name": "ChatGPT", "price": 100.0 }'


# simple-oauth2
https://fastapi.tiangolo.com/ja/tutorial/security/simple-oauth2/#scope

## get token
curl -X POST http://localhost:8000/security1/token \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "username=johndoe&password=secret"

## use token
curl -X GET http://localhost:8000/security1/users/me \
-H "Authorization: Bearer johndoe"
