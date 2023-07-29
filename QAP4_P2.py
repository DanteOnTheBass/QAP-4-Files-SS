import matplotlib.pyplot as plt
import matplotlib.patheffects as patheffects


# main program
def get_sales_amount(month):
    while True:
        SaleAmt = input(f"Enter the total sales for {month}: ")
        if not SaleAmt:
            print("ERROR - Sales amount cannot be blank.")
        elif not SaleAmt.isdigit():
            print("ERROR - Sales amount must consist of numerical digits only. (ex. 1234)")
        else:
            return float(SaleAmt)


def get_monthly_sales():
    sales = []

    for month in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November", "December"]:
        SaleAmt = get_sales_amount(month)
        sales.append(SaleAmt)

    return sales


# graph set up
def plot_sales_graph(months, sales):
    fig, ax = plt.subplots()

    bars = ax.bar(months, sales,
                  color=['skyblue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan',
                         'magenta', 'lightblue'], edgecolor='black', linewidth=1.5, alpha=0.7)

    for bar in bars:
        shadow = patheffects.withSimplePatchShadow((1.5, -1.5), shadow_rgbFace=(0, 0, 0, 0.3))
        bar.set_path_effects([shadow])

    ax.set_title('End of Year OSIC Monthly Sales')
    ax.set_xlabel('Months')
    ax.set_ylabel('Total Sales ($)')

    for bar, sale in zip(bars, sales):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 100, f"${sale:,.2f}", ha='center', va='bottom', fontsize=9,
                fontweight='bold', rotation=90)

    ax.grid(axis='y', linestyle='--', alpha=0.7)

    # Show the plot
    plt.show()


# printed output table
def main():
    print("Enter the total sales for each month:")
    MonthlySales = get_monthly_sales()

    Months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    plot_sales_graph(Months, MonthlySales)

    # Print the neatly formatted information
    print("\nOSIC Monthly Sales:")
    print("---------------------")
    print("Month        |    Sales")
    print("---------------------")
    for month, sale in zip(Months, MonthlySales):
        print(f"{month:12s} |   ${sale:,.2f}")


if __name__ == "__main__":
    main()
