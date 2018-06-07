from models import db, RealtyAd
import json
import sys

from server import app


def dict2model(ad):
    new_ad = RealtyAd(
        id=ad["id"],
        settlement=ad["settlement"],
        under_construction=ad["under_construction"],
        description=ad["description"],
        price=ad["price"],
        oblast_district=ad["oblast_district"],
        living_area=ad["living_area"],
        has_balcony=ad["has_balcony"],
        address=ad["address"],
        construction_year=ad["construction_year"],
        rooms_number=ad["rooms_number"],
        premise_area=ad["premise_area"],
        active=ad["active"]
    )
    return new_ad


def update_database_from_json(json_filename):
    with open(json_filename, "r") as file:
        ads = json.load(file)

    with app.app_context():
        RealtyAd.query.delete()
        for ad in ads:
            new_ad = dict2model(ad)
            db.session.add(new_ad)
        db.session.commit()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        update_database_from_json(filename)
    else:
        print("Usage: python3 {} some_file.json".format(__file__))
