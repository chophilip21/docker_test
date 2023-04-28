from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os


def set_env_from_file(file):
    """Read env file and set env variables"""

    with open(file, "r") as f:
        for line in f:
            if len(line) > 0:
                key, value = line.split("=")
                os.environ[key] = value.strip()


if __name__ == "__main__":
    env_path = "../.env"
    assert os.path.exists(env_path), "env file exists"
    set_env_from_file(env_path)
    assert "MONGO_PWD" in os.environ, "MONGO_PWD is set"

    # get env variable from env file
    pwd = os.environ.get("MONGO_PWD")

    uri = f"mongodb+srv://philip:{pwd}@cluster0.yudzwet.mongodb.net/?retryWrites=true&w=majority"
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi("1"))
    # Send a ping to confirm a successful connection
    try:
        client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    # print(client.list_database_names())
    db = client["local"]
    print(db.list_collection_names())

    # mydb = client["mydatabase"]
    # col_test = mydb["test"]
    # print(mydb.list_collection_names())
