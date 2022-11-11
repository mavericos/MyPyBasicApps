#https://www.youtube.com/watch?v=p15xzjzR9j0&list=PLnbmk43t7uQM5BQT_C2rXqUKanK0dwOkV&index=6

class Cat:
    TOTAL_CATS = 0

    def __init__(self, name):
        self.name = name

        @staticmethod
        def add_cat():
            Cat.TOTAL_CATS += 1
