# python-influxdb-example
Easy to understand python to influxdb example.
Assumes a working influxdb server. If you are really keen, fire up Grafana and hook it into Influxdb :)

## Requirements

* Best tested in the python environment (virtualenv).
* Tested on Python 2.7, should work on 3.X.
* Influxdb python client

## Quick Start

* Build you virtualenv

```
virtualenv influxdb/
```

* Source your virtualenv and install the required python modules

```
source influxdb/bin/activate
pip install influxdb
```

## How it works

The python code simply creates a connection to Influxdb, creates a database and inserts random values
via a JSON sample. It is a very easy way to understand how Influxdb works with python. 


