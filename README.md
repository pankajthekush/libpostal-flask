# flask_boilerplate
A very basic and simple flask template , with sqlalchemy and login module. Nothing fancy

# to develop locally 

```bash
docker run -it -p 5000:5000 -v $PWD:/libpostal-flask pkumdev/libpostal bash
```

# to build 
```
docker build -t pkumdev/libpostal-flask . --no-cache
```

# to run locally
```bash
docker run -it -p 8000:8000 -v $PWD:/libpostal-flask pkumdev/libpostal-flask gunicorn -w 10 --threads=2 --bind 0.0.0.0:8000 --timeout 600 wsgi:app --preload
```