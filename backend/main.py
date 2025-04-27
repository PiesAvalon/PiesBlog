from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()  # 创建 FastAPI 实例

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # 前端开发服务器地址
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")  # 定义 GET 路由
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")  # 路径参数
async def read_item(item_id: int):
    return {"item_id": item_id}

"""
运行：
uvicorn main:app --reload
"""