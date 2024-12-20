class Egress:
    def __init__(self, id=None, date=None, concept=None, amount=None):
        self._id = id
        self._date = date
        self._concept = concept
        self._amount = amount

    # Getter methods
    @property
    def id(self):
        return self._id

    @property
    def date(self):
        return self._date

    @property
    def concept(self):
        return self._concept

    @property
    def amount(self):
        return self._amount

    # Setter methods
    @id.setter
    def date(self, id):
        self._id = id

    @date.setter
    def date(self, date):
        self._date = date

    @concept.setter
    def date(self, concept):
        self._concept = concept

    @amount.setter
    def date(self, amount):
        self._amount = amount

    def __str__(self):
        return f'''
            Egress:
                ID: {self._id}
                Date: {self._date}
                Concept: {self._concept}
                Amount: {self._amount}
            '''


if __name__ == '__main__':
    egress1 = Egress('1', '2024-10-10', 'Comida Qin', '227.00')
    print(egress1)