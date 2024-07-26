import frappe
from erpnext.accounts.doctype.sales_invoice.sales_invoice import SalesInvoice
from pycoingecko import CoinGeckoAPI



class SalesInvoiceCustom(SalesInvoice):
    # pass

    def get_crypto_prices(self):
        cg = CoinGeckoAPI()
        prices = frappe._dict(cg.get_price(ids=['bitcoin', 'ethereum'], vs_currencies=self.currency))

        print("GETTING PRICES")

        return {
            'bitcoin' : float(self.grand_total/prices.bitcoin[self.currency.lower()]),
            'ethereum' : float(self.grand_total/prices.ethereum[self.currency.lower()])
        }