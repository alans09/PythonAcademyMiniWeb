from zoo import db


class Zoo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    opening_hours = db.Column(db.String)
    description = db.Column(db.String)

    pavilions = db.relationship('Pavilions', backref='zoo', lazy=True)
    shops = db.relationship('Shops', backref='zoo', lazy=True)

    def __init__(self, name, opening_hours, description):
        self.name = name
        self.opening_hours = opening_hours
        self.description = description


class Pavilions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    description = db.Column(db.String)
    zoo_id = db.Column(db.Integer, db.ForeignKey('zoo.id'), nullable=False)

    animals = db.relationship('Animals', backref='pavilions', lazy=True)

    def __init__(self, name, description, zoo_id):
        self.name = name
        self.description = description
        self.zoo_id = zoo_id


class Shops(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    description = db.Column(db.String)
    goods = db.Column(db.String)
    zoo_id = db.Column(db.Integer, db.ForeignKey('zoo.id'), nullable=False)

    def __init__(self, name, description, goods, zoo_id):
        self.name = name
        self.description = description
        self.goods = goods
        self.zoo_id = zoo_id


class Animals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    description = db.Column(db.String)
    type = db.Column(db.String)
    sex = db.Column(db.String)
    age = db.Column(db.Integer)
    pavilions_id = db.Column(db.Integer, db.ForeignKey('pavilions.id'), nullable=False)

    def __init__(self, name, description, type_, sex, age, pavilions_id):
        self.name = name
        self.description = description
        self.type = type_
        self.sex = sex
        self.age = age
        self.pavilions_id = pavilions_id


def init_database():
    # vytvorime databazovy model (/database/database.db) subor
    db.create_all()
    # vytvorime zoo
    zoo = Zoo("Tomasova Zoo", "10:00 - 15:00", "Tomasova prva databazova zoo")
    # vytvorime si pavilony
    water = Pavilions("Water pavilion", "prvy vodny pavilon", 1)
    water2 = Pavilions("Water pavilion exotic", "druhy vodny pavilon", 1)
    sand = Pavilions("Sand pavilion", "Piesocny saharsky pavilon", 1)
    # vytvorime si zvierata
    meerkat1 = Animals("Karolinka", "Hneda surikata", "meerkat meerkat", "F", 2, 3)
    meerkat2 = Animals("Karol", "Hneda surikata", "meerkat meerkat", "M", 2, 3)
    octopus = Animals("Nadezda", "Farebna chobotnica", "Giant Octopus", "F", 5, 2)
    octopus2 = Animals("Nastasia", "Farebna chobotnica", "Giant Octopus", "F", 5, 1)
    # vytvorime si obchod
    shop1 = Shops("Water Shop", "Octopus goods", "1. Octopus 4.00", 1)
    # pridame si vsetko co chceme upravit do  "SESSION"
    db.session.add(zoo)
    db.session.add(water)
    db.session.add(water2)
    db.session.add(sand)
    db.session.add(meerkat1)
    db.session.add(meerkat2)
    db.session.add(octopus)
    db.session.add(octopus2)
    db.session.add(shop1)

    db.session.commit()


if __name__ == "__main__":
    init_database()
