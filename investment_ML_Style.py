import pandas as pd
import matplotlib.pyplot as plot



def test_run():
        df = pd.read_csv("data/AAPL.csv")
        print (df.head(5)) 
        print (df[10:21])



def get_max_close(symbol):
    df = pd.read_csv("data/{}.csv".format(symbol))
    return df['Close'].max()

def test_run_extra():
    """Function called by test run"""
    for symbol in ['AAPL', 'IBM']:
        print ("Max Close")
        print (symbol, get_max_close(symbol))

    print ("Mean Value")
    print (symbol, get_mean_volume('IBM'))

def get_mean_volume(symbol):
        df = pd.read_csv("data/{}.csv".format(symbol))
        return df['Volume'].mean()

def plot_symbol():
    df = pd.read_csv("data/AAPL.csv")
    print (df['Adj Close'])
    df ['Adj Close'].plot()
    plot.show()

def plot_high(symbol):
    df = pd.read_csv("data/{}.csv".format(symbol))
    print (df['High'])
    df ['High'].plot()
    plot.show()

def plot_adj_close(symbol):
    df = pd.read_csv("data/{}.csv".format(symbol))
    df [['High', 'Adj Close']].plot()
    plot.show()


def data_price_range(symbols,start,end):
        start_date= start
        end_date= end
        dates = pd.date_range(start_date,end_date)
        #print (dates[0])

        #create an empty dataframe
        dataFrameOne = pd.DataFrame(index = dates)

        #read SPY data into temporary dataframe
        dfSPY = pd.read_csv("data/SPY.csv", 
                            index_col="Date", 
                            parse_dates = True, 
                            usecols = ['Date', 'Adj Close'], 
                            na_values = ['nan'])

        #Rename 'Adj Close' column to 'SPY' to prevent clash
        dfSPY = dfSPY.rename(columns={'Adj Close':'SPY Adj Close'})
        #Join the dataframes using DataFrame.join()
        dataFrameOne = dataFrameOne.join(dfSPY, how = 'inner')

        #Drop NaN Values not required if we use how = 'inner' in join
        #dataFrameOne = dataFrameOne.dropna()

        #read more then one Stocks
        for symbol in symbols:
            df_temp = pd.read_csv("data/{}.csv".format(symbol), 
                            index_col="Date", 
                            parse_dates = True, 
                            usecols = ['Date', 'Adj Close'], 
                            na_values = ['nan'])
            #Rename 'Adj Close' column to 'SPY' to prevent clash
            df_temp = df_temp.rename(columns={'Adj Close' : symbol+' Adj Close'})
            dataFrameOne = dataFrameOne.join(df_temp)

        return dataFrameOne

def plot_data_frame(df, title="Stock prices", normalize = True):
    if normalize == True:
        df = normalize_data(df)

    #plot stock series
    ax = df.plot(title = title, fontsize = 2)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plot.show()

def normalize_data(df):
    #normalize stock prices using the first row of the dataframe.
    return df/df.ix[0,:]

if __name__ == "__main__":
        #test_run()
        #test_run_extra()
        #plot_symbol()
        #plot_high('IBM')
        #plot_adj_close('AAPL')
        plot_data_frame(data_price_range(['IBM','AAPL', 'GOOG', 'GLD'],'2019-01-01','2019-01-31'), title= "Stock Prices", normalize = True)