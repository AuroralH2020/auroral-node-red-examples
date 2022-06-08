# AURORAL device exposing MQTT messages as events
Registers two AURORAL devices:
- Consumer: creates events when message is sent to MQTT channel
- Producer listens to event created by Producer and writes it to debug log
## Instalation and usage
- Import Test_device.json file into Node-RED using Menu -> import -> Clipboard / load file.
- Because OIDs are assigned dynamically during registration, before usage proper OID (of Producer) needs to be filled in Consumers node subscription option. It can be found in device properties view.
![Flow view!](/mqtt_device/Properties_consumer.png)
- Please enable devices (and re-deploy flow) before testing 

- With *Send MQTT message* you can try event subscription

## Goal 
Serve static test data in Auroral platform.

![Flow view!](/mqtt_device/Mqtt_device.png)

## Used extensions
    - node-red-contrib-auroral  >= 2.0.0

### Who do I talk to? ###

Developed by bAvenir

* jorge.almela@bavenir.eu
* peter.drahovsky@bavenir.eu