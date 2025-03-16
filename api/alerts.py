from fastapi import APIRouter, WebSocket
import asyncio
import yfinance as yf

router = APIRouter()


async def fetch_stock_price(symbol: str):
    """Fetch live stock prices from Yahoo Finance"""
    stock = yf.Ticker(symbol)
    return stock.history(period="1d")["Close"].iloc[-1]


@router.websocket("/ws/{symbol}")
async def websocket_endpoint(websocket: WebSocket, symbol: str):
    """WebSocket connection for real-time stock alerts"""
    await websocket.accept()
    try:
        while True:
            price = await fetch_stock_price(symbol)
            await websocket.send_text(f"Latest price of {symbol}: ${price}")
            await asyncio.sleep(10)  # Fetch every 10 seconds
    except Exception as e:
        print(f"WebSocket error: {e}")
        await websocket.close()
