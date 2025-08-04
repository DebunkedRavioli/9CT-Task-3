from data_module import load_data, plot_vacancies_and_cancellations, filter_data

def main():
    file_path = "busperformance_reports_may25.xlsx"
    print("📊 Welcome to the Bus Performance Dashboard")

    try:
        df = load_data(file_path)
    except Exception as e:
        print(f"❌ Failed to load data: {e}")
        return

    while True:
        print("\nMain Menu:")
        print("1. View data preview")
        print("2. Plot vacancies vs cancellations")
        print("3. Filter by region or month")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print(df.head())

        elif choice == "2":
            plot_vacancies_and_cancellations(df)

        elif choice == "3":
            region = input("Enter region (leave blank to skip): ").strip()
            month = input("Enter month (format YYYY-MM, leave blank to skip): ").strip()
            filtered_df = filter_data(df, region if region else None, month if month else None)
            print(filtered_df)

        elif choice == "4":
            print("👋 Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

