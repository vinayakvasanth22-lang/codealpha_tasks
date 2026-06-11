import csv
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 175,
    "MSFT": 420,
    "AMZN": 195,
    "NFLX": 650,
    "META": 530,
    "NVDA": 130,
}
def display_available_stocks():
    print("\n📈 Available Stocks:")
    print(f"{'Symbol':<10} {'Price (USD)':>12}")
    print("-" * 24)
    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol:<10} ${price:>11,.2f}")
def get_portfolio():
    portfolio = {}
    print("\nEnter your stock holdings (type 'done' when finished):")
    while True:
        symbol = input("\n  Stock symbol: ").strip().upper()
        if symbol.lower() == "done":
            break
        if symbol not in STOCK_PRICES:
            print(f"  ⚠️  '{symbol}' not found. Available: {', '.join(STOCK_PRICES.keys())}")
            continue
        try:
            quantity = int(input(f"  Quantity of {symbol}: ").strip())
            if quantity <= 0:
                print("  ⚠️  Quantity must be a positive number.")
                continue
            portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        except ValueError:
            print("  ⚠️  Please enter a valid whole number for quantity.")  
    return portfolio
def calculate_investment(portfolio):
    results = []
    total = 0
    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        total += value
        results.append((symbol, quantity, price, value))
    return results, total
def display_results(results, total):
    print("\n" + "=" * 50)
    print("        📊 PORTFOLIO SUMMARY")
    print("=" * 50)
    print(f"{'Stock':<8} {'Qty':>6} {'Price':>10} {'Value':>12}")
    print("-" * 50)
    for symbol, qty, price, value in results:
        print(f"{symbol:<8} {qty:>6} ${price:>9,.2f} ${value:>11,.2f}")
    print("-" * 50)
    print(f"{'TOTAL INVESTMENT':>36} ${total:>11,.2f}")
    print("=" * 50)
def save_results(results, total):
    print("\nSave results?")
    print("  1. Save as .txt")
    print("  2. Save as .csv")
    print("  3. Skip")
    choice = input("Choose (1/2/3): ").strip()
    if choice == "1":
        filename = "portfolio_summary.txt"
        with open(filename, "w") as f:
            f.write("STOCK PORTFOLIO SUMMARY\n")
            f.write("=" * 40 + "\n")
            f.write(f"{'Stock':<8} {'Qty':>6} {'Price':>10} {'Value':>12}\n")
            f.write("-" * 40 + "\n")
            for symbol, qty, price, value in results:
                f.write(f"{symbol:<8} {qty:>6} ${price:>9,.2f} ${value:>11,.2f}\n")
            f.write("-" * 40 + "\n")
            f.write(f"{'TOTAL':>26} ${total:>11,.2f}\n")
        print(f"  ✅ Saved to {filename}")
    elif choice == "2":
        filename = "portfolio_summary.csv"
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price (USD)", "Value (USD)"])
            for symbol, qty, price, value in results:
                writer.writerow([symbol, qty, price, value])
            writer.writerow(["TOTAL", "", "", total])
        print(f"  ✅ Saved to {filename}")
    else:
        print("  Skipped saving.")
def main():
    print("=" * 50)
    print("    💼 STOCK PORTFOLIO TRACKER")
    print("=" * 50)
    display_available_stocks()
    portfolio = get_portfolio()
    if not portfolio:
        print("\n⚠️  No stocks entered. Exiting.")
        return
    results, total = calculate_investment(portfolio)
    display_results(results, total)
    save_results(results, total)
    print("\nThank you for using Stock Portfolio Tracker! 👋\n")
if __name__ == "__main__":
    main()