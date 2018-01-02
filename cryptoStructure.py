import cryptoCurrency

class cryptoStructure:

    def __init__(self):
        self.crypto_list = []

    def addCrypto(self, crypto):
        if (isinstance(crypto, cryptoCurrency.cryptoCurrency)):
            self.crypto_list.append(crypto)

    def getSortedSupplyVolume24(self, lowSupply, highSupply):
        sorted_list = []
        for c in self.crypto_list:
            if c.available_supply >= lowSupply and c.available_supply <= highSupply:
                sorted_list.append(c)

        sorted_list.sort(key=lambda c: c.volume_24h_usd, reverse=True)
        return sorted_list






