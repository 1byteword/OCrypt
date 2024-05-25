import fastapi
from fastapi import Request
from fastapi.responses import JSONResponse

import uvicorn

app = fastapi.FastAPI()

tokens = {}

@app.post("/tokenize")
async def tokenize(request: Request):
    i = 1
    data = await request.json()
    for item in data['data']:
        tokens['field' + str(i)] = item
        i += 1

    return JSONResponse(status_code=200, content=tokens)

@app.post("/detokenize")
async def detokenize(request: Request):
    data = await request.json()
    i = 1
    response = []
    for item in data['data']:
        key = 'field' + str(i)
        if key in tokens:
            response.append(tokens[key])
        else:
            response.append(item + " (not found)")
        i += 1

    return JSONResponse(status_code=200, content=response)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)