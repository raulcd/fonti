Title: ELK on Docker
Date: 2015-02-11 18:30
Summary: Set up Elasticsearch - Logstash - Kibana stack in a docker container
Status: draft

While doing performance testing on a project I got to the situation where 
I need to define the navigation profile of the current users to be sure that
the tests are reflecting what the users are doing.

We do not have any type of analysis and the only thing that I have are
the access logs of our web server.

I have heard of Logstash, Elasticsearch and Kibana so I thought it would be good to give it a try.

## ELK Stack

### Elasticsearch

[Elasticsearch](http://www.elasticsearch.org/overview/elasticsearch) and 
the [Github Elasticsearch project](https://github.com/elasticsearch/elasticsearch)
In order to set up Elastic Search the only thing that you need to do is, download the package an execute it:

```console
➜  wget https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.4.2.tar.gz
➜  tar -zxvf elasticsearch-1.4.2.tar.gz
➜  cd elasticsearch-1.4.2
➜  ./bin/elasticsearch
[2015-02-11 10:43:21,573][INFO ][node                     ] [Jumbo Carnation] version[1.4.2], pid[6019], build[927caff/2014-12-16T14:11:12Z]
[2015-02-11 10:43:21,574][INFO ][node                     ] [Jumbo Carnation] initializing ...
[2015-02-11 10:43:21,578][INFO ][plugins                  ] [Jumbo Carnation] loaded [], sites []
[2015-02-11 10:43:23,483][INFO ][node                     ] [Jumbo Carnation] initialized
[2015-02-11 10:43:23,483][INFO ][node                     ] [Jumbo Carnation] starting ...
[2015-02-11 10:43:23,528][INFO ][transport                ] [Jumbo Carnation] bound_address {inet[/0:0:0:0:0:0:0:0:9300]}, publish_address {inet[/10.105.14.17:9300]}
[2015-02-11 10:43:23,540][INFO ][discovery                ] [Jumbo Carnation] elasticsearch/_EGLpT09SfCaIbfW4KCSqg
[2015-02-11 10:43:27,315][INFO ][cluster.service          ] [Jumbo Carnation] new_master [Jumbo Carnation][_EGLpT09SfCaIbfW4KCSqg][pumuki][inet[/10.105.14.17:9300]], reason: zen-disco-join (elected_as_master)
[2015-02-11 10:43:27,332][INFO ][http                     ] [Jumbo Carnation] bound_address {inet[/0:0:0:0:0:0:0:0:9200]}, publish_address {inet[/10.105.14.17:9200]}
[2015-02-11 10:43:27,332][INFO ][node                     ] [Jumbo Carnation] started
[2015-02-11 10:43:27,783][INFO ][gateway                  ] [Jumbo Carnation] recovered [4] indices into cluster_state
```

This will set elasticsearch web server listening on port 9200 on your localhost.

At this moment you should be able to retrieve the following information:

```console
➜  curl -XGET http://localhost:9200/
{
  "status" : 200,
  "name" : "Jumbo Carnation",
  "cluster_name" : "elasticsearch",
  "version" : {
    "number" : "1.4.2",
    "build_hash" : "927caff6f05403e936c20bf4529f144f0c89fd8c",
    "build_timestamp" : "2014-12-16T14:11:12Z",
    "build_snapshot" : false,
    "lucene_version" : "4.10.2"
  },
  "tagline" : "You Know, for Search"
}
```

You can also get the stats by doing:

```console
➜  curl -XGET http://localhost:9200/_stats
{"_shards":{"total":0,"successful":0,"failed":0},"_all":{"primaries":{},"total":{}},"indices":{}}
```

When I was playing I processes several times different logs. So in order to clean all the information of
my elasticsearch instance I found quite useful the following command that *wil remove* all your
existing data. So *BE CAREFULL*:

```console
➜  curl -XDELETE "http://localhost:9200/*"
{"acknowledged":true}
```

### Logstash

[Logstash](http://logstash.net/) and the [Github project repo](https://github.com/elasticsearch/logstash).

In order to setup Logstash you will need to Download the package:

```console
➜  wget https://download.elasticsearch.org/logstash/logstash/logstash-1.4.2.tar.gz
➜  tar -zxvf logstashh-1.4.2.tar.gz
➜  cd logstash-1.4.2
```

In order to process your Access logs and send them to elastic search you will need to create the logstash configuration file.
I have created the next one:

```console
➜  cat logstash_simple.conf 
input {
  file {
    path => "/var/logs/access-logs/*.log"
    type => "apache_access"
  }
}

filter {
  if [path] =~ "access" {
    mutate { replace => { "type" => "apache_access" } }
    grok {
      match => { "message" => "%{COMBINEDAPACHELOG}" }
    }
  }
  date {
    match => [ "timestamp" , "dd/MMM/yyyy:HH:mm:ss Z" ]
  }
}


output {
  elasticsearch_http {
    host => localhost 
  } 
  stdout { 
  } 
}
➜
```

In the input section we define which logs logstash needs to process. You can define
different types of input but we are getting directly from a file. To see other types of
input take a look at the [documentation](http://logstash.net/docs/1.4.2/).

The filter is how logstash will process your logs. We are using grok which is a like a regex parser 
for unstructured data. We just use the %{COMBINEDAPACHELOG} regex and set the date format.

For the output we have created two outputs. Our Elasticsearch instance and standard output.

In order to run logstash:

```console
➜  bin/logstash -f logstash_simple.conf
```

### Kibana

[Kibana](http://www.elasticsearch.org/overview/kibana/) is a visualization tool for data from 
elasticsearch. The [Github project](https://github.com/elasticsearch/kibana).

In order to set it up just download it and run it:

```console
➜  wget https://download.elasticsearch.org/kibana/kibana/kibana-4.0.0-beta3.tar.gz 
➜  tar -zxvf kibana-4.0.0-beta3.tar.gz
➜  cd kibana-4.0.0-beta3
➜  bin/kibana
The Kibana Backend is starting up... be patient
{"@timestamp":"2015-02-11T12:34:29+00:00","level":"INFO","name":"Kibana","message":"Kibana server started on tcp://0.0.0.0:5601 in production mode."}
```

And kibana should be running on your localhost at port 5601.

The first page will ask you to create an index. If you don't have any data yet you will not be able to create it.
You can create index and start playing querying the data.

## Deploy

Once the Stack was locally working I thought it would be good to deploy it to one of our boxes
and send periodically our access logs to be able to have the logs updated every once in a while.

And I thought that maybe creating a container to be able to replicate it easily on the future may
be a good possibility.

### Docker Container Generation

Create one unique docker file. Not really the best practice but the easiest way:

Supervisor and mounting a volume exposing only the port for kibana. The volume is were the docs will be added.

In order to build the container you just need to run:

```console
docker build -t elk:latest .
```

You should have your image listed when

```console
➜  docker images
REPOSITORY                         TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
elk                                latest              28bf7af29dc1        55 seconds ago      575.7 MB
```


Separate containers (TODO)

### Deploying container

### Sending logs and processing
