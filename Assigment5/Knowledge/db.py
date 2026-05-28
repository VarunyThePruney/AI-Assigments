from database import TravelPlannerDB


def load_sample_data(db):

    db.clear_database()

    db.create_tourist(
        "Varun",
        8000,
        "Italian",
        "Adventure"
    )

    db.create_destination(
        "Hyderabad",
        "Charminar",
        3000,
        "Historical"
    )

    db.create_destination(
        "Goa",
        "Baga Beach",
        7000,
        "Beach"
    )

    db.create_destination(
        "Manali",
        "Solang Valley",
        6000,
        "Adventure"
    )

    db.create_restaurant(
        "Pizza Palace",
        "Italian",
        "Hyderabad",
        800
    )

    db.create_restaurant(
        "Ocean Bites",
        "Italian",
        "Goa",
        1200
    )

    db.create_restaurant(
        "Mountain Cafe",
        "Italian",
        "Manali",
        1000
    )

    db.create_hotel(
        "Royal Stay",
        "Hyderabad",
        2000,
        4.3
    )

    db.create_hotel(
        "Sea View Resort",
        "Goa",
        3500,
        4.8
    )

    db.create_hotel(
        "Snow Peak Hotel",
        "Manali",
        2500,
        4.6
    )