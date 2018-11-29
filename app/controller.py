import datetime
from sqlalchemy import or_
from app import db
from app.models import Buyer, Invoice


def search_buyers(search_string):
    keywords = search_string.split()
    conditions = [
        or_(Buyer.name.like("%" + kw + "%"),
            Buyer.address.like("%" + kw + "%"),
            Buyer.vat_number.like("%" + kw + "%"))
        for kw in keywords
    ]
    return db.session.query(Buyer).filter(or_(*conditions)).all()


def generate_invoice_number():
    today = datetime.date.today()
    last_invoice = db.session.query(Invoice).order_by(
        Invoice.date.desc()).first()
    if last_invoice is not None:
        last = last_invoice.date
        if last.year == today.year and last.month == today.month:
            return last_invoice.number + 1
    return 1

