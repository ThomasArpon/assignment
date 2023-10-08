mobile_data = {
    'status': True,
    'data': [
          {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
          {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
          {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
          {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
          {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
          {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
            ],
    'exchange_rate': 107.25
            }

i = 0
while i <len(mobile_data ["data"]):
    product_info = (mobile_data['data'][i])
    product_name = product_info ["name"]
    product_origin = product_info ["made"]
    usd_price = float(product_info ["price"] .split()[0])
    dollar_rate = mobile_data['exchange_rate']
    bdt_price = (usd_price * dollar_rate)
    print(f"{product_name} is made in {product_origin}. The price is {usd_price} USD which is almost equal to {bdt_price} BDT.")
    i += 1
