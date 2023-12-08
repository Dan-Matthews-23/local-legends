from local_legends import db


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(500), nullable=False)
    password_hash = db.Column(db.String(500), nullable=False) 
    is_admin = db.Column(db.Boolean, default=False)
    user_date_registered = db.Column(db.DateTime, nullable=False)   

    def __repr__(self):
        return self.user_id

class Admins(db.Model):
    admin_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    admin_password_hash = db.Column(db.String(500), nullable=False)  
    def __repr__(self):
        return self.admin_id


class Restaurants(db.Model):
    restaurant_id = db.Column(db.Integer, primary_key=True)
    restaurant_name = db.Column(db.String(25), nullable=False)
    restaurant_address_one = db.Column(db.String(25), nullable=False)
    restaurant_address_two = db.Column(db.String(25))
    restaurant_address_three = db.Column(db.String(25))
    restaurant_address_four = db.Column(db.String(25))
    restaurant_address_postcode = db.Column(db.String(25), nullable=False)
    restaurant_average_taste_stars = db.Column(db.Float)
    restaurant_average_presentation_stars = db.Column(db.Float)
    restaurant_average_friendliness_stars = db.Column(db.Float)
    restaurant_average_price_stars = db.Column(db.Float)
    restaurant_average_ambience_stars = db.Column(db.Float)
    restaurant_average_overall_stars = db.Column(db.Float)
    restaurant_image_url = db.Column(db.String(500))
    restaurant_date_registered = db.Column(db.DateTime, nullable=False)
    restaurant_review_count = db.Column(db.Integer)
  

    def __repr__(self):
        return self.restaurant_id

class Reviews(db.Model):
    review_id = db.Column(db.Integer, primary_key=True)
    taste_stars = db.Column(db.Float, nullable=False)
    presentation_stars = db.Column(db.Float, nullable=False)
    friendliness_stars = db.Column(db.Float, nullable=False)
    price_stars = db.Column(db.Float, nullable=False)
    ambience_stars = db.Column(db.Float, nullable=False)
    overall_stars = db.Column(db.Float, nullable=False)
    written_review_title = db.Column(db.String(25), nullable=False)
    written_review = db.Column(db.String(500), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurants.restaurant_id", ondelete="CASCADE"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id", 
    ondelete="CASCADE"), nullable=False)
    review_date = db.Column(db.DateTime, nullable=False)
   

    def __repr__(self):
        return self.review_id