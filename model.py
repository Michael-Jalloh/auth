from peewee import *

db = SqliteDatabase('auth.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField(default="")
    first_name = CharField(default="")
    last_name = CharField(default="")
    password = CharField()
    email = CharField()
    pub_key = CharField(default="")
    priv_key = CharField(default="")



db.create_table([User], safe=True)
