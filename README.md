# autify-web-scraper

## Requirements
- Python 3.8

## Spec
```
$ autifycli fetch --help
Usage: autifycli fetch [OPTIONS] URLS...

  Fetch web pages

Options:
  --metadata                   Display metadata of url
  -p, --numof-process INTEGER  Number of processes.
  --help                       Show this message and exit.
```

Multiprocessing supported. It might be okay to support multi-threading but because each processes is independent each others, using multiprocessing more makes sense. But again using multi-threading is also fine if we can handle errors properly.

## Limitation
- I didn't support urls which have slask "/" because I didn't come up with a good strategy to save them within limited time (2hours).
- I didn't support urls which have query parameters because (ditto).
- I didn't support the "Extra credit" because of the limited time.
- I didn't finish unit tests because of the limited time. but covered base cases.

## How to install (dev mode)
```
$ pip install poetry
$ poetry install
```

## Run with Docker
```
$ docker-compose build app
$ docker-compose run app autifycli fetch --metadata -p 2 https://www.google.com https://autify.com
{
  "site": "https://autify.com",
  "last_fetch": "2021-08-13 19:00:41.712655+09:00",
  "num_links": 51,
  "num_images": 105
}
{
  "site": "https://www.google.com",
  "last_fetch": "2021-08-13 19:00:41.712655+09:00",
  "num_links": 18,
  "num_images": 1
}
$ ls
Dockerfile  Makefile   autify.com.html  docker-compose.yaml  poetry.lock  pyproject.toml  www.google.com.html
LICENSE     README.md  autifycli        mypy.ini             poetry.toml  tests
```