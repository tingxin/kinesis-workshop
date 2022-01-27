from datetime import datetime, timedelta
import json
import random
import boto3
from setting import *
import time
import sys
from mock import gen


if __name__ == '__main__':

    if len(sys.argv) > 1:
        stream_name = sys.argv[1]
    else:
        raise ValueError("need param for stream name")

    print(f"prepare to send data to {stream_name}")
    creator = gen(500, 5000)
    session = boto3.Session()
    kinesis_client = session.client('kinesis', region_name=REGION)
    for item in creator:
        kinesis_client.put_record(
            StreamName=stream_name,
            Data=json.dumps(item),
            PartitionKey=item["city"])
        print(item)
