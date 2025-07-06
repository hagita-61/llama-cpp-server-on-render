from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from llama_cpp import Llama

app = FastAPI()

# モデルファイルは Render のディスクに置く必要がある
llm = Llama(
    model_path="./model.gguf",  # ggufモデルをルートにアップして使う想定
    n_ctx=4096,
    n_threads=4
)

class Request(BaseModel):
    prompt: str
    n_predict: int = 128

@app.post("/completion")
async def completion(req: Request):
    try:
        result = llm(req.prompt, max_tokens=req.n_predict)
        text = result["choices"][0]["text"]
        return {"content": text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "llama.cpp server is running"}
