import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

try:
    connect_str = "DefaultEndpointsProtocol=https;AccountName=haoranzlab2;AccountKey=NIcSq7zA2xcQtfMjtUpRcRpH7cnricsF1hYhtDuA58M7fKODtLtJE1CHDeNLMGVnNZH8rsJJoTnx+AStODBhDw==;EndpointSuffix=core.windows.net"
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)


    container_name = 'lab2container'
    blob_name = 'events_with_forecast.csv'


    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

    with open('events_with_forecast.csv', 'rb') as data:
        blob_client.upload_blob(data, overwrite=True)
    print('Upload Success')

except Exception as ex:
    print('Exception:')
    print(ex)