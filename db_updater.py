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
        active=ad["active"],
    )
    return new_ad


def copy_fields_values(model_to, model_from):
    for full_column_name in model_from.__table__.columns:
        short_column_name = str(full_column_name).split(".")[1]
        setattr(model_to, short_column_name,
                getattr(model_from, short_column_name))


def update_database_from_json(json_filename):
    with open(json_filename, "r") as file:
        ads = json.load(file)

    with app.app_context():
        for ad in ads:
            tmp_ad = dict2model(ad)
            old_ad = RealtyAd.query.filter_by(id=tmp_ad.id).first()
            if old_ad is None:
                db.session.add(tmp_ad)
            else:
                copy_fields_values(old_ad, tmp_ad)
        db.session.commit()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        update_database_from_json(filename)
    else:
        print("Usage: python3 {} some_file.json".format(__file__))
