import os
from azure.storage.blob import (BlockBlobService, 
                                BlobClient, 
                                ContentSettings)

# STORAGE CONNECTION VARIABLES
STORAGE_CONNECTION_STRING = os.getenv('STORAGE_CONNECTION_STRING')

def create_container_in_storage(container_name):
    """
    Creates a container in the Azure Blob Storage
    """
    block_blob_service = BlockBlobService(connection_string=STORAGE_CONNECTION_STRING)
    block_blob_service.create_container(container_name)

def move_image_to_storage(file_path, file_name, container):
    """
    Moves a file to the Azure Blob Storage
    """
    block_blob_service = BlockBlobService(connection_string=STORAGE_CONNECTION_STRING)
    block_blob_service.create_blob_from_path(
        container,
        file_name,
        file_path,
        content_settings=ContentSettings(content_type='image/jpeg')
    )
    
def get_image_url(file_name, container):
    """
    Returns the URL of the image
    """
    blob_client = BlobClient.from_connection_string(
        conn_str=STORAGE_CONNECTION_STRING,
        blob_name=container + '/' + file_name
    )
    return blob_client.url

def remove_file_from_storage(file_name, container):
    """
    Removes a file from the Azure Blob Storage
    """
    block_blob_service = BlockBlobService(connection_string=STORAGE_CONNECTION_STRING)
    block_blob_service.delete_blob(container, file_name)