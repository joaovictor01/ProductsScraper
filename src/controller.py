import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from loguru import logger

# Load environment variables from .env file
load_dotenv()

# Get MongoDB credentials from environment variables
mongo_user = os.getenv("MONGO_INITDB_ROOT_USERNAME")
mongo_password = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
mongo_host = "localhost"
mongo_port = 27017

# Connection string with credentials
# connection_string = f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/?authSource=admin"
connection_string = f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}"
# Establishing a connection
client = AsyncIOMotorClient(connection_string)
try:
    conn = client.server_info()
    print(f'Connected to MongoDB {conn.get("version")}')
except Exception:
    print("Unable to connect to the MongoDB server.")

# Access the database
db = client.prova_tecnologias_emergentes


def insert_list_of_dicts_into_db(list_of_dicts: list[dict]):
    try:
        db.products.insert_many(list_of_dicts)
    except Exception as e:
        logger.warning(f"Error inserting data in bulk into MongoDB. {e}")


def get_product(product_id: str) -> dict:
    return db.products.find_one({"product_id": product_id})


def delete_product(product_id: str):
    db.products.delete_one({"product_id": product_id})


def delete_all_products():
    db.products.delete_many({})


# Close the connection
client.close()
