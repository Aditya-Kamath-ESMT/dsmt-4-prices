"""Plot stock performance since 2024 as percentage change from the first close."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt

from prices import TICKERS, load_prices

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "figures" / "stock_prices_since_2024.png"
START_DATE = "2024-01-01"


def main() -> None:
    fig, ax = plt.subplots(figsize=(12, 6), constrained_layout=True)

    for ticker in TICKERS:
        prices = load_prices(ticker)
        closes = prices.loc[prices.index >= START_DATE, "Close"]
        performance = (closes / closes.iloc[0] - 1) * 100
        ax.plot(performance.index, performance, label=ticker, linewidth=1.6)

    ax.axhline(0, color="black", linewidth=0.8, alpha=0.6)
    ax.set_title("Stock price performance since 2024")
    ax.set_xlabel("Date")
    ax.set_ylabel("Change from first 2024 close (%)")
    ax.grid(True, alpha=0.25)
    ax.legend(title="Ticker")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT, dpi=160, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {OUTPUT}")


if __name__ == "__main__":
    main()
