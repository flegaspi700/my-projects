
"""
Distributed Machine Learning with Google Cloud ML

sudo apt-get update
sudo apt-get install virtualenv
virtualenv -p python3 venv
source venv/bin/activate

sudo apt -y update
sudo apt -y upgrade

sudo apt -y install python3-pip

pip install --upgrade pip

#Define local environment variables:

export PROJECT_ID=$(gcloud info --format='value(config.project)')
export BUCKET=${PROJECT_ID}

gsutil cp gs://${BUCKET}/flights/chapter9/linear-model.tar.gz ~

cd ~
tar -zxvf linear-model.tar.gz

cd ~/tensorflow

nano -w ~/tensorflow/flights/trainer/model.py

"""

#Add a function that applies a dimensionality reduction function to the categorical fields. 
#This reduces the number of one-hot encoded variables from the 1000 discretized values that 
# was used when experimenting with the linear categorizer. 
# Embedding converts a sparse data field that might be represented with 1000 separate columns 
# when one-hot encoded and instead maps those to a much smaller number, 
# significantly reducing the number of variable dimensions that have to be dealt with.

"""
  #estimator = linear_model(output_dir)
  estimator = dnn_model(output_dir)

  export REGION=us-central1
export OUTPUT_DIR=gs://${BUCKET}/flights/chapter9/output
export DATA_DIR=gs://${BUCKET}/flights/chapter8/output

export JOBNAME=dnn_flights_$(date -u +%y%m%d_%H%M%S)
cd ~/tensorflow

gcloud ai-platform jobs submit training $JOBNAME \
  --module-name=trainer.task \
  --package-path=$(pwd)/flights/trainer \
  --job-dir=$OUTPUT_DIR \
  --staging-bucket=gs://$BUCKET \
  --region=$REGION \
  --scale-tier=STANDARD_1 \
  --runtime-version=1.15 \
  -- \
  --output_dir=$OUTPUT_DIR \
  --traindata $DATA_DIR/train* --evaldata $DATA_DIR/test*

  nano -w ~/tensorflow/flights/trainer/model.py

"""


"""
  #estimator = linear_model(output_dir)
  # estimator = dnn_model(output_dir)
  estimator =  wide_and_deep_model(output_dir, 5, '64,32', 0.01)

export OUTPUT_DIR=gs://${BUCKET}/flights/chapter9/output2

export JOBNAME=wide_and_deep_flights_$(date -u +%y%m%d_%H%M%S)

gcloud ai-platform jobs submit training $JOBNAME \
  --module-name=trainer.task \
  --package-path=$(pwd)/flights/trainer \
  --job-dir=$OUTPUT_DIR \
  --staging-bucket=gs://$BUCKET \
  --region=$REGION \
  --scale-tier=STANDARD_1 \
  --runtime-version=1.15 \
  -- \
  --output_dir=$OUTPUT_DIR \
  --traindata $DATA_DIR/train* --evaldata $DATA_DIR/test*

  nano -w ~/tensorflow/flights/trainer/model.py

  MODEL_LOCATION=$(gsutil ls $OUTPUT_DIR/export/exporter | tail -1)

  gcloud ai-platform models create flights --regions us-central1
gcloud ai-platform versions create v1 --model flights \
                                    --origin ${MODEL_LOCATION} \
                                    --runtime-version 1.15 \
                                    --region global


pip install --upgrade google-api-python-client
pip install --upgrade oauth2client


python

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
import os
import json

credentials = GoogleCredentials.get_application_default()

api = discovery.build('ml', 'v1', credentials=credentials)
PROJECT = os.environ['PROJECT_ID']
parent = 'projects/%s/models/%s/versions/%s' % (PROJECT, 'flights', 'v1')

request_data = {'instances':
  [
      {
        'dep_delay': 16.0,
        'taxiout': 13.0,
        'distance': 160.0,
        'avg_dep_delay': 13.34,
        'avg_arr_delay': 67.0,
        'carrier': 'AS',
        'dep_lat': 61.17,
        'dep_lon': -150.00,
        'arr_lat': 60.49,
        'arr_lon': -145.48,
        'origin': 'ANC',
        'dest': 'CDV'
      }
  ]
}

response = api.projects().predict(body=request_data, name=parent).execute()
print ("response={0}".format(response))


"""

import tensorflow as tf
#from tensorflow.contrib.learn.python.learn.utils import saved_model_export_utils
#import tensorflow.estimator as tflearn
#import tensorflow.contrib.layers as tflayers
#import tensorflow.contrib.metrics as tfmetrics
import numpy as np

