from models.model import Mobile, db
from sqlalchemy.exc import IntegrityError
from models.exceptions import MobileAlreadyExists, MobileBrandUnknown, MobileDoesNotExists, MobileBrandDoesNotExists
from models.Constants import HttpStatus, ResponseMessages, MobileBrands


class MobileHandler():

    def __init__(self):
        return

    @staticmethod
    def create_mobile(brand, mobile_name):
        try:
            new_mobile = Mobile(
                brand=brand.upper(),
                mobile_name=mobile_name
            )
            db.session.add(new_mobile)
            db.session.commit()
            return new_mobile
        except IntegrityError as e:
            raise MobileAlreadyExists()

    @staticmethod
    def get_mobile(mobile_ID):
        mob = Mobile.query.get(mobile_ID)
        if mob:
            response = {
                "brand": mob.brand,
                "mobile_name": mob.mobile_name
            }
            return response
        elif mob is None:
            raise MobileDoesNotExists()
