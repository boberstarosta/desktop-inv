from sqlalchemy import or_
from app import db
from app.models import Buyer


def search_buyers(search_string):
    keywords = search_string.split()
    conditions = [
        or_(Buyer.name.like("%" + kw + "%"),
            Buyer.address.like("%" + kw + "%"),
            Buyer.vat_number.like("%" + kw + "%"))
        for kw in keywords
    ]
    return db.session.query(Buyer).filter(or_(*conditions)).all()

