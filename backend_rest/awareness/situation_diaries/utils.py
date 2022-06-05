from backend_rest.awareness.models import Situation


def get_random_situation_id():
    import time
    import random

    random.seed(time.time())
    num_of_situations = Situation.query.count()
    return random.randint(1, num_of_situations)
