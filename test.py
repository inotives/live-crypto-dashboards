from utils.api import paxos_api
import pandas as pd

print('FARK')

px = paxos_api()

data1 = px.get_paxos_data_single_market('ETHUSD')

df1 = pd.DataFrame.from_dict(data1['orderbook_full'],orient='index', columns=['price','qty','side'])
df2 = pd.DataFrame(list(data1.items()), columns=['key', 'value'])
