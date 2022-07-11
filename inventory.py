import requests
import json

# Submit a http request to website inventory and get a response
response = requests.get("https://wss2.cex.uk.webuy.io/v3/boxes/SCPUINTI32100/neareststores?latitude=53.10040499999999&longitude=-2.4438209")

# Convert Response object to string
response_string = json.dumps(response.json())

# Convert string to dictionary
response_dict = json.loads(response_string)

# Access stores and inventory data in response dict
nearest_stores = response_dict["response"]["data"]["nearestStores"]

# Print header
print("Store          Quantity")

# Iterate through stores and print
for store in nearest_stores:
    store_name = store["storeName"]
    store_quantity = store["quantityOnHand"]

    print("{0:15} {1}".format(store_name, store_quantity))





