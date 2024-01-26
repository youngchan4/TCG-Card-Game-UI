import abc


class CardController(abc.ABC):

    @abc.abstractmethod
    def getCardTypeTable(self, cardType):
        pass

    @abc.abstractmethod
    def itemCardInitShapes(self, local_translation):
        pass

    @abc.abstractmethod
    def trapCardInitShapes(self, local_translation):
        pass

    @abc.abstractmethod
    def suppoitCardInitShapes(self, local_translation):
        pass