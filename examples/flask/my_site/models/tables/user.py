from sqlalchemy import Column, Integer, String

from my_site.models.tables import db


class User(db.Model):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, nullable=False)
    full_name = Column(String)
    email = Column(String)
    patreon_pledge_amount_cents = Column(Integer)
    patreon_user_id = Column(String, index=True)
    patreon_refresh_token = Column(String)
    patreon_access_token = Column(String)
