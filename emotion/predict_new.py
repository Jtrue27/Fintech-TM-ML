import os
import pickle
import numpy as np
import pandas as pd
import operate_data as od
import ml_model as ml
from  demo import Predictor
import argparse
import ipdb

VECTOR_MODE = {'onehot': 0, 'wordfreq': 1, 'twovec': 2, 'tfidf': 3, 'outofdict': 4}

parser=argparse.ArgumentParser()
parser.add_argument("--path",type=str,default='./data/China',help="input data")
opt = parser.parse_args()

def read_news(path):
    new_dataframe=pd.read_csv(path)
    ipdb.set_trace()
    print(new_dataframe['Time']






if __name__ == "__main__":

    read_news(opt.path)