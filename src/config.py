import pymongo
import os
from dotenv import load_dotenv


load_dotenv()  # Load environment variables from .env file


class EnvironmentVariable:
    access_key = os.getenv("MONGODB_ACCESS_KEY")


env_var = EnvironmentVariable()
mongo_client = pymongo.MongoClient(f"mongodb+srv://master:master123@atlascluster.w0iwrbk.mongodb.net/?retryWrites=true&w=majority")
TARGET_COLUMN = "default.payment.next.month"
