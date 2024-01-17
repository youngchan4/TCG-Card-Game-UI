import abc


class UiFrameService(abc.ABC):
    @abc.abstractmethod
    def switchFrameWithMenuName(self, menuName: str):
        pass

    @abc.abstractmethod
    def registerMainMenuUiFrame(self, mainMenuFrame):
        pass

    @abc.abstractmethod
    def registerLoginMenuUiFrame(self, loginMenuFrame):
        pass

    @abc.abstractmethod
    def registerAccountRegisterUiFrame(self, accountRegisterFrame):
        pass

    @abc.abstractmethod
    def registerLobbyMenuUiFrame(self, lobbyMenuFrame):
        pass

    @abc.abstractmethod
    def registerBattleLobbyMenuUiFrame(self, battleLobbyMenuFrame):
        pass

    @abc.abstractmethod
    def registerMyCardUiFrame(self, myCardFrame):
        pass

    @abc.abstractmethod
    def registerMyDeckUiFrame(self, myDeckFrame):
        pass

    @abc.abstractmethod
    def registerCardShopMenuUiFrame(self, cardShopMenuFrame):
        pass

    @abc.abstractmethod
    def injectTransmitIpcChannel(self, transmitIpcChannel):
        pass

    @abc.abstractmethod
    def injectReceiveIpcChannel(self, receiveIpcChannel):
        pass
