from fastapi import FastAPI

app = FastAPI(title="CI Practice API")


@app.get("/")
def root():
    return {"message": "hello from the CI practice app"}


@app.get("/health")
def health():
    return {"status": "ok"}
