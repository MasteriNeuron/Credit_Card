import pymongo
import pandas as pd
import json
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

access_key = os.getenv("MONGODB_ACCESS_KEY")
client = pymongo.MongoClient("mongodb+srv://master:master123@atlascluster.w0iwrbk.mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH = r"C:\Users\pc\Desktop\credit\data\card.csv"
DATABASE_NAME = "CreditDefaults"
COLLECTION_NAME = "CreditData"

if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    # Converting DataFrame to JSON format (for dumping records in JSON)
    df.reset_index(drop=True, inplace=True)
    json_records = json.loads(df.to_json(orient="records"))
    print(json_records[0])

    # Connect to MongoDB and insert the JSON records
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]
    collection.insert_many(json_records)
