# gPBL_2023_summer
## requirment
http://www.cl.ecei.tohoku.ac.jp/~m-suzuki/jawiki_vector/  
word2vecフォルダを作り、中にentity_vector.model.binを配置

## データベース構築
```sh
python3 manage.py makemigrations
python3 manage.py migrate
```

## デモデータの作成
```sh
python3 manage.py demodata
```

## 実行
```sh
python3 manage.py runserver
```
