import boto3
from setting import *
import time
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        stream_name = sys.argv[1]
    else:
        raise ValueError("need param for stream name")

    print(f"prepare to read data to {stream_name}")
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
                time.sleep(1)
