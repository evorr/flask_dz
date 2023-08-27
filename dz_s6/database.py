import databases
import sqlalchemy
import datetime
from settings import settings


database = databases.Database(settings.DATABASE_URL)
metadata = sqlalchemy.MetaData()

items = sqlalchemy.Table("items",
                         metadata,
                         sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column("name", sqlalchemy.String(32)),
                         sqlalchemy.Column("description", sqlalchemy.String(128)),
                         sqlalchemy.Column("price", sqlalchemy.Float), )

users = sqlalchemy.Table("users",
                         metadata,
                         sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column("name", sqlalchemy.String(32)),
                         sqlalchemy.Column("last_name", sqlalchemy.String(32)),
                         sqlalchemy.Column("email", sqlalchemy.String(128)),
                         sqlalchemy.Column("password", sqlalchemy.String(32)), )

orders = sqlalchemy.Table("orders",
                          metadata,
                          sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                          sqlalchemy.Column("user_id", sqlalchemy.ForeignKey("users.id")),
                          sqlalchemy.Column("item_id", sqlalchemy.ForeignKey("items.id")),
                          sqlalchemy.Column("created_on", sqlalchemy.Date(), default=datetime.date.today()),
                          sqlalchemy.Column("status", sqlalchemy.Boolean(), default=False), )


engine = sqlalchemy.create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)
