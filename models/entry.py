class Entry():
    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, entry_date, concept, body, mood_id):
        self.id = id
        self.entry_date = entry_date
        self.concept = concept
        self.body = body
        self.mood_id = mood_id
        self.mood = None
