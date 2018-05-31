from flask import Flask
from flask import request
from models import db
from help_functions import (ad_model2dict, get_page_navigation_info, filter_ads,
                            generate_json_with_ads, generate_page_with_ads)
from flask import url_for



def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    db.init_app(app)

    with app.app_context():
        db.create_all()
    return app


app = create_app()


@app.route('/')
def ads_list():
    page = request.args.get("page", 1, type=int)

    ads_per_page = 15

    ads_query_set = filter_ads(request)
    ads_pagination = ads_query_set.paginate(page, ads_per_page, False)
    ads = ads_pagination.items
    navigation_info = get_page_navigation_info(ads_pagination)
    if request.is_xhr:
        return generate_json_with_ads(ads, navigation_info)
    else:
        return generate_page_with_ads(ads, navigation_info)


if __name__ == "__main__":
    app.run()
