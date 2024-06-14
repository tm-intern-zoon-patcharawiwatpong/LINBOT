from fastapi import FastAPI, Request, Response
from linebot import LineBotApi
from linebot.webhook import WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from dotenv import load_dotenv
import os

app = FastAPI()

load_dotenv()

CHANNEL_ACCESS_TOKEN = os.getenv('CHANNEL_ACCESS_TOKEN')
CHANNEL_SECRET = os.getenv('CHANNEL_SECRET')

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)


@app.get("/hello")
def read_root():
    return "Hello!"


@app.post('/message')
async def handle_message_request(request: Request):
    signature = request.headers['X-Line-Signature']
    body = await request.body()

    try:
        handler.handle(body.decode('UTF-8'), signature)
    except InvalidSignatureError:
        return Response(content="Invalid signature. Please check your channel access token/channel secret.", status_code=400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
