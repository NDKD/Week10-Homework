def get_noise_trend(data):
    import statsmodels.api as sm
    df_noise, df_trend = sm.tsa.filters.hpfilter(data)
    data = data.to_frame()
    data["noise"] = df_noise
    data["trend"] = df_trend
    return data