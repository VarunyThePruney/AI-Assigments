class BayesianNetwork:

    def __init__(self):

        self.prob_rain = {
            True: 0.3,
            False: 0.7
        }

        self.prob_traffic_given_rain = {
            (True, True): 0.7,
            (False, True): 0.3,
            (True, False): 0.2,
            (False, False): 0.8
        }

        self.prob_late_given_conditions = {

            (True, True, True): 0.9,
            (False, True, True): 0.1,

            (True, True, False): 0.5,
            (False, True, False): 0.5,

            (True, False, True): 0.6,
            (False, False, True): 0.4,

            (True, False, False): 0.1,
            (False, False, False): 0.9
        }

    def probability_of_traffic(self):

        rain_true = (
            self.prob_rain[True] *
            self.prob_traffic_given_rain[(True, True)]
        )

        rain_false = (
            self.prob_rain[False] *
            self.prob_traffic_given_rain[(True, False)]
        )

        return rain_true + rain_false

    def probability_of_late_given_rain(self):

        traffic_true = (
            self.prob_traffic_given_rain[(True, True)] *
            self.prob_late_given_conditions[
                (True, True, True)
            ]
        )

        traffic_false = (
            self.prob_traffic_given_rain[(False, True)] *
            self.prob_late_given_conditions[
                (True, False, True)
            ]
        )

        return traffic_true + traffic_false

    def probability_of_rain_given_late(self):

        p_late_and_rain = (
            self.prob_rain[True] *
            self.probability_of_late_given_rain()
        )

        p_late = (
            p_late_and_rain +
            (
                self.prob_rain[False] * 0.18
            )
        )

        return p_late_and_rain / p_late


network = BayesianNetwork()

print("\nBayesian Network\n")

print("Rain -> Traffic")
print("Rain -> Late")
print("Traffic -> Late")

traffic_probability = (
    network.probability_of_traffic()
)

print(
    f"\nProbability of Traffic: "
    f"{traffic_probability:.2f}"
)

late_probability = (
    network.probability_of_late_given_rain()
)

print(
    f"Probability of Being Late Given Rain: "
    f"{late_probability:.2f}"
)

rain_given_late = (
    network.probability_of_rain_given_late()
)

print(
    f"Probability of Rain Given Late: "
    f"{rain_given_late:.2f}"
)