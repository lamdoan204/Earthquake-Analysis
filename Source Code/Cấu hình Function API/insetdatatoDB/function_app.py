import logging
import azure.functions as func
import requests
import json

def main(event: func.EventGridEvent):
    # lấy file json vừa được tạo
    result = event.get_json()
    # lấy đường dẫn của json
    blob_url = result.get('url')
    logging.info(f"New blob detected: {blob_url}")

    # Gọi Databricks notebook
    DATABRICKS_TOKEN = "Bearer dapi68dddff08ef60f8d8d6d807f50a4530f-2" #access token
    DATABRICKS_WORKSPACE_URL = "https://adb-103900810483641.1.azuredatabricks.net" # URL databrick
    # đường dẫn notebook /Workspace/Users/doanquanglam281@outlook.com.vn/AutoInsertDataGoldToDB
    NOTEBOOK_PATH = "/Users/doanquanglam281@outlook.com.vn/AutoInsertDataGoldToDB"  
    # thực hiện run notebook với cluster id
    JOB_PAYLOAD = {
        "run_name": "Run from Azure Function",
        "existing_cluster_id": "0526-060153-9ewvfw6s",  # cluster ID Compute trong databrick
        "notebook_task": {
            "notebook_path": NOTEBOOK_PATH,
            "base_parameters": {
                "blob_path": blob_url
            }
        }
    }

    headers = {
        "Authorization": DATABRICKS_TOKEN,#
        "Content-Type": "application/json"
    }

    response = requests.post(
        f"{DATABRICKS_WORKSPACE_URL}/api/2.1/jobs/runs/submit",
        headers=headers,
        json=JOB_PAYLOAD
    )

    if response.status_code == 200:
        logging.info("Databricks job triggered successfully")
    else:
        logging.error(f"Failed to trigger Databricks job: {response.text}")

