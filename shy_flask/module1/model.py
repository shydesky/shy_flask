from extensions import db
from database import SurrogatePK, Column


class Account(SurrogatePK, db.Model):
    __tablename__ = 'account'

    advertiser_id = Column(db.Integer, db.ForeignKey('advertiser.id'))
    status = Column(db.SmallInteger, default=1)


class Advertiser(SurrogatePK, db.Model):
    __tablename__ = 'advertiser'

    name = Column(db.String(255), index=True)
