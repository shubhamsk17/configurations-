import requests
import json

def update_gateway_config(gateway_id, user_id, password, success_dict):
    url = f"https://loratest.eleven-x.com:1795/omc/newLoraConfInd/{gateway_id}"

    # Sample configuration data
    config_data = {
   "SX1301s_conf":[
      {
         "radio":[
            {
               "enable":True,
               "freq":912900000
            },
            {
               "enable":True,
               "freq":912300000
            }
         ],
         "chan_multiSF":[
            {
               "enable":True,
               "radio":0,
               "bandwidth":125000,
               "offset":400000,
               "maxtxp":27,
               "minsf":"SF7",
               "maxsf":"SF10"
            },
            {
               "enable":True,
               "radio":0,
               "bandwidth":125000,
               "offset":200000,
               "maxtxp":27,
               "minsf":"SF7",
               "maxsf":"SF10"
            },
            {
               "enable":True,
               "radio":0,
               "bandwidth":125000,
               "offset":0,
               "maxtxp":27,
               "minsf":"SF7",
               "maxsf":"SF10"
            },
            {
               "enable":True,
               "radio":1,
               "bandwidth":125000,
               "offset":-400000,
               "maxtxp":27,
               "minsf":"SF7",
               "maxsf":"SF10"
            },
            {
               "enable":True,
               "radio":1,
               "bandwidth":125000,
               "offset":0,
               "maxtxp":27,
               "minsf":"SF7",
               "maxsf":"SF10"
            },
            {
               "enable":True,
               "radio":1,
               "bandwidth":125000,
               "offset":-200000,
               "maxtxp":27,
               "minsf":"SF7",
               "maxsf":"SF10"
            },
            {
               "enable":True,
               "radio":0,
               "bandwidth":125000,
               "offset":-400000,
               "maxtxp":27,
               "minsf":"SF7",
               "maxsf":"SF10"
            },
            {
               "enable":True,
               "radio":1,
               "bandwidth":125000,
               "offset":400000,
               "maxtxp":27,
               "minsf":"SF7",
               "maxsf":"SF10"
            }
         ],
         "chan_Lora_std":{
            "enable":True,
            "radio":0,
            "bandwidth":500000,
            "offset":-300000,
            "maxtxp":27,
            "minsf":"SF8",
            "maxsf":"SF8"
         },
         "chan_FSK":{
            "enable":False,
            "radio":-1,
            "offset":0,
            "bandwidth":125000,
            "datarate":0,
            "maxtxp":27
         }
      }
   ],
   "enable_beacon":False,
   "maxDownlinkPowerFreqBands":[
      {
         "lowFreq":902000000,
         "highFreq":928000000,
         "rx1MaxTxPower":27,
         "rx2MaxTxPower":27,
         "classBdownlinkMaxTxPower":27,
         "authorizedAntennaIdx":[
            0
         ]
      }
   ],
   "antennaParameters":[
      {
         "cableLoss":0,
         "antennaGain":0
      }
   ]
}

    # Perform the PUT request with authorization
    response = requests.put(url, json=config_data, auth=(user_id, password))

    # Check the response status
    if response.status_code == 200:
        print(f"Gateway ID {gateway_id} configuration updated successfully.")
        success_dict[gateway_id] = True
    else:
        print(f"Failed to update configuration for Gateway ID {gateway_id}.")
        print(f"Response: {response.text}")
        success_dict[gateway_id] = False

# Provide your user ID and password
user_id = "orbiwise"
password = "53eN5BODc4OZF4SDkvpsw" #eleven -x testbed password

#password = "hOKb8heZ9yKE0eG" rocky-linux password

# Provide a list of gateway IDs
gateway_ids = [
    "000800fffe4a4a14",
    "001616fffe2ba9b6",
    "7076fffffe02008f",
    "58a0cbfffe012fe4",
    "gateway_id5",
    # Add more gateway IDs as needed
]

# Dictionary to track success status for each gateway
success_status = {}

# Update configurations for each gateway
for gateway_id in gateway_ids:
    update_gateway_config(gateway_id, user_id, password, success_status)

# Print the success status for each gateway
for gateway_id, success in success_status.items():
    if success:
        print(f"Configuration updated successfully for Gateway ID: {gateway_id}")
    else:
        print(f"Failed to update configuration for Gateway ID: {gateway_id}")
 