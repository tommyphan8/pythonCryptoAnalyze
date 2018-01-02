class cryptoCurrency:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.symbol = data['symbol']
        self.rank = data['rank']

        if data['price_usd'] is not None:
            self.price_usd = float(data['price_usd'])
        else:
            self.price_usd = -1

        if data['price_btc'] is not None:
            self.price_btc = float(data['price_btc'])
        else:
            self.price_btc = -1

        if data['24h_volume_usd'] is not None:
            self.volume_24h_usd = float(data['24h_volume_usd'])
        else:
            self.volume_24h_usd = -1

        if data['market_cap_usd'] is not None:
            self.market_cap_usd = float(data['market_cap_usd'])
        else:
            self.market_cap_usd = -1

        if data['available_supply'] is not None:
            self.available_supply = float(data['available_supply'])
        else:
            self.available_supply = -1

        if data['total_supply'] is not None:
            self.total_supply = float(data['total_supply'])
        else:
            self.total_supply = -1

        if data['percent_change_24h'] is not None:
            self.percent_change_24h = float(data['percent_change_24h'])
        else:
            self.percent_change_24h = -1

        if data['percent_change_7d'] is not None:
            self.percent_change_7d = float(data['percent_change_7d'])
        else:
            self.percent_change_7d = -1

        self.last_updated = data['last_updated']

        self.percent_marketCap_volume24h = self.market_cap_usd / self.volume_24h_usd

    def __str__(self):
        return (self.name + "\n" + self.symbol + "\n" + "Rank: " + self.rank + "\n" + "Price: " + str(self.price_usd)
                + "\n" + "Market Cap: " + str(self.market_cap_usd) + "\n" + "Available Supply: " + str(
                    self.available_supply) +
                "\n" + "Total Supply: " + str(self.total_supply) + "\n" + "Percent Changed 24h: " + str(
                    self.percent_change_24h)
                + "\n" + "Percent Changed 7d: " + str(self.percent_change_7d) + "\n" + "Market Cap Volume 24h %: " +
                str(self.percent_marketCap_volume24h) + "\n")
