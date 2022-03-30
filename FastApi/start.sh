uvicorn main:app --reload --port 8080
#lsof -nP -iTCP:8080 | grep LISTEN