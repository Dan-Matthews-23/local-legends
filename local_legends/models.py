from local_legends import db

class Users(db.Model):
    """Schema for the Users model."""

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(25), nullable=False)
    

    def __repr__(self):
        return self.username


class Restaurants(db.Model):
    """Schema for the Restaurants model."""
    restaurant_id = db.Column(db.Integer, db.ForeignKey("reviews.review_id", ondelete="CASCADE"), primary_key=True)
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
    

    def __repr__(self):
        return "#{0} - Task: {1} | Urgent: {2}".format(self.restaurant_id, self.restaurant_name, self.restaurant_address_postcode)


class Reviews(db.Model):
    """Schema for the Reviews model."""
    review_id = db.Column(db.Integer, primary_key=True)
    taste_stars = db.Column(db.Integer, nullable=False)
    presentation_stars = db.Column(db.Integer, nullable=False)
    friendliness_stars = db.Column(db.Integer, nullable=False)
    price_stars = db.Column(db.Integer, nullable=False)
    ambience_stars = db.Column(db.Integer, nullable=False)
    overall_stars = db.Column(db.Integer, nullable=False)
    written_review_title = db.Column(db.String(25), nullable=False)
    written_review = db.Column(db.String(25), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurants.restaurant_id", ondelete="CASCADE"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return self.review_id
