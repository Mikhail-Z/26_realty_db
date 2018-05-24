from sqlalchemy import or_
from flask import url_for
from models import RealtyAd
from sys import maxsize
from datetime import datetime


def ad_model2dict(ad):
    return {
        "settlement": ad.settlement,
        "under_construction": ad.under_construction,
        "description": ad.description,
        "price": ad.price,
        "oblast_district": ad.oblast_district,
        "living_area": ad.living_area,
        "has_balcony": ad.has_balcony,
        "address": ad.address,
        "construction_year": ad.construction_year,
        "rooms_number": ad.rooms_number,
        "premise_area": ad.premise_area,
    }


def get_page_navigation_info(ads_pagination):
    next_page_num = ads_pagination.next_num
    prev_page_num = ads_pagination.prev_num
    next_url = url_for("ads_list", page=next_page_num) if ads_pagination.has_next else None
    prev_url = url_for("ads_list", page=prev_page_num) if ads_pagination.has_prev else None
    cur_page = ads_pagination.page
    pages_num = ads_pagination.pages
    return {
        "next_url": next_url,
        "prev_url": prev_url,
        "cur_page": cur_page,
        "pages_num": pages_num
    }


def filter_ads(request):
    oblast_district = request.args.get("oblast_district", "")
    min_price = request.args.get("min_price", 0, int)
    max_price = request.args.get("max_price", maxsize, int)
    new_building = request.args.get("new_building", None)
    years_when_building_is_new = 2
    ads_query_set = RealtyAd.query.filter(
        or_(RealtyAd.oblast_district == oblast_district, oblast_district == ""),
        RealtyAd.price >= min_price, RealtyAd.price <= max_price,
        or_(
            RealtyAd.under_construction == 1,
            datetime.now().year - RealtyAd.construction_year <= years_when_building_is_new,
            new_building is None
        ),
        RealtyAd.active == 1
    )
    return ads_query_set
