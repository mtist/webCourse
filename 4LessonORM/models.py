from peewee import *
from pip._vendor.distlib import database

db = SqliteDatabase("people.db")


class Person(Model):
    name = CharField(max_length=50)
    year = SmallIntegerField()
    male = BooleanField()

    class Meta:
        database = db


def create_tables():
    with db:
        db.create_tables([Person])