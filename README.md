# Auto-Email-Generation
Auto Email Generation

# Run locally
- FastAPI server for backend
    ```bash
    uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
    ```

- Fronted server
    ```bash
    npm start
    ```
Other terminal npm start to start the react server

# Local Testing of lambda function
```bash
python-lambda-local -f handler main.py test-events-lambda/events.json
```