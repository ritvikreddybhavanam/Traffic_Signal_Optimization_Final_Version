class ProbabilityTables:

    # Prior probabilities

    P_RUSH_HOUR = {
        True: 0.7,
        False: 0.3
    }

    P_RAIN = {
        True: 0.4,
        False: 0.6
    }

    P_ACCIDENT = {
        True: 0.2,
        False: 0.8
    }

    # P(Congestion | RushHour, Rain, Accident)

    CONGESTION_TABLE = {

        (True, True, True): 0.99,
        (True, True, False): 0.90,

        (True, False, True): 0.85,
        (True, False, False): 0.75,

        (False, True, True): 0.80,
        (False, True, False): 0.60,

        (False, False, True): 0.50,
        (False, False, False): 0.20
    }