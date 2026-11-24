import yfinance as yf

shares = {"VOO": 0, "VXUS": 0, "IJR": 0, "QQQ": 0}

prices = yf.download(list(shares), period="2y", auto_adjust=True, threads=False)["Close"]
prices = prices.dropna(axis=1, how="all")
latest = prices.iloc[-1]

print("Latest prices:")
print(latest.round(2))

values = {t: shares[t] * latest[t] for t in shares if t in latest.index}
total = sum(values.values())
if total > 0:
    print(f"\nTotal in these funds: ${total:,.2f}")
    for t, v in values.items():
        print(f"{t}: ${v:,.2f} ({v / total:.1%})")

returns = prices.pct_change().dropna()
print("\nAnnualized volatility:")
print((returns.std() * 252 ** 0.5).round(3))
print("\nCorrelation:")
print(returns.corr().round(2))
