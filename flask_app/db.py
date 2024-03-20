import pymongo
import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv()

my_user = os.getenv("mongo_user")
my_pass = os.getenv("mongo_pass")
esc_my_pass = quote_plus(my_pass)

# url = "mongodb://localhost:27017"
url = f"mongodb+srv://{my_user}:{esc_my_pass}@cluster0.uf2yh8k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = pymongo.MongoClient(url)

db = client["api-test-v2"]
