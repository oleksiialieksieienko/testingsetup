# testingsetup

Minimal Python app that publishes a static web page.

## Run

```bash
python3 app.py
```

Open `http://localhost:8000`.

The page shows:

`this is python web app`

## Docker

Build the image:

```bash
docker build -t testingsetup .
```

Run the container:

```bash
docker run --rm -p 8000:8000 testingsetup
```
