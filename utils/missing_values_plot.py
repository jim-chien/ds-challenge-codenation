def plot_missing_hist(dataframe):
    missing_values_df = round(dataframe.isna().sum() / dataframe.shape[0], 2)
    missing_values_df.plot.hist(bins=5)
