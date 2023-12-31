"""This ACI Sandbox Lab contains a shared ACI Server Instance.

url: https://sandboxapicdc.cisco.com

    username: admin
    password: !v3G@!4@Y

    POST http://APIC-IP/api/aaaLogin.json HTTP/1.1
Content-Type: application/json

{
    "aaaUser" : {
        "attributes" : {
            "name" : "APIC_USER",
            "pwd" : "APIC_PASSWORD"
        }
    }
}
"""

import requests
import json
import conf

requests.packages.urllib3.disable_warnings()
url ="https://sandboxapicdc.cisco.com/api/aaaLogin.json"
dato ={
    "aaaUser" : {
        "attributes" : {
            "name" : conf.usuario,
            "pwd" : conf.clave
        }
    }
}

cabecera = {"Content-Type": "application/json"}

respuesta =requests.post(url, data=json.dumps(dato),headers=cabecera, verify=False)
respuesta_json= respuesta.json()
print(respuesta_json)
Token = respuesta_json["imdata"][0]["aaaLogin"]["attributes"]["token"]
print("API-token: . "+ Token)