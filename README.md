# Django+Docker+MySQL

## Setup

#### Create local_settings.py

```
touch app/source/config/local_settings.py
```

#### Generate Secret Key & Export to local_settings.py

```
python app/source/config/get_random_secret_key.py > app/source/config/local_settings.py
```

## Run

```
docker compose up -d
```
