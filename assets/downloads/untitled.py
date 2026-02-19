import pandas as pd
import matplotlib.pyplot as plt

os.chdir("/Users/apxww/Desktop/GitHub/myside/assets/downloads/")

df = pd.read_csv(".data_ofr_varmetric.csv", encoding = "iso-8859-1")

    # --- Plot ---
    plt.figure(figsize=(10, 5))
    plt.plot(yearly["year"], yearly["share_no_metric"], marker="o", label="No risk metric reported")
    plt.plot(yearly["year"], yearly["share_alt_var"], marker="o", label="Alternative to VaR")
    plt.plot(yearly["year"], yearly["share_var"], marker="o", label="VaR")

    plt.xlabel("Year")
    plt.ylabel("Share of total qualifying funds")
    plt.ylim(0, 1)
    plt.title("Shares of Qualifying Hedge Funds by Risk Metric (per year)")
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.legend()
    plt.tight_layout()
    plt.savefig(args.output, dpi=200)
    plt.show()

    # Optional: save the computed yearly shares
    out_csv = args.output.rsplit(".", 1)[0] + "_shares_by_year.csv"
    yearly.to_csv(out_csv, index=False)
    print(f"Saved plot to: {args.output}")
    print(f"Saved yearly shares to: {out_csv}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)