CSV_COLUMNS  = \
('ontime,dep_delay,taxiout,distance,avg_dep_delay,avg_arr_delay,' + \
 'carrier,dep_lat,dep_lon,arr_lat,arr_lon,origin,dest').split(',')
LABEL_COLUMN = 'ontime'
DEFAULTS     = [[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],\
                ['na'],[0.0],[0.0],[0.0],[0.0],['na'],['na']]

def read_dataset(filename, mode=tf.contrib.learn.ModeKeys.EVAL,
                 batch_size=512, num_training_epochs=10):
   # the actual input function passed to TensorFlow
   def _input_fn():
      # This is double indented to make a later edit simpler
      if mode == tf.contrib.learn.ModeKeys.TRAIN:
         num_epochs = num_training_epochs
      else:
         num_epochs = 1
      # could be a path to one file or a file pattern.
      input_file_names = tf.train.match_filenames_once(filename)
      filename_queue = tf.train.string_input_producer(
          input_file_names, num_epochs=num_epochs, shuffle=True)
      # Read in and parse the CSV
      reader = tf.TextLineReader()
      _, value = reader.read_up_to(
          filename_queue, num_records=batch_size)
      value_column = tf.expand_dims(value, -1)
      columns = tf.decode_csv(value_column, record_defaults=DEFAULTS)
      features = dict(zip(CSV_COLUMNS, columns))
      label = features.pop(LABEL_COLUMN)
      return features, label
   # return input function callback.
   return _input_fn

def get_features_raw():
    real = {
      colname : tflayers.real_valued_column(colname) \
          for colname in \
            ('dep_delay,taxiout,distance,avg_dep_delay,avg_arr_delay' +
             ',dep_lat,dep_lon,arr_lat,arr_lon').split(',')
    }
    sparse = {
      'carrier': tflayers.sparse_column_with_keys('carrier',
                 keys='AS,VX,F9,UA,US,WN,HA,EV,MQ,DL,OO,B6,NK,AA'.split(',')),

      'origin' : tflayers.sparse_column_with_hash_bucket('origin',
                 hash_bucket_size=1000),

      'dest'   : tflayers.sparse_column_with_hash_bucket('dest',
                 hash_bucket_size=1000)
    }
    return real, sparse

def get_features_ch7():
    # Using three basic inputs
    real = {
      colname : tflayers.real_valued_column(colname) \
          for colname in \
            ('dep_delay,taxiout,distance').split(',')
    }
    sparse = {}
    return real, sparse

def get_features_ch8():
    # Using the basic three inputs plus calculated time averages
    real = {
      colname : tflayers.real_valued_column(colname) \
          for colname in \
            ('dep_delay,taxiout,distance,avg_dep_delay,avg_arr_delay').split(',')
    }
    sparse = {}
    return real, sparse

def get_features():
    # Select the active get_feature function
    return get_features_raw()
    #return get_features_ch7()
    #return get_features_ch8()

def my_rmse(labels,predictions):
    predicted_classes = predictions['probabilities'][:,1]
    custom_metric = tf.metrics.root_mean_squared_error(labels, predicted_classes,name="rmse")
    return {'rmse':custom_metric}

def parse_hidden_units(s):
    return [int(item) for item in s.split(',')]

def wide_and_deep_model(output_dir,nbuckets=5,
                        hidden_units='64,32', learning_rate=0.01):
    real, sparse = get_features()
    # lat/lon cols can be discretized to "air traffic corridors"
    latbuckets = np.linspace(20.0, 50.0, nbuckets).tolist()
    lonbuckets = np.linspace(-120.0, -70.0, nbuckets).tolist()
    disc = {}
    disc.update({
       'd_{}'.format(key) : \
           tflayers.bucketized_column(real[key], latbuckets) \
           for key in ['dep_lat', 'arr_lat']
    })
    disc.update({
       'd_{}'.format(key) : \
           tflayers.bucketized_column(real[key], lonbuckets) \
           for key in ['dep_lon', 'arr_lon']
    })
    # cross columns that make sense in combination
    sparse['dep_loc'] = tflayers.crossed_column( \
           [disc['d_dep_lat'], disc['d_dep_lon']],\
           nbuckets*nbuckets)
    sparse['arr_loc'] = tflayers.crossed_column( \
           [disc['d_arr_lat'], disc['d_arr_lon']],\
           nbuckets*nbuckets)
    sparse['dep_arr'] = tflayers.crossed_column( \
           [sparse['dep_loc'], sparse['arr_loc']],\
           nbuckets ** 4)
    sparse['ori_dest'] = tflayers.crossed_column( \
           [sparse['origin'], sparse['dest']], \
           hash_bucket_size=1000)

    # create embeddings of all the sparse columns
    embed = {
       colname : create_embed(col) \
          for colname, col in sparse.items()
    }
    real.update(embed)

    lin_opt=tf.train.FtrlOptimizer(learning_rate=learning_rate)
    l_rate=learning_rate*0.25
    dnn_opt=tf.train.AdagradOptimizer(learning_rate=l_rate)
    estimator = tflearn.DNNLinearCombinedClassifier(
         model_dir=output_dir,
         linear_feature_columns=sparse.values(),
         dnn_feature_columns=real.values(),
         dnn_hidden_units=parse_hidden_units(hidden_units),
         linear_optimizer=lin_opt,
         dnn_optimizer=dnn_opt)
    estimator = tf.contrib.estimator.add_metrics(estimator, my_rmse)
    return estimator

