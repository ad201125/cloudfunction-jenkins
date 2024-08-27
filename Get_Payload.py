import argparse
from google.cloud import storage
import json

def download_blob(bucket_name, source_blob_name, destination_file_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)
    print(f"Downloaded {source_blob_name} from bucket {bucket_name} to {destination_file_name}.")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--gcp_project_name', required=True)
    parser.add_argument('--gcs_folder', required=True)
    parser.add_argument('--payload_name', required=True)
    args = parser.parse_args()

    bucket_name = f"{args.gcp_project_name}-bucket"
    source_blob_name = f"{args.gcs_folder}/{args.payload_name}"
    destination_file_name = args.payload_name

    download_blob(bucket_name, source_blob_name, destination_file_name)

if __name__ == '__main__':
    main()
