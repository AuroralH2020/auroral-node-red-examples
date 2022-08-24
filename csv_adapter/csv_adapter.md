# CSV adapter using Node Red

## Instalation
Import csv_adapter.json file into Node-RED using Menu -> import -> Clipboard / load file

## Goal 
Integrate CSV files and query its values with requests containing query parameters.

## Deployment
Before deploying the node red flow, replace the 'MyCSVChart' module and register your own item.

 * TD Example

```json
    {
        "adapterId": "csv-adapter",
        "securityDefinitions": {
            "nosec_sc": {
            "scheme": "nosec"
            }
        },
        "description": "CSV chart with reparability index",
        "properties": {
            "csv_measurement": {
            "forms": [
                {
                "href": "http://node-red:1250/api/property/fc21b238-6fa6-4f26-9daf-750ce030530c/csv_measurement",
                "op": "readproperty"
                }
            ],
            "monitors": "repairIndex",
            "readOnly": true,
            "title": "csv_measurement",
            "type": "number"
            }
        },
        "title": "MyCSVChart",
        "type": "Device",
        "@context": [
            "https://www.w3.org/2019/wot/td/v1",
            "https://w3c.github.io/wot-discovery/context/discovery-context.jsonld",
            "https://w3c.github.io/wot-discovery/context/discovery-context.jsonld"
        ],
        "security": [
            "nosec_sc"
        ],
        "@type": [
            "CSVChart"
        ]
    }
 ```

## Requesting values
Example request to retrieve values:
```bash
  curl -X 'GET' \
  'http://localhost:81/api/properties/<Origin_OID>/<Destination_OID>/csv_measurement?area=60&location=spain&age=15' \
  -H 'accept: application/json'  
```

## Used extensions
    - node-red-contrib-auroral  >= 2.1.4

### Who do I talk to? ###

Developed by bAvenir

* jorge.almela@bavenir.eu
* peter.drahovsky@bavenir.eu