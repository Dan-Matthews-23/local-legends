from local_legends import db

class Users(db.Model):
    # schema for the Category model
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(25), nullable=False)
    reviews = db.relationship("Reviews", backref="users", cascade="all, delete", lazy=True)
    restaurants = db.relationship("Restaurants", backref="users", cascade="all, delete", lazy=True)
    def __repr__(self):
        return self.username

class Restaurants(db.Model):
    # schema for the Category model
    restaurant_id = db.Column(db.Integer, primary_key=True)
    restaurant_name = db.Column(db.String(25), nullable=False)
    restaurant_address_one = db.Column(db.String(25), nullable=False)
    restaurant_address_two = db.Column(db.String(25), nullable=False)
    restaurant_address_three = db.Column(db.String(25), nullable=False)
    restaurant_address_four = db.Column(db.String(25), nullable=False)
    restaurant_address_postcode = db.Column(db.String(25), nullable=False)
    restaurant_average_taste_stars = db.Column(db.String(25), nullable=False)
    restaurant_average_presentation_stars = db.Column(db.String(25), nullable=False)
    restaurant_average_friendliness_stars = db.Column(db.String(25), nullable=False)
    restaurant_average_price_stars = db.Column(db.String(25), nullable=False)
    restaurant_average_ambience_stars = db.Column(db.String(25), nullable=False)
    restaurant_average_overall_stars = db.Column(db.String(25), nullable=False)
    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Task: {1} | Urgent: {2}".format(self.restaurant_id, self.restaurant_name, self.restaurant_address_postcode)

        

class Reviews(db.Model):
    # schema for the Category model
    review_id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey(
        "restaurants.restaurant_id", ondelete="CASCADE"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(
        "users.user_id", ondelete="CASCADE"), nullable=False)
    taste_stars =  db.Column(db.Integer, nullable=False)
    presentation_stars = db.Column(db.Integer, nullable=False) 
    friendliness_stars = db.Column(db.Integer, nullable=False)
    price_stars = db.Column(db.Integer, nullable=False)
    ambience_stars = db.Column(db.Integer, nullable=False)
    overall_stars = db.Column(db.Integer, nullable=False)
    written_review_title = db.Column(db.String(25), nullable=False)
    written_review = db.Column(db.String(25), nullable=False)
    def __repr__(self):
        return self.review_id