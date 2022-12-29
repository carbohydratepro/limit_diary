# README

# 0. バージョン
- ruby -> 3.1.2
- rails -> 7.0.4
- docker compose -> 3.9

# 1. 環境構築
### 1-1. Gitリポジトリをクローン
```text
git clone https://github.com/carbohydratepro/limit_diary.git
cd limit_diary
```

### 1-2. dockerイメージをbuild
```text
docker-compose build
```

### 1-3. Dockerを起動
```text
docker-compose up -d
```

### 1-4. コマンドを実行
```text
docker-compose exec web rake db:create

docker-compose exec web bundle install

docker-compose exec web bundle exec rake app:update:bin
```

### 1-5. localhost:3000にアクセス
Railsの画面が表示されていれば成功




