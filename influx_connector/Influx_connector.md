# Monitor service example for Auroral Node-RED adapter


## Instalation
Import InfluxConnector.json file into Node-RED using Menu -> import -> Clipboard / load file

## Goal 
Periodically request data from sensor accesible from your node and store them in InfluxDB.



![Flow view!](/influx_connector/Influx_connector.png)


## Requirements
- InfluxDB server 
    - Can be installed on the same machine, docker enviroment or elsewhere, you just need to know the IP address (or DNS name) and port
    - If running on the same machine, you can use myhost DNS name (instead of localhost)

## Used extensions
    - node-red-contrib-auroral  >= 2.1.4
    - node-red-contrib-influxdb >= 0.6.1


### Who do I talk to? ###

Developed by bAvenir

* jorge.almela@bavenir.eu
* peter.drahovsky@bavenir.eu