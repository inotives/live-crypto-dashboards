import requests
import time

class paxos_api():

    def get_data(self, url):
        resp = requests.get(url)
        return resp.json()

    def get_messari_asset_metrics(self, token):
        return self.get_data(f"https://data.messari.io/api/v1/assets/{token}/metrics")

    def get_orderbook(self, market):
        return self.get_data(f"https://api.paxos.com/v2/markets/{market}/order-book")

    def get_ticker(self, market):
        return self.get_data(f"https://api.paxos.com/v2/markets/{market}/ticker")

    def get_paxos_data_single_market(self, market):
            # get data from PAXOS API V2 -------------------
            ticker_raw = self.get_ticker(market)
            orderbook_raw = self.get_orderbook(market)
            
            ticker = self.process_ticker_data(ticker_raw)
            odbk = self.process_orderbook_data(orderbook_raw)

            return {
                'market': market, 
                'asset': market.split('USD')[0],
                'vol_today': ticker['vol_today'],
                'vol_today_usd': ticker['vol_today_usd'],
                'mid_price': odbk['mid_price'],
                'spread': odbk['spread'],
                'top_asks': odbk['top_asks'],
                'top_bids': odbk['top_bids'],
                'ask_cnt': odbk['ask_cnt'],
                'bid_cnt': odbk['bid_cnt'],
                'ask_total_liq': odbk['ask_total_liq'],
                'bid_total_liq': odbk['bid_total_liq'],

                'bid_liq_25bps': odbk['bid_liq_25bps'],
                'ask_liq_25bps': odbk['ask_liq_25bps'],
                'ask_cnt_25bps': odbk['ask_cnt_25bps'],
                'bid_cnt_25bps': odbk['bid_cnt_25bps'],

                'bid_liq_50bps': odbk['bid_liq_50bps'],
                'ask_liq_50bps': odbk['ask_liq_50bps'],
                'ask_cnt_50bps': odbk['ask_cnt_50bps'],
                'bid_cnt_50bps': odbk['bid_cnt_50bps'],

                'bid_liq_100bps': odbk['bid_liq_100bps'],
                'ask_liq_100bps': odbk['ask_liq_100bps'],
                'ask_cnt_100bps': odbk['ask_cnt_100bps'],
                'bid_cnt_100bps': odbk['bid_cnt_100bps'],

                'bid_liq_200bps': odbk['bid_liq_200bps'],
                'ask_liq_200bps': odbk['ask_liq_200bps'],
                'ask_cnt_200bps': odbk['ask_cnt_200bps'],
                'bid_cnt_200bps': odbk['bid_cnt_200bps'],

                'orderbook_full': odbk['orderbook_full']
            }

    def get_paxos_data_all(self):
        final_output = {}
        all_markets = ['BTCUSD', 'ETHUSD', 'PAXGUSD', 'BCHUSD', 'LTCUSD','UNIUSD', 'SOLUSD', 'LINKUSD', 'AAVEUSD', 'MATICUSD']

        for market in all_markets:

            data = self.get_paxos_data_single_market(market)

            spread_bps = (data['spread']/data['mid_price'])*10000

            final_output[market] = [
                market, 
                data['vol_today'],
                data['vol_today_usd'],
                data['mid_price'],
                data['spread'],
                spread_bps,
                data['top_asks'],
                data['top_bids'],
                data['ask_cnt'],
                data['bid_cnt'],
                data['ask_total_liq'],
                data['bid_total_liq'],
                data['bid_liq_25bps'],
                data['ask_liq_25bps'],
                data['bid_liq_50bps'],
                data['ask_liq_50bps'],
                data['bid_liq_100bps'],
                data['ask_liq_100bps'],
                data['bid_liq_200bps'],
                data['ask_liq_200bps']
            ]

            time.sleep(0.5) # stop 1 sec per 2 call to make sure we dont over the limit of 10 req/sec

        return final_output




    def process_ticker_data(self, ticker):

        best_bid = float(ticker['best_bid']['price'])
        best_ask = float(ticker['best_ask']['price'])
        midprice = ( best_ask + best_bid ) / 2
        today_vol = float(ticker['today']['volume'])
        today_vol_usd = today_vol * midprice
        lastd_vol = float(ticker['last_day']['volume'])

        return {
            'vol_today': today_vol,
            'vol_lastday': lastd_vol,
            'vol_today_usd': today_vol_usd
        }


    def process_orderbook_data(self, orderbook):
        
        top_bids=float(orderbook['bids'][0]['price'])
        top_asks=float(orderbook['asks'][0]['price'])
        mid_price=(top_bids+top_asks)/2
        spread=top_asks - top_bids
        bids_cnt = len(orderbook['bids'])
        asks_cnt = len(orderbook['asks'])
        bids_total_liq = 0
        asks_total_liq = 0
        orderbook_full = {}

        # liquidities at 25bps
        bid_price_25bps = mid_price - (0.0025 * mid_price) # meaning the price 25bps away from mid price. e.q. midprice=20000, bid price 25bps away = $20000 - (0.0025*20000) = $19950
        ask_price_25bps = mid_price + (0.0025 * mid_price) # meaning the price 25bps away from mid price. e.q. midprice=20000, bid price 25bps away = $20000 + (0.0025*20000) = $20050
        total_bids_size_at_25bps = 0
        total_asks_size_at_25bps = 0
        bid_cnt_25bps = 0
        ask_cnt_25bps = 0

        # liquidities at 50bps
        bid_price_50bps = mid_price - (0.005 * mid_price) # meaning the price 50bps away from mid price. e.q. midprice=20000, bid price 50bps away = $20000 - (0.005*20000) = $19900
        ask_price_50bps = mid_price + (0.005 * mid_price) # meaning the price 50bps away from mid price. e.q. midprice=20000, bid price 50bps away = $20000 + (0.005*20000) = $20100
        total_bids_size_at_50bps = 0
        total_asks_size_at_50bps = 0
        bid_cnt_50bps = 0
        ask_cnt_50bps = 0

        # liquidities at 100bps
        bid_price_100bps = mid_price - (0.01 * mid_price) # meaning the price 100bps away from mid price. e.q. midprice=20000, bid price 100bps away = $20000 - (0.01*20000) = $19800
        ask_price_100bps = mid_price + (0.01 * mid_price) # meaning the price 100bps away from mid price. e.q. midprice=20000, bid price 100bps away = $20000 + (0.01*20000) = $20200
        total_bids_size_at_100bps = 0
        total_asks_size_at_100bps = 0
        bid_cnt_100bps = 0
        ask_cnt_100bps = 0

        # liquidities at 200bps
        bid_price_200bps = mid_price - (0.02 * mid_price) # meaning the price 200bps away from mid price. e.q. midprice=20000, bid price 200bps away = $20000 - (0.02*20000) = $19600
        ask_price_200bps = mid_price + (0.02 * mid_price) # meaning the price 200bps away from mid price. e.q. midprice=20000, bid price 200bps away = $20000 + (0.02*20000) = $20600
        total_bids_size_at_200bps = 0
        total_asks_size_at_200bps = 0    
        bid_cnt_200bps = 0
        ask_cnt_200bps = 0

        
        bid_accum_amt = 0
        bid_order_cnt = 0
        for bid in orderbook['bids']: 
            bid_order_cnt += 1
            bid_price = float(bid['price'])
            bid_amount = float(bid['amount'])
            bids_total_liq += bid_price*bid_amount
            bid_accum_amt += bid_amount

            if bid_price >= 0.5*mid_price:
                # Making accumulative chart
                if bid_price in orderbook_full: 
                    orderbook_full[bid_price]['qty'] += bid_amount
                else:
                    orderbook_full[bid_price] = {'price': bid_price, 'qty': bid_amount, 'side': 'bid'}

            if bid_price >= bid_price_25bps:
                total_bids_size_at_25bps += bid_amount
                bid_cnt_25bps = bid_order_cnt
            if bid_price >= bid_price_50bps:
                total_bids_size_at_50bps += bid_amount
                bid_cnt_50bps = bid_order_cnt
            if bid_price >= bid_price_100bps:
                total_bids_size_at_100bps += bid_amount
                bid_cnt_100bps = bid_order_cnt
            if bid_price >= bid_price_200bps:
                total_bids_size_at_200bps += bid_amount    
                bid_cnt_200bps = bid_order_cnt
            
        ask_accum_amt = 0
        ask_order_cnt = 0
        for ask in orderbook['asks']:
            ask_order_cnt += 1
            ask_price = float(ask['price'])
            ask_amount = float(ask['amount'])
            asks_total_liq += ask_price*ask_amount
            ask_accum_amt += ask_amount

            if ask_price <= 1.5*mid_price:
                if ask_price in orderbook_full:
                    orderbook_full[ask_price]['qty'] += ask_amount
                else: 
                    orderbook_full[ask_price] = {'price': ask_price, 'qty': ask_amount, 'side': 'ask'}

            # sum from top ask price till it hit the price at 25bps, 50bps, 100bps, 200bps
            if ask_price <= ask_price_25bps: 
                total_asks_size_at_25bps += ask_amount
                ask_cnt_25bps = ask_order_cnt

            if ask_price <= ask_price_50bps: 
                total_asks_size_at_50bps += ask_amount
                ask_cnt_50bps = ask_order_cnt

            if ask_price <= ask_price_100bps: 
                total_asks_size_at_100bps += ask_amount
                ask_cnt_100bps = ask_order_cnt

            if ask_price <= ask_price_200bps: 
                total_asks_size_at_200bps += ask_amount    
                ask_cnt_200bps = ask_order_cnt

        return {
            'market': orderbook['market'],
            'asset': orderbook['market'].split('USD')[0],
            'mid_price': mid_price,
            'spread': spread,
            'top_asks': top_asks,
            'top_bids': top_bids,
            'ask_cnt': asks_cnt,
            'bid_cnt': bids_cnt,
            'ask_total_liq': asks_total_liq,
            'bid_total_liq': bids_total_liq,

            'bid_liq_25bps': total_bids_size_at_25bps*mid_price,
            'ask_liq_25bps': total_asks_size_at_25bps*mid_price,
            'ask_cnt_25bps': ask_cnt_25bps,
            'bid_cnt_25bps': bid_cnt_25bps,

            'bid_liq_50bps': total_bids_size_at_50bps*mid_price,
            'ask_liq_50bps': total_asks_size_at_50bps*mid_price,
            'ask_cnt_50bps': ask_cnt_50bps,
            'bid_cnt_50bps': bid_cnt_50bps,
            
            'bid_liq_100bps': total_bids_size_at_100bps*mid_price,
            'ask_liq_100bps': total_asks_size_at_100bps*mid_price,
            'ask_cnt_100bps': ask_cnt_100bps,
            'bid_cnt_100bps': bid_cnt_100bps,
            
            'bid_liq_200bps': total_bids_size_at_200bps*mid_price,
            'ask_liq_200bps': total_asks_size_at_200bps*mid_price,
            'ask_cnt_200bps': ask_cnt_200bps,
            'bid_cnt_200bps': bid_cnt_200bps,

            'orderbook_full': orderbook_full
        }
