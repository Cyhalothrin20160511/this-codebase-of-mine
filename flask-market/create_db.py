from market import app, db
from market.models import User, Item

with app.app_context():
    db.drop_all()
    db.create_all()

    u1 = User(username='jsc', password_hash = '123456', email_address='jsc@jsc.com')
    item1 = Item(name="IPhone 10", price=500, barcode='846154104831', description='desc')
    item2 = Item(name="Laptop", price=600, description='description',barcode='321912987542')
    db.session.add(u1)
    item1.owner = User.query.filter_by(username='jsc').first().id
    db.session.add(item1)
    db.session.add(item2)
    db.session.commit()
