from random import randint

class Insulter():
    _default_insults = (
        'You look pretty dumb',
        'You smell of old cheese',
        'Your face could launch a thousand ships...in the opposite direction',
        'When I think of you, I drink',
    )


    def __init__(self, *insults, include_default_insults=True):
        self.insults = insults

        if include_default_insults:
            self.insults += self._default_insults


    def random_insult(self):
        index = randint(0, len(self.insults)-1)

        return self.insults[index]



class FileBasedInsulter(Insulter):
    def __init__(self, insult_filename):
        with open(insult_filename) as insult_file:
            insults = [insult.strip('\n') for insult in insult_file]

        super().__init__(*insults, include_default_insults=False)


