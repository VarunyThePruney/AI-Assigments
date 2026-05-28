from neo4j import GraphDatabase


class TravelPlannerDB:

    def __init__(self, uri, username, password):

        self.driver = GraphDatabase.driver(
            uri,
            auth=(username, password)
        )

    def close(self):
        self.driver.close()

    def clear_database(self):

        query = """
        MATCH (n)
        DETACH DELETE n
        """

        with self.driver.session() as session:
            session.run(query)

    def create_tourist(
        self,
        name,
        budget,
        food_preference,
        travel_style
    ):

        query = """
        CREATE (:Tourist {
            name: $name,
            budget: $budget,
            food_preference: $food_preference,
            travel_style: $travel_style
        })
        """

        with self.driver.session() as session:
            session.run(
                query,
                name=name,
                budget=budget,
                food_preference=food_preference,
                travel_style=travel_style
            )

    def create_destination(
        self,
        city,
        attraction,
        average_cost,
        category
    ):

        query = """
        CREATE (:Destination {
            city: $city,
            attraction: $attraction,
            average_cost: $average_cost,
            category: $category
        })
        """

        with self.driver.session() as session:
            session.run(
                query,
                city=city,
                attraction=attraction,
                average_cost=average_cost,
                category=category
            )

    def create_restaurant(
        self,
        name,
        cuisine,
        city,
        average_price
    ):

        query = """
        CREATE (:Restaurant {
            name: $name,
            cuisine: $cuisine,
            city: $city,
            average_price: $average_price
        })
        """

        with self.driver.session() as session:
            session.run(
                query,
                name=name,
                cuisine=cuisine,
                city=city,
                average_price=average_price
            )

    def create_hotel(
        self,
        name,
        city,
        price_per_night,
        rating
    ):

        query = """
        CREATE (:Hotel {
            name: $name,
            city: $city,
            price_per_night: $price_per_night,
            rating: $rating
        })
        """

        with self.driver.session() as session:
            session.run(
                query,
                name=name,
                city=city,
                price_per_night=price_per_night,
                rating=rating
            )

    def recommend_trip(self, tourist_name):

        query = """
        MATCH (t:Tourist {name: $tourist_name})

        MATCH (d:Destination)
        MATCH (r:Restaurant)
        MATCH (h:Hotel)

        WHERE d.average_cost <= t.budget
        AND r.cuisine = t.food_preference
        AND r.city = d.city
        AND h.city = d.city

        RETURN
            d.city AS city,
            d.attraction AS attraction,
            d.average_cost AS trip_cost,
            r.name AS restaurant,
            r.cuisine AS cuisine,
            h.name AS hotel,
            h.price_per_night AS hotel_cost,
            h.rating AS rating

        ORDER BY rating DESC
        """

        with self.driver.session() as session:

            result = session.run(
                query,
                tourist_name=tourist_name
            )

            recommendations = []

            for record in result:

                recommendations.append({
                    "city": record["city"],
                    "attraction": record["attraction"],
                    "trip_cost": record["trip_cost"],
                    "restaurant": record["restaurant"],
                    "cuisine": record["cuisine"],
                    "hotel": record["hotel"],
                    "hotel_cost": record["hotel_cost"],
                    "rating": record["rating"]
                })

            return recommendations