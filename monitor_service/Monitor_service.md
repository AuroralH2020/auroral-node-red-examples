# Monitor service example for Auroral Node-RED adapter

This is a service that can be integrated as a Node-RED flow. It registers a new service in AURORAL automatically and opens a UI on {nodered-host}:{nodered-port}/ui.
This UI lets the user discover the local node items and also remote nodes, featuring SPARQL queries that can be used as example. It also allows to consume data from nodes that belong to your organisation.

## Installation
Import Monitor_service.json file into Node-RED using Menu -> import -> Clipboard / load file.

SERVICE is updated, and will work with the latest version of the node

## Goal 
Monitor and request data from your organisation infrastructure.

## Used extensions
    - node-red-contrib-auroral  >= 2.0.0
    - node-red-dashboard        >= 3.1.7

### Who do I talk to? ###

Developed by bAvenir

* jorge.almela@bavenir.eu
* peter.drahovsky@bavenir.eu
