import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Sequence
from sqlalchemy.orm import relationship
from app import db


class Buyer(db.Base):
    __tablename__ = "buyers"

    id = Column(Integer, Sequence("buyer_id_seq"), primary_key=True)
    name = Column(String(150))
    address = Column(String(300))
    vat_number = Column(String(20))

    invoices = relationship("Invoice", back_populates="buyer")

    def __repr__(self):
        return "<Buyer({})>".format(self.name)

    def to_str_row(self):
        lines = [self.name] + self.address.splitlines() + [self.vat_number]
        return "  ".join(lines)

    def to_text(self):
        lines = [self.name] + self.address.splitlines()
        lines.append("NIP: {}".format(self.vat_number))
        return "\n".join(lines)


class Rate(db.Base):
    __tablename__ = "rates"

    id = Column(Integer, Sequence("rate_id_seq"), primary_key=True)
    name = Column(String(20))
    value = Column(Integer)

    items = relationship("Item", back_populates="rate")

    def __repr__(self):
        return "<Rate({})>".format(self.name)


class Item(db.Base):
    __tablename__ = "items"

    id = Column(Integer, Sequence("item_id_seq"), primary_key=True)
    name = Column(String(150))
    unit = Column(String(20), default="szt.")
    quantity = Column(Integer, default=1)
    price = Column(Integer)
    invoice_id = Column(Integer, ForeignKey("invoices.id"))
    rate_id = Column(Integer, ForeignKey("rates.id"))

    invoice = relationship("Invoice", back_populates="items")
    rate = relationship("Rate", back_populates="items")

    def __repr__(self):
        return "<Item({})>".format(self.name)


class Invoice(db.Base):
    __tablename__ = "invoices"

    id = Column(Integer, Sequence("invoice_id_seq"), primary_key=True)
    date = Column(Date, default=datetime.date.today)
    number = Column(Integer)
    buyer_id = Column(Integer, ForeignKey("buyers.id"))

    buyer = relationship("Buyer", back_populates="invoices")
    items = relationship("Item", back_populates="invoice")

    def __repr__(self):
        return "<Invoice({}/{})>".format(self.number, self.date)

    def get_number_str(self):
        return "{}/{}/{}".format(self.number, self.date.month, self.date.year)


db.Base.metadata.create_all(db.engine)

