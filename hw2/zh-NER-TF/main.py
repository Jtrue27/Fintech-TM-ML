import tensorflow as tf
import numpy as np
import os, argparse, time, random
from model import BiLSTM_CRF
from utils import str2bool, get_logger, get_entity
from data import read_corpus, read_dictionary, tag2label, random_embedding
import ipdb
import pandas as pd



## Session configuration
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # default: 0
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
config.gpu_options.per_process_gpu_memory_fraction = 0.2  # need ~700MB GPU memory


## hyperparameters
parser = argparse.ArgumentParser(description='BiLSTM-CRF for Chinese NER task')
parser.add_argument('--train_data', type=str, default='data_path', help='train data source')
parser.add_argument('--test_data', type=str, default='data_path', help='test data source')
parser.add_argument('--batch_size', type=int, default=64, help='#sample of each minibatch')
parser.add_argument('--epoch', type=int, default=40, help='#epoch of training')
parser.add_argument('--hidden_dim', type=int, default=300, help='#dim of hidden state')
parser.add_argument('--optimizer', type=str, default='Adam', help='Adam/Adadelta/Adagrad/RMSProp/Momentum/SGD')
parser.add_argument('--CRF', type=str2bool, default=True, help='use CRF at the top layer. if False, use Softmax')
parser.add_argument('--lr', type=float, default=0.001, help='learning rate')
parser.add_argument('--clip', type=float, default=5.0, help='gradient clipping')
parser.add_argument('--dropout', type=float, default=0.5, help='dropout keep_prob')
parser.add_argument('--update_embedding', type=str2bool, default=True, help='update embedding during training')
parser.add_argument('--pretrain_embedding', type=str, default='random', help='use pretrained char embedding or init it randomly')
parser.add_argument('--embedding_dim', type=int, default=300, help='random init char embedding_dim')
parser.add_argument('--shuffle', type=str2bool, default=True, help='shuffle training data before each epoch')
parser.add_argument('--mode', type=str, default='demo', help='train/test/demo')
parser.add_argument('--demo_model', type=str, default='1521112368', help='model for test and demo')
args = parser.parse_args()


## get char embeddings
word2id = read_dictionary(os.path.join('.', args.train_data, 'word2id.pkl'))
if args.pretrain_embedding == 'random':
    embeddings = random_embedding(word2id, args.embedding_dim)
else:
    embedding_path = 'pretrain_embedding.npy'
    embeddings = np.array(np.load(embedding_path), dtype='float32')


## read corpus and get training data
if args.mode != 'demo':
    train_path = os.path.join('.', args.train_data, 'train_data')
    test_path = os.path.join('.', args.test_data, 'test_data')
    train_data = read_corpus(train_path)
    test_data = read_corpus(test_path); test_size = len(test_data)


## paths setting
paths = {}
timestamp = str(int(time.time())) if args.mode == 'train' else args.demo_model
output_path = os.path.join('.', args.train_data+"_save", timestamp)
if not os.path.exists(output_path): os.makedirs(output_path)
summary_path = os.path.join(output_path, "summaries")
paths['summary_path'] = summary_path
if not os.path.exists(summary_path): os.makedirs(summary_path)
model_path = os.path.join(output_path, "checkpoints/")
if not os.path.exists(model_path): os.makedirs(model_path)
ckpt_prefix = os.path.join(model_path, "model")
paths['model_path'] = ckpt_prefix
result_path = os.path.join(output_path, "results")
paths['result_path'] = result_path
if not os.path.exists(result_path): os.makedirs(result_path)
log_path = os.path.join(result_path, "log.txt")
paths['log_path'] = log_path
get_logger(log_path).info(str(args))


## training model
if args.mode == 'train':
    model = BiLSTM_CRF(args, embeddings, tag2label, word2id, paths, config=config)
    model.build_graph()

    ## hyperparameters-tuning, split train/dev
    # dev_data = train_data[:5000]; dev_size = len(dev_data)
    # train_data = train_data[5000:]; train_size = len(train_data)
    # print("train data: {0}\ndev data: {1}".format(train_size, dev_size))
    # model.train(train=train_data, dev=dev_data)

    ## train model on the whole training data
    print("train data: {}".format(len(train_data)))
    model.train(train=train_data, dev=test_data)  # use test_data as the dev_data to see overfitting phenomena

## testing model
elif args.mode == 'test':
    ckpt_file = tf.train.latest_checkpoint(model_path)
    print(ckpt_file)
    paths['model_path'] = ckpt_file
    model = BiLSTM_CRF(args, embeddings, tag2label, word2id, paths, config=config)
    model.build_graph()
    print("test data: {}".format(test_size))
    model.test(test_data)

## demo
elif args.mode == 'demo':
    ckpt_file = tf.train.latest_checkpoint(model_path)
    print(ckpt_file)
    paths['model_path'] = ckpt_file
    model = BiLSTM_CRF(args, embeddings, tag2label, word2id, paths, config=config)
    model.build_graph()
    saver = tf.train.Saver()
    with tf.Session(config=config) as sess:
        print('============= demo =============')
        saver.restore(sess, ckpt_file)
        # while(1):
            # print('Please input your sentence:')
            # demo_sent = input() 
        with open('data.txt','r') as fp:
            all_lines = fp.readlines()
        demo_sent=all_lines
        # seg_list=[t for t in jieba.cut(demo_sent,cut_all=False) if t not in stops]\
        PERList = []
        LOCList = []
        PERArray = []
        LOCArray = []
        if demo_sent == '':
                print('See you next time!')
                # break
        else:
            for demo in demo_sent:
                demo_sent = list(demo.strip())
                demo_data = [(demo_sent, ['O'] * len(demo_sent))]
                tag = model.demo_one(sess, demo_data)
                PER, LOC, ORG = get_entity(tag, demo_sent)
                PERList += PER
                LOCList += LOC
                PERArray += [PER]
                LOCArray += [LOC]
                # ipdb.set_trace()
                # TODO 
                # Save PER,LOC,ORG to dataframe to csv
                # dict={}
                # occurrences=dict
                # print('PER: {}\nLOC: {}\nORG: {}'.format(PER, LOC, ORG))
                # co_occur = pd.DataFrame.from_dict(occurrences)
                # co_occur.to_csv('co-occurancy_matrix.csv')
        PERList = list(set(PERList))
        LOCList = list(set(LOCList))
        # print('PERList', PERList)
        # print('LOCList', LOCList)
        # dictionary = dict(zip(LOCList, PERList))
        # print('dictionary',dictionary)
        occurrences = np.zeros((len(LOCList),len(PERList)))
        for i in range(0,len(LOCArray)):
            for j in range(0, len(LOCArray[i])):
                for k in range(0, len(PERArray[i])):
                    occurrences[LOCList.index(LOCArray[i][j])][PERList.index(PERArray[i][k])] += 1
        print('occurrences',occurrences)
        co_occur = pd.DataFrame.from_dict(occurrences)
        co_occur.columns=PERList
        co_occur.index=LOCList
        co_occur.to_csv('co-occurancy_matrix.csv')
        print(len(PERList))
        # print('PERArray', PERList)
        # print(len(LOCList))
        # print('LOCArray', LOCList)

           
        