def linear_model(output_dir):
    real, sparse = get_features()
    all = {}
    all.update(real)
    all.update(sparse)
    estimator = tflearn.LinearClassifier(model_dir=output_dir, feature_columns=all.values())
    estimator = tf.contrib.estimator.add_metrics(estimator, my_rmse)
    return estimator

def create_embed(sparse_col):
    dim = 10 # default
    if hasattr(sparse_col, 'bucket_size'):
       nbins = sparse_col.bucket_size
       if nbins is not None:
          dim = 1 + int(round(np.log2(nbins)))
    return tflayers.embedding_column(sparse_col, dimension=dim)

def dnn_model(output_dir):
    real, sparse = get_features()
    all = {}
    all.update(real)

    # create embeddings of the sparse columns
    embed = {
       colname : create_embed(col) \
          for colname, col in sparse.items()
    }
    all.update(embed)

    estimator = tflearn.DNNClassifier(
         model_dir=output_dir,
         feature_columns=all.values(),
         hidden_units=[64, 16, 4])
    estimator = tf.contrib.estimator.add_metrics(estimator, my_rmse)
    return estimator

def serving_input_fn():
    real, sparse = get_features()

    feature_placeholders = {
      key : tf.placeholder(tf.float32, [None]) \
        for key in real.keys()
    }
    feature_placeholders.update( {
      key : tf.placeholder(tf.string, [None]) \
        for key in sparse.keys()
    } )

    features = {
      # tf.expand_dims will insert a dimension 1 into tensor shape
      # This will make the input tensor a batch of 1
      key: tf.expand_dims(tensor, -1)
         for key, tensor in feature_placeholders.items()
    }
    return tf.estimator.export.ServingInputReceiver(
      features,
      feature_placeholders)

def run_experiment(traindata,evaldata,output_dir):
  train_input = read_dataset(traindata,\
                 mode=tf.contrib.learn.ModeKeys.TRAIN)
  # Don't shuffle evaluation data
  eval_input = read_dataset(evaldata)
  train_spec = tf.estimator.TrainSpec(train_input, max_steps=1000)
  exporter = tf.estimator.LatestExporter('exporter', serving_input_fn, exports_to_keep=None)
  eval_spec  = tf.estimator.EvalSpec(eval_input,exporters=exporter)
  run_config = tf.estimator.RunConfig()
  run_config = run_config.replace(model_dir=output_dir)
  print('model dir {}'.format(run_config.model_dir))
  #estimator = linear_model(output_dir)
  #estimator = dnn_model(output_dir)
  estimator =  wide_and_deep_model(output_dir, 5, '64,32', 0.01)

  tf.estimator.train_and_evaluate(estimator, train_spec, eval_spec)

"""
Submit the Cloud-ML task for the new model:

export OUTPUT_DIR=gs://${BUCKET}/flights/chapter9/output3

export JOBNAME=learn_rate_flights_$(date -u +%y%m%d_%H%M%S)

gcloud ai-platform jobs submit training $JOBNAME \
  --module-name=trainer.task \
  --package-path=$(pwd)/flights/trainer \
  --job-dir=$OUTPUT_DIR \
  --staging-bucket=gs://$BUCKET \
  --region=$REGION \
  --scale-tier=STANDARD_1 \
  --runtime-version=1.15 \
  -- \
  --output_dir=$OUTPUT_DIR \
  --traindata $DATA_DIR/train* --evaldata $DATA_DIR/test*

Deploy model
MODEL_LOCATION=$(gsutil ls $OUTPUT_DIR/export/exporter | tail -1)

gcloud ai-platform models create flights --regions us-central1
gcloud ai-platform versions create v1 --model flights \
                                    --origin ${MODEL_LOCATION} \
                                    --runtime-version 1.15 \
                                    --region global
                                    

"""