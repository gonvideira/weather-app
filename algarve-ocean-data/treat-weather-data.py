"""Treating weather ocean data"""
import pandas as pd
from datetime import date
from datetime import timedelta
from matplotlib import pyplot as plt


# yesterday = date.today() - timedelta(days = 1)
FN = 'weather-data-HEIGHT.json'

# def import_height(file_name):
#     """Imports and cleans Data, returns dataframe"""
#     df = pd.read_json(file_name,encoding='utf8',convert_dates=['SDATA'])
#     df.set_index('SDATA',inplace=True)
#     return df

# def report_yesterday(df):
#     """Provides only yesterday's values"""
#     return df[yesterday:]

class HeightData():
    """Class that handles Wave Height Data"""
    
    def __init__(self,file_name) -> None:
        self.file_name = file_name
        self.yesterday = date.today() - timedelta(days = 1)
        self.one_month_ago = date.today() - timedelta(days = 30)

    def import_height(self):
        """Imports and cleans Data, returns dataframe"""
        df = pd.read_json(self.file_name,encoding='utf8',convert_dates=['SDATA'])
        df.set_index('SDATA',inplace=True)
        return df
    
    def yesterday_height(self):
        """Slices data for yesterday"""
        df = self.import_height()
        return (df[self.yesterday:]['HMAX'].max(),df[self.yesterday:]['HS'].max())
    
    def max_values(self):
        """Returns max values for Hs & Hmax and the respective dates"""
        df = self.import_height()
        max_hs = df['HS'].max()
        max_hs_date = df.index[df['HS'] == max_hs][0].strftime("%d %b, %Y")
        max_hmax = df['HMAX'].max()
        max_hmax_date = df.index[df['HMAX'] == max_hmax][0].strftime("%d %b, %Y")
        num_days = len(set(df.index.date))
        return f"Maximum Hs of {max_hs} ocurred at {max_hs_date} and maximum Hmax of {max_hmax} ocurred at {max_hmax_date}.\nWe have {num_days} day(s) of data!"

    def plot_date_rolling_30(self):
        """Plot on date"""
        df = self.import_height()
        df['Data'] = df.index.date
        grouped = df[self.one_month_ago:].groupby('Data').max()
        grouped.plot(kind="bar",title="Hs e Hmax para os ultimos dias!")
        # Bar labels here: https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_label_demo.html
        plt.show()
        return grouped
    
    def table_data(self):
        """Table / DataFrame with all the data"""
        df = self.import_height()
        df['Data'] = df.index.date
        grouped = df.groupby('Data').max()
        return grouped
    
    def plot_histogram(self):
        """Plots histogram with all data for max Hs daily"""
        df = self.import_height()
        df['Data'] = df.index.date
        grouped = df.groupby('Data').max()['HS']
        grouped.plot(kind="hist",title="Histograma de valores máximos de Hs diários!")
        # Bar labels here: https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_label_demo.html
        plt.show()
        return grouped

# df_all = data.import_height()
# HmaxYesterday, HsYesterday = data.yesterday_height()
# print(HmaxYesterday)
# print(HsYesterday)
# print(data.max_values())

if __name__ == "__main__":
    data = HeightData(FN)
    data.plot_histogram()
