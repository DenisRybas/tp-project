from backend_rest.awareness.models import Theme


def get_random_theme_id():
    import time
    import random

    random.seed(time.time())
    num_of_themes = Theme.query.count()
    return random.randint(1, num_of_themes)
