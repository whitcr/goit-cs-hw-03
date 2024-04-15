import argparse

from pymongo import MongoClient

client = MongoClient("mongodb+srv://whitcr0k:1111@cluster0.j0mzdk0.mongodb.net/")
db = client.cats
collection = db.cats

parser = argparse.ArgumentParser(description="Add new cat")

parser.add_argument("--action", help="[create, read, update, delete]")
parser.add_argument("--id", help="id of the cat")
parser.add_argument("--name", help="name of the cat")
parser.add_argument("--age", help="Age of the cat")
parser.add_argument("--features", help="features of the cat", nargs="+")

args = vars(parser.parse_args())

action = args["action"]
pk = args["id"]
name = args["name"]
age = args["age"]
features = args["features"]


def read_all():
    cats = collection.find({})
    return cats


def read_by_name(name):
    cat = collection.find_one({"name": name})
    return cat


def create(name, age, features):
    return collection.insert_one({"name": name, "age": age, "features": features})


def update_age(name, age):
    return collection.update_one(
        {"name": name},
        {"$set": {"age": age}},
    )


def update_features(name, features):
    return collection.update_one(
        {"name": name},
        {"$set": {"features": features}},
    )


def delete_one(name):
    return collection.delete_one({"name": name})


def delete():
    return collection.delete_many({})


if __name__ == "__main__":
    match action:
        case "create":
            r = create(name, age, features)
            print(r.inserted_id)
        case "read_all":
            [print(cat) for cat in read_all()]
        case "read_by_name":
            r = read_by_name(name)
            print(r)
        case "update_age":
            r = update_age(name, age)
            print(r.modified_count)
        case "update_features":
            r = update_features(name, features)
            print(r.modified_count)
        case "delete":
            r = delete()
            print(r.modified_count)
        case "delete_one":
            r = delete_one(name)
            print(r.modified_count)
        case _:
            print("Invalid action")
