import requests
from pycoingecko import CoinGeckoAPI
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
url="https://api.coingecko.com/api/v3/simple/price"
cg=CoinGeckoAPI()

ohlc=cg.get_coin_ohlc_by_id(id = "bitcoin", vs_currency = "usd", days = "30")
df=pd.DataFrame(ohlc,columns=["timestamp","open","high","low","close"])
df["timestamp"]=pd.to_datetime(df["timestamp"],unit="ms")
df.to_csv("bitcoin_30days_ohlc.csv",index=False) 
print("Kayıt Başarılı!!")

xpoints=np.array([0,6])
ypoints=np.array([0,250])

plt.plot(xpoints,ypoints)
plt.show()