import sys
from flask import Flask, render_template
from flask_socketio import SocketIO
from threading import Lock
import boto3
from setting import *
import json
import datetime
import time

async_mode = None
stream_name = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()


def background_thread():
    session = boto3.Session()
    kinesis_client = session.client('kinesis', region_name=REGION)
    response = kinesis_client.describe_stream(StreamName=stream_name)
    shard_id = response['StreamDescription']['Shards'][0]['ShardId']
    shard_iterator = kinesis_client.get_shard_iterator(StreamName=stream_name,
                                                       ShardId=shard_id,
                                                       ShardIteratorType='LATEST')
    my_shard_iterator = shard_iterator['ShardIterator']
    record_response = kinesis_client.get_records(
        ShardIterator=my_shard_iterator, Limit=100)
    while 'NextShardIterator' in record_response:
        record_response = kinesis_client.get_records(
            ShardIterator=record_response['NextShardIterator'], Limit=100)
        if len(record_response['Records']) > 0:
            for record in record_response['Records']:
                print(record)
                record_data_str = record['Data'].decode("utf-8")
                t = json.loads(record_data_str)
                socketio.emit('push', t)


@socketio.on('connect')
def handle_my_custom_event(json):
    print('received json: ' + str(json))
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)


@app.route("/")
def hello():
    return render_template('index.html')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        stream_name = sys.argv[1]
        socketio.run(app, host="0.0.0.0", port=3008, debug=True)
    else:
        raise ValueError("need param for stream name")
