from flask import Flask
from flask import request, render_template
from models import db
from help_functions import ad_model2dict, get_page_navigation_info, filter_ads


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
    return render_template(
        'ads_list.html',
        ads=[ad_model2dict(ad) for ad in ads],
        next_url=navigation_info["next_url"],
        prev_url=navigation_info["prev_url"],
        cur_page=navigation_info["cur_page"],
        pages_num=navigation_info["pages_num"]
    )


if __name__ == "__main__":
    app.run()
