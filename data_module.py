import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    df = pd.read_excel(file_path, sheet_name="BusData")
    df['Month'] = pd.to_datetime(df['Month'], errors='coerce')
    return df.dropna(subset=['Month']).sort_values('Month')

def plot_vacancies_and_cancellations(df):
    fig, ax = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    ax[0].plot(df['Month'], df['Driver Vacancies'], marker='o', color='orange')
    ax[0].set_title('Driver Vacancies Over Time')
    ax[0].set_ylabel('Vacancies')
    ax[0].grid(True)

    ax[1].plot(df['Month'], df['% of services cancelled'], marker='o', color='red')
    ax[1].set_title('Service Cancellations Over Time')
    ax[1].set_ylabel('% Cancelled')
    ax[1].set_xlabel('Month')
    ax[1].grid(True)
    

    plt.tight_layout()
    plt.show()

def filter_data(df, region=None, month=None):
    if region:
        df = df[df['Region'].str.contains(region, case=False, na=False)]
    if month:
        df = df[df['Month'].dt.strftime('%Y-%m') == month]
    return df
