def usd_inr(a, b):
    inr = a * b
    return inr
user_input = int(input("Enter the amount in USD: "))
exchange_rate = float(input("Enter the exchange rate (USD to INR): "))
result = usd_inr(user_input, exchange_rate)
print(f"{user_input} USD is equal to {result} INR.")
    