from mongoengine import *

connect(
    db='testdb',
    username='admin',
    password='1234',
    # host='mongodb://admin:qwerty@localhost/production'
)


class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
