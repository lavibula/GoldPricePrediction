
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
#load model code

def scale_sequence_data(df,timesteps ,close_col_idx):
    x = []
    y = []
    timeLine=[]
    for i in range(len(df)-timesteps):    
        scaler=MinMaxScaler()      
        scaler.fit(df[i:i+timesteps,:])
        timeLine.append((scaler.data_min_[close_col_idx],scaler.data_max_[close_col_idx]))
        x.append(scaler.transform(df[i:i+timesteps,:]))
        value=df[i+timesteps].reshape(1,-1)
        value=scaler.transform(value)
        y.append(value[:,close_col_idx])
    return np.array(x),np.array(y),timeLine
def inverseTransform(value, timeline):
    result = []
    for i in range(len(timeline)):
        min_val = timeline[i][0]
        max_val = timeline[i][1]
        original_value = (value[i] * (max_val - min_val)) + min_val
        result.append(original_value)
    return np.array(result)
if __name__=='__main__':
    whole_file="https://raw.githubusercontent.com/lavibula/GoldPricePrediction/main/data/data_preparation/data_preparation.csv"
    data =pd.read_csv(whole_file)
    data=data[::-1]
    data = data.reset_index(drop=True)
    time=data['Date']
    data_prepare=data.drop(['Date'], axis=1).to_numpy()
    data_prepare=np.asarray(data_prepare).astype('float32')
    timesteps=30
    #assume we get 30 days of data start at 1/1/2023 to predict day 31/1
    indices = [index for index, date in enumerate(time) if date == "2023-02-15"]
    get_data=data_prepare[indices[0]:indices[0]+30]
    input_data=scale_sequence_data(get_data,timesteps,data.columns.get_loc('GOLD_close'))
    #load model here
