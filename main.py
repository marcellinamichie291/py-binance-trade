import time
import numpy as np
from threading import Timer
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
from config.main import API_KEY, SECRET_KEY

client = Client(API_KEY, SECRET_KEY)

depth = client.get_order_book(symbol='BNBBTC')

print(depth)