import boto3
from setting import *
import time

if __name__ == '__main__':

    session = boto3.Session()
    kinesis_client = session.client('kinesis', region_name=REGION)
    response = kinesis_client.describe_stream(StreamName=K_STEAM)
    shard_id = response['StreamDescription']['Shards'][0]['ShardId']
    shard_iterator = kinesis_client.get_shard_iterator(StreamName=K_STEAM,
                                                       ShardId=shard_id,
                                                       ShardIteratorType='LATEST')
    my_shard_iterator = shard_iterator['ShardIterator']
    record_response = kinesis_client.get_records(ShardIterator=my_shard_iterator, Limit=100)
    while 'NextShardIterator' in record_response:
        record_response = kinesis_client.get_records(ShardIterator=record_response['NextShardIterator'], Limit=100)
        if len(record_response['Records']) > 0:
            for record in record_response['Records']:
                print(record)
                time.sleep(1)
