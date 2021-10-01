import sqlalchemy as sa
import datetime
from first_site.data.modelbase import SqlAlchemyBase


class Package(SqlAlchemyBase):
    __tablename__ = 'packages'

    id = sa.Column(sa.String, primary_key=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True) # if we put datetime.datetime.now(), with parentheses, it will take the current time when the application starts and use that date.  Without parentheses, it brings in the function without calling it.
    summary = sa.Column(sa.String, nullable=False)
    description = sa.Column(sa.String, nullable=True)

    home_page = sa.Column(sa.String)
    docs_url = sa.Column(sa.String)
    package_url = sa.Column(sa.String)

    author_name = sa.Column(sa.String)
    author_email = sa.Column(sa.String, index=True)

    license = sa.Column(sa.String, index=True)

    #maintainers
    #releases




