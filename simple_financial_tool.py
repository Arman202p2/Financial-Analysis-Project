# SIMPLE FINANCIAL ANALYSIS TOOL
# Created by: Arman (BCA Student)
# Purpose: Learn basic financial calculations

def analyze_company(name, revenue, profit, assets, debt):
    """Simple function to analyze a company"""
    print(f"\n--- {name} Analysis ---")
    print(f"Revenue: ₹{revenue:,} crores")
    print(f"Profit: ₹{profit:,} crores")
    
    # Calculate basic ratios
    profit_margin = (profit / revenue) * 100
    debt_ratio = (debt / assets) * 100
    
    print(f"Profit Margin: {profit_margin:.1f}%")
    print(f"Debt Ratio: {debt_ratio:.1f}%")
    
    # Simple recommendations
    if profit_margin > 15:
        print("✓ Good profitability")
    else:
        print("⚠ Average profitability")
    
    return profit_margin, debt_ratio

def analyze_budget(income, expenses_dict):
    """Simple function to analyze personal budget"""
    total_expenses = sum(expenses_dict.values())
    savings = income - total_expenses
    savings_rate = (savings / income) * 100
    
    print(f"\n--- Budget Analysis ---")
    print(f"Income: ₹{income:,}")
    print(f"Expenses: ₹{total_expenses:,}")
    print(f"Savings: ₹{savings:,}")
    print(f"Savings Rate: {savings_rate:.1f}%")
    
    return savings_rate

def pause_or_exit():
    while True:
        choice = input("\nEnter 'M' to return to main menu or 'E' to exit: ").strip().upper()
        if choice == 'M':
            return True  # Return to menu
        elif choice == 'E':
            print("Exiting the tool. Goodbye!")
            return False  # Exit program
        else:
            print("Invalid input. Please enter 'M' or 'E'.")

def menu():
    while True:
        print("\nWelcome to the Simple Financial Analysis Tool!")
        print("Please select an option:")
        print("1. Analyze Companies")
        print("2. Analyze Personal Budget")
        choice = input("Enter your choice (1-2): ")
        
        if choice == '1':
            analyze_company("TCS", 164177, 26688, 132788, 12000)
            analyze_company("Infosys", 136592, 25568, 124936, 8500)
            analyze_company("Wipro", 86854, 8834, 81395, 15000)
            if not pause_or_exit():
                break
        elif choice == '2':
            my_expenses = {
                'Food': 4000,
                'Transport': 2000,
                'Study': 1500,
                'Entertainment': 2500,
                'Others': 3000
            }
            analyze_budget(15000, my_expenses)
            if not pause_or_exit():
                break
        else:
            print("Invalid choice. Please enter a number between 1 and 2.")

if __name__ == "__main__":
    menu()
