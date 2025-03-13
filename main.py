import requests
from pycoingecko import CoinGeckoAPI
import pandas as pd
import numpy as np
import seaborn as sns
import seaborn.objects as so
import plotly.express as px
url="https://api.coingecko.com/api/v3/simple/price"
cg=CoinGeckoAPI()

ohlc=cg.get_coin_ohlc_by_id(id = "bitcoin", vs_currency = "usd", days = "30")
df=pd.DataFrame(ohlc,columns=["timestamp","open","high","low","close"])
df["timestamp"]=pd.to_datetime(df["timestamp"],unit="ms")
df[df["timestamp"] >= (df["timestamp"].max() - pd.Timedelta(days=7))]
df.to_csv("bitcoin_30days_ohlc.csv",index=False) 
print("Kayıt Başarılı!!")

df=pd.read_csv("bitcoin_30days_ohlc.csv",parse_dates=["timestamp"])

fig = px.line(df, x='timestamp', y='close', title='Bitcoin Kapanış Fiyatları (Son 30 Gün)')
fig.update_xaxes(title='Tarih')
fig.update_yaxes(title='Kapanış Fiyatı (USD)')
fig.update_layout(
    update_menus=[
        dict(
            type="buttons",
            direction="left",
            buttons=list([
                dict(
                    args=["type","7days"],
                    label="7 Days",
                    method="restyle"
                ),
                dict(
                    args=["type","30days"],
                    label="30 Days",
                    method="restyle"
                )                      
            ]),
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0.11,
            xanchor="left",
            y=1.1,
            yanchor="top"
        )
    ]
)
fig.show()