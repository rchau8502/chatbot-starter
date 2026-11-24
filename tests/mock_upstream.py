"""本地假的模型上游：没有真 key 时验证 SSE 流式、压缩、停止。

启动：
    .venv/bin/uvicorn --app-dir tests mock_upstream:app --port 8011
"""
import asyncio
import json

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, StreamingResponse

app = FastAPI()

REPLY = (
    "外卖 3 公里内都能送：\n"
    "1. 满 30 元免配送费，不满收 5 元。\n"
    "2. 高峰期（11:30–13:00）大约 30–40 分钟，平时 20 分钟左右。\n"
    "3. 下雨天会再慢 10 分钟，急的话可以先打电话给门店。\n\n"
    "记得备注楼层和门牌号，骑手到了不好找会耽误时间。"
)

SUMMARY = "备忘：顾客在问外卖；已告知 3 公里内配送、满 30 元免配送费、高峰 30–40 分钟。"


@app.post("/chat/completions")
async def completions(req: Request):
    body = await req.json()
    if "messages" not in body:
        return JSONResponse({"error": "bad request"}, status_code=400)
    if not body.get("stream"):
        return {"choices": [{"message": {"role": "assistant", "content": SUMMARY}}]}

    async def gen():
        for i in range(0, len(REPLY), 6):
            chunk = REPLY[i : i + 6]
            data = {"choices": [{"delta": {"content": chunk}}]}
            yield "data: " + json.dumps(data, ensure_ascii=False) + "\n\n"
            await asyncio.sleep(0.1)
        yield "data: [DONE]\n\n"

    return StreamingResponse(gen(), media_type="text/event-stream")
