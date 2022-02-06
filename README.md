# kinesis-workshop
## 安装aws cli
```
https://aws.amazon.com/cn/cli/

https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html
```
## 配置环境变量
```
https://docs.aws.amazon.com/zh_cn/cli/latest/userguide/cli-configure-envvars.html
export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
export AWS_DEFAULT_REGION=us-west-2
```
## 开启aurora 
## 安装maxwell
拉取
```
docker pull zendesk/maxwell
```
启动
```
docker run -it --rm --name maxwell-kinesis -e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -v `cd && pwd`/.aws:/root/.aws zendesk/maxwell  sh -c 'cp /app/kinesis-producer-library.properties.example /app/kinesis-producer-library.properties && echo "Region=ap-northeast-1" >>/app/kinesis-producer-library.properties && /app/bin/maxwell --user={DB_USERNAME} --password={DB_PASSWORD} --host={MYSQL_RDS_URI} --producer=kinesis --kinesis_stream={KINESIS_NAME}'
```
修改成自己的参数
```
docker run -it --rm --name maxwell -e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -v `cd && pwd`/.aws:/root/.aws zendesk/maxwell sh -c 'cp /app/kinesis-producer-library.properties.example /app/kinesis-producer-library.properties && echo "Region=$AWS_DEFAULT_REGION" >> /app/kinesis-producer-library.properties && bin/maxwell --user=admin --password=Demo1234 --host=abdemo.cluster-cqshokmqgqfv.ap-northeast-1.rds.amazonaws.com --producer=kinesis --kinesis_stream=order_ds'
```

```

CREATE TABLE IF NOT EXISTS customer (
    email varchar(20) NOT NULL,
    level INT NOT NULL,
    sex varchar(20) NOT NULL,
    PRIMARY KEY (email)
);
```

```
        this.email = c.getEmail();
        this.sex =c.getSex();
        this.city = e.getCity();
        this.orderId = e.getOrderId();
        this.status = e.getStatus();
        this.goodCount = e.getGoodCount();
        this.amount = e.getAmount();
        this.createTime = e.getCreateTime();

CREATE TABLE IF NOT EXISTS customer (
    email varchar(20) NOT NULL,
    sex varchar(20) NOT NULL,
    level INT,
    city varchar(20) NOT NULL,
    orderId INT,
    status varchar(20) NOT NULL,
    goodCount INT,
    amount Double,
    createTime Timestamp
);
```

firehouse
```
161.189.23.64/27

mock-order-event
metrics-ds

json 'auto'
```
