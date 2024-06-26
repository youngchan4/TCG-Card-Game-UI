from account_register_frame.service.account_register_frame_service_impl import AccountRegisterFrameServiceImpl
from app_window.service.window_service_impl import WindowServiceImpl
from account_login_frame.service.login_menu_frame_service_impl import LoginMenuFrameServiceImpl
from battle_field.frame.battle_field_frame import BattleFieldFrame
from battle_field.infra.battle_field_repository import BattleFieldRepository

from battle_field.infra.legacy.your_hand_repository import LegacyYourHandRepository
from battle_field.infra.legacy.circle_image_legacy_your_deck_repository import CircleImageLegacyYourDeckRepository
from battle_field.infra.round_repository import RoundRepository
from battle_field.infra.your_deck_repository import YourDeckRepository

from battle_field.infra.your_field_energy_repository import YourFieldEnergyRepository
from battle_field.infra.legacy.circle_image_legacy_your_field_unit_repository import CircleImageLegacyYourFieldUnitRepository
from battle_field.infra.legacy.circle_image_legacy_your_hand_repository import CircleImageLegacyYourHandRepository
from battle_field.infra.your_field_unit_repository import YourFieldUnitRepository
from battle_field.infra.your_hand_repository import YourHandRepository
from battle_field.infra.your_tomb_repository import YourTombRepository
from battle_field.service.battle_field_frame_service_impl import BattleFieldFrameServiceImpl
from battle_field_function.service.battle_field_function_service_impl import BattleFieldFunctionServiceImpl
from battle_field_muligun.infra.muligun_your_hand_repository import MuligunYourHandRepository
from battle_field.infra.legacy.circle_image_legacy_your_tomb_repository import CircleImageLegacyYourTombRepository
from battle_field_muligun.service.battle_field_muligun_service_impl import BattleFieldMuligunFrameServiceImpl
from battle_lobby_frame.service.battle_lobby_frame_service_impl import BattleLobbyFrameServiceImpl
from card_shop_frame.service.card_shop_service_impl import CardShopMenuFrameServiceImpl
from card_shop_frame.frame.buy_check_frame.service.buy_check_service_impl import BuyCheckServiceImpl
from decision_first_strike.decision_first_strike_frame_service import DecisionFirstStrikeFrameService
from fake_battle_field.infra.fake_opponent_hand_repository import FakeOpponentHandRepositoryImpl
from fake_battle_field.service.fake_battle_field_frame_service_impl import FakeBattleFieldFrameServiceImpl
from fake_notify_reader.controller.fake_notify_reader_controller_impl import FakeNotifyReaderControllerImpl
from lobby_frame.service.lobby_menu_frame_service_impl import LobbyMenuFrameServiceImpl
from main_frame.service.main_menu_frame_service_impl import MainMenuFrameServiceImpl
from matching_window.service.matching_window_service_impl import MatchingWindowServiceImpl
from opengl_battle_field.frame.battle_field_frame import legacyBattleFieldFrame
from opengl_dummy_frame.service.opengl_dummy_frame_service import OpenGLDummyFrameService
from opengl_my_card_main_frame.service.my_card_main_frame_service_impl import MyCardMainFrameServiceImpl
from opengl_buy_random_card_frame.service.buy_random_card_frame_service_impl import BuyRandomCardFrameServiceImpl
from opengl_my_deck_register_frame.service.my_deck_register_frame_service_impl import MyDeckRegisterFrameServiceImpl
from notify_reader.controller.notify_reader_controller_impl import NotifyReaderControllerImpl
from rock_paper_scissors.service.rock_paper_scissors_service_impl import RockPaperScissorsServiceImpl
from rock_paper_scissors.frame.check_rock_paper_scissors_winner.service.check_rock_paper_scissors_winner_service_impl import CheckRockPaperScissorsWinnerServiceImpl

from session.service.session_service_impl import SessionServiceImpl
from test_detector.detector import DetectorAboutTest
from tests.ljs.ugly_test_result_frame.service.test_result_frame_service import TestResultFrameService

from ui_frame.controller.ui_frame_controller import UiFrameController
from ui_frame.service.ui_frame_service_impl import UiFrameServiceImpl


class UiFrameControllerImpl(UiFrameController):
    __instance = None

    __receiveIpcChannel = None
    __transmitIpcChannel = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__openGLDummyFrameService = OpenGLDummyFrameService.getInstance()

            cls.__instance.__uiFrameService = UiFrameServiceImpl.getInstance()
            cls.__instance.__windowService = WindowServiceImpl.getInstance()

            cls.__instance.__battleFieldFrameService = BattleFieldFrameServiceImpl.getInstance()

            cls.__instance.__fakeBattleFieldFrameServiece = FakeBattleFieldFrameServiceImpl.getInstance()
            cls.__instance.__fakeOpponentHandRepository = FakeOpponentHandRepositoryImpl.getInstance()

            cls.__instance.__roundRepository = RoundRepository.getInstance()

            cls.__instance.__mainMenuFrameService = MainMenuFrameServiceImpl.getInstance()
            cls.__instance.__loginMenuFrameService = LoginMenuFrameServiceImpl.getInstance()
            cls.__instance.__accountRegisterFrameService = AccountRegisterFrameServiceImpl.getInstance()
            cls.__instance.__lobbyMenuFrameService = LobbyMenuFrameServiceImpl.getInstance()
            cls.__instance.__battleLobbyFrameService = BattleLobbyFrameServiceImpl.getInstance()
            cls.__instance.__cardShopMenuFrameService = CardShopMenuFrameServiceImpl.getInstance()
            cls.__instance.__buyCheckService = BuyCheckServiceImpl.getInstance()
            cls.__instance.__myCardMainFrameService = MyCardMainFrameServiceImpl.getInstance()
            cls.__instance.__buyRandomCardFrameService = BuyRandomCardFrameServiceImpl.getInstance()
            cls.__instance.__battleFieldFunctionService = BattleFieldFunctionServiceImpl.getInstance()
            cls.__instance.__myDeckRegisterFrameService = MyDeckRegisterFrameServiceImpl.getInstance()
            cls.__instance.__legacyBattleFieldFrame = legacyBattleFieldFrame
            cls.__instance.__sessionService = SessionServiceImpl.getInstance()
            cls.__instance.__matchingWindowService = MatchingWindowServiceImpl.getInstance()
            cls.__instance.__battleFieldRepository = BattleFieldRepository.getInstance()
            # cls.__instance.__yourDeckRepository = CircleImageLegacyYourDeckRepository.getInstance()
            # cls.__instance.__yourFieldUnitRepository = CircleImageLegacyYourFieldUnitRepository.getInstance()
            cls.__instance.__muligunYourHandRepository = MuligunYourHandRepository.getInstance()
            cls.__instance.__yourTombRepository = YourTombRepository.getInstance()
            cls.__instance.__yourHandRepository = YourHandRepository.getInstance()
            cls.__instance.__legacy_your_hand_repository = LegacyYourHandRepository.getInstance()
            # cls.__instance.__yourTombLegacyRepository = CircleImageLegacyYourTombRepository.getInstance()
            # cls.__instance.__yourHandLegacyRepository = CircleImageLegacyYourHandRepository.getInstance()

            cls.__instance.__yourDeckRepository = YourDeckRepository.getInstance()
            cls.__instance.__yourFieldUnitRepository = YourFieldUnitRepository.getInstance()

            cls.__instance.__yourFieldEnergyRepository = YourFieldEnergyRepository.getInstance()
            cls.__instance.__battleFieldMuligunFrameServiece = BattleFieldMuligunFrameServiceImpl.getInstance()
            cls.__instance.__rockPaperScissorsService = RockPaperScissorsServiceImpl.getInstance()
            cls.__instance.__checkRockPaperScissorsWinnerServiceImpl = CheckRockPaperScissorsWinnerServiceImpl.getInstance()

            cls.__instance.__decisionFirstStrikeFrameService = DecisionFirstStrikeFrameService.getInstance()

            cls.__instance.__battle_result_frame_service = TestResultFrameService.getInstance()

            cls.__instance.__battleFieldFrame = BattleFieldFrame
            cls.__instance.notify_reader_controller = NotifyReaderControllerImpl.getInstance()

            # For Check Fake Battle Field or Real Battle Field
            cls.__instance.detector_about_test = DetectorAboutTest.getInstance()
            cls.__instance.fake_notify_reader_controller = FakeNotifyReaderControllerImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def requestToCreateUiFrame(self):
        print("UiFrameControllerImpl: requestToCreateUiFrame()")

        self.__windowService.createRootWindow()
        rootWindow = self.__windowService.getRootWindow()

        openglDummyFrame = self.__openGLDummyFrameService.createOpenGLDummyFrame(rootWindow, self.switchFrameWithMenuName)
        self.__uiFrameService.registerOpenGLDummyFrame(openglDummyFrame)

        mainMenuFrame = self.__mainMenuFrameService.createMainUiFrame(rootWindow, self.switchFrameWithMenuName)
        self.__uiFrameService.registerMainMenuUiFrame(mainMenuFrame)

        loginMenuFrame = self.__loginMenuFrameService.createLoginUiFrame(rootWindow, self.switchFrameWithMenuName)
        self.__uiFrameService.registerLoginMenuUiFrame(loginMenuFrame)

        accountRegisterFrame = self.__accountRegisterFrameService.createAccountRegisterUiFrame(rootWindow, self.switchFrameWithMenuName)
        self.__uiFrameService.registerAccountRegisterUiFrame(accountRegisterFrame)

        battleLobbyMenuFrame = self.__battleLobbyFrameService.createBattleLobbyUiFrame(rootWindow, self.switchFrameWithMenuName)
        self.__uiFrameService.registerBattleLobbyMenuUiFrame(battleLobbyMenuFrame)

        lobbyMenuFrame = self.__lobbyMenuFrameService.createLobbyUiFrame(rootWindow, self.switchFrameWithMenuName)
        self.__uiFrameService.registerLobbyMenuUiFrame(lobbyMenuFrame)

        myCardMainFrame = self.__myCardMainFrameService.createMyCardMainUiFrame(rootWindow, self.switchFrameWithMenuName)
        self.__uiFrameService.registerMyCardMainUiFrame(myCardMainFrame)

        cardShopMenuFrame = (
            self.__cardShopMenuFrameService.createCardShopUiFrame(rootWindow, self.switchFrameWithMenuName))
        self.__uiFrameService.registerCardShopMenuUiFrame(cardShopMenuFrame)

        buyRandomCardFrame = self.__buyRandomCardFrameService.createBuyRandomCardUiFrame(rootWindow, self.switchFrameWithMenuName)
        self.__uiFrameService.registerBuyRandomCardUiFrame(buyRandomCardFrame)

        # myDeckRegisterFrame = self.__myDeckRegisterFrameService.createMyDeckRegisterUiFrame(rootWindow, self.switchFrameWithMenuName)
        # self.__uiFrameService.registerMyDeckRegisterUiFrame(myDeckRegisterFrame)

        legacyBattleFieldFrame = self.__legacyBattleFieldFrame()
        self.__uiFrameService.legacyRegisterBattleFieldUiFrame(legacyBattleFieldFrame)

        battleFieldMuligunFrame = self.__battleFieldMuligunFrameServiece.createBattleFieldMuligunFrame(rootWindow, self.switchFrameWithMenuName)
        self.__uiFrameService.registerBattleFieldMuligunUiFrame(battleFieldMuligunFrame)

        decisionFirstStrikeFrame = self.__decisionFirstStrikeFrameService.create_decision_first_strike_frame(rootWindow, self.switchFrameWithMenuName)
        self.__uiFrameService.registerDecisionFirstStrikeFrame(decisionFirstStrikeFrame)

        rockPaperScissorsFrame = self.__rockPaperScissorsService.createRockPaperScissorsUiFrame(rootWindow, self.switchFrameWithMenuName)
        self.__uiFrameService.registerRockPaperScissorsUiFrame(rockPaperScissorsFrame)

        checkRockPaperScissorsFrame = self.__checkRockPaperScissorsWinnerServiceImpl.createCheckRockPaperScissorsWinnerUiFrame(rootWindow, self.switchFrameWithMenuName)
        self.__uiFrameService.registerCheckRockPaperScissorsUiFrame(checkRockPaperScissorsFrame)

        # TODO: 매칭 없이 통합 테스트를 진행하기 위한 별도의 가짜 방 (지속적으로 업데이트 해야함)
        fakeBattleFieldFrame = self.__fakeBattleFieldFrameServiece.createFakeBattleFieldFrame(rootWindow, self.switchFrameWithMenuName)
        self.__uiFrameService.registerFakeBattleFieldUiFrame(fakeBattleFieldFrame)

        # test_battle_result_frame = self.__battle_result_frame_service.create_battle_result_frame(rootWindow, self.switchFrameWithMenuName)
        # self.__uiFrameService.register_battle_result_frame(test_battle_result_frame)

        self.__battleFieldFunctionService.saveFrame(self, fakeBattleFieldFrame)

        battleFieldFrame = self.__battleFieldFrame()
        self.__uiFrameService.registerBattleFieldUiFrame(battleFieldFrame)

    def opengl_dummy_frame(self):
        self.switchFrameWithMenuName("dummy")

    def first_main_window(self):
        self.switchFrameWithMenuName("main-menu")

    def switchFrameWithMenuName(self, name):
        print("UiFrameControllerImpl: switchFrameWithMenuName()")
        self.__uiFrameService.switchFrameWithMenuName(name)

    def requestToStartPrintGameUi(self):
        print("UiFrameControllerImpl: requestToStartPrintGameUi()")
        rootWindow = self.__windowService.getRootWindow()

        def get_notify():
            # detector_about_test.set_is_it_test(True)
            if self.detector_about_test.get_is_fake_battle_field() is False:
                self.notify_reader_controller.requestToReadNotifyCommand()
            else:
                self.fake_notify_reader_controller.requestToReadNotifyCommand()

            rootWindow.after(17, get_notify)
        rootWindow.after(0,get_notify)

        rootWindow.mainloop()

    def requestToInjectTransmitIpcChannel(self, transmitIpcChannel):
        print("UiFrameControllerImpl: requestToInjectTransmitIpcChannel()")

        self.__uiFrameService.injectTransmitIpcChannel(transmitIpcChannel)
        self.__accountRegisterFrameService.injectTransmitIpcChannel(transmitIpcChannel)
        self.__loginMenuFrameService.injectTransmitIpcChannel(transmitIpcChannel)
        self.__mainMenuFrameService.injectTransmitIpcChannel(transmitIpcChannel)
        self.__battleLobbyFrameService.injectTransmitIpcChannel(transmitIpcChannel)
        self.__lobbyMenuFrameService.injectTransmitIpcChannel(transmitIpcChannel)
        self.__sessionService.injectTransmitIpcChannel(transmitIpcChannel)

        self.__battleFieldFunctionService.injectTransmitIpcChannel(transmitIpcChannel)

        self.__myDeckRegisterFrameService.injectTransmitIpcChannel(transmitIpcChannel)
        self.__matchingWindowService.injectTransmitIpcChannel(transmitIpcChannel)

        self.__buyCheckService.injectTransmitIpcChannel(transmitIpcChannel)
        self.__battleFieldMuligunFrameServiece.injectReceiveIpcChannel(transmitIpcChannel)
        self.__rockPaperScissorsService.injectTransmitIpcChannel(transmitIpcChannel)
        self.__checkRockPaperScissorsWinnerServiceImpl.injectTransmitIpcChannel(transmitIpcChannel)

        # TODO: Ugly -> Need to Refactor
        self.__battleFieldRepository.saveTransmitIpcChannel(transmitIpcChannel)
        self.__yourDeckRepository.saveTransmitIpcChannel(transmitIpcChannel)
        self.__yourFieldUnitRepository.saveTransmitIpcChannel(transmitIpcChannel)
        self.__muligunYourHandRepository.saveTransmitIpcChannel(transmitIpcChannel)
        # self.__yourTombLegacyRepository.saveTransmitIpcChannel(transmitIpcChannel)
        # self.__yourHandLegacyRepository.saveTransmitIpcChannel(transmitIpcChannel)
        self.__yourTombRepository.saveTransmitIpcChannel(transmitIpcChannel)
        self.__yourHandRepository.saveTransmitIpcChannel(transmitIpcChannel)
        self.__yourFieldEnergyRepository.saveTransmitIpcChannel(transmitIpcChannel)

        self.__fakeBattleFieldFrameServiece.injectTransmitIpcChannel(transmitIpcChannel)
        self.__fakeOpponentHandRepository.injectTransmitIpcChannel(transmitIpcChannel)

        self.__roundRepository.injectTransmitIpcChannel(transmitIpcChannel)

        self.__legacy_your_hand_repository.saveTransmitIpcChannel(transmitIpcChannel)

        self.__buyRandomCardFrameService.saveTransmitIpcChannel(transmitIpcChannel)

        self.__battleFieldFrameService.injectTransmitIpcChannel(transmitIpcChannel)


    def requestToInjectReceiveIpcChannel(self, receiveIpcChannel):
        print("UiFrameControllerImpl: requestToInjectReceiveIpcChannel()")

        self.__uiFrameService.injectReceiveIpcChannel(receiveIpcChannel)
        self.__accountRegisterFrameService.injectReceiveIpcChannel(receiveIpcChannel)
        self.__loginMenuFrameService.injectReceiveIpcChannel(receiveIpcChannel)
        self.__mainMenuFrameService.injectReceiveIpcChannel(receiveIpcChannel)
        self.__battleLobbyFrameService.injectReceiveIpcChannel(receiveIpcChannel)
        self.__lobbyMenuFrameService.injectReceiveIpcChannel(receiveIpcChannel)
        self.__sessionService.injectReceiveIpcChannel(receiveIpcChannel)

        self.__battleFieldFunctionService.injectReceiveIpcChannel(receiveIpcChannel)

        self.__myDeckRegisterFrameService.injectReceiveIpcChannel(receiveIpcChannel)
        self.__matchingWindowService.injectReceiveIpcChannel(receiveIpcChannel)

        self.__buyCheckService.injectReceiveIpcChannel(receiveIpcChannel)
        self.__battleFieldMuligunFrameServiece.injectReceiveIpcChannel(receiveIpcChannel)
        self.__rockPaperScissorsService.injectReceiveIpcChannel(receiveIpcChannel)
        self.__checkRockPaperScissorsWinnerServiceImpl.injectReceiveIpcChannel(receiveIpcChannel)

        # TODO: Ugly -> Need to Refactor
        self.__battleFieldRepository.saveReceiveIpcChannel(receiveIpcChannel)
        self.__yourDeckRepository.saveReceiveIpcChannel(receiveIpcChannel)
        self.__yourFieldUnitRepository.saveReceiveIpcChannel(receiveIpcChannel)
        self.__muligunYourHandRepository.saveReceiveIpcChannel(receiveIpcChannel)
        # self.__yourTombLegacyRepository.saveReceiveIpcChannel(receiveIpcChannel)
        # self.__yourHandLegacyRepository.saveReceiveIpcChannel(receiveIpcChannel)
        self.__yourTombRepository.saveReceiveIpcChannel(receiveIpcChannel)
        self.__yourHandRepository.saveReceiveIpcChannel(receiveIpcChannel)
        self.__yourFieldEnergyRepository.saveReceiveIpcChannel(receiveIpcChannel)

        self.__roundRepository.injectReceiveIpcChannel(receiveIpcChannel)

        self.__fakeBattleFieldFrameServiece.injectReceiveIpcChannel(receiveIpcChannel)
        self.__fakeOpponentHandRepository.injectReceiveIpcChannel(receiveIpcChannel)

        self.__legacy_your_hand_repository.saveReceiveIpcChannel(receiveIpcChannel)

        self.__buyRandomCardFrameService.saveReceiveIpcChannel(receiveIpcChannel)

        self.__battleFieldFrameService.injectReceiveIpcChannel(receiveIpcChannel)

    def requestToInjectMusicPlayIpcChannel(self, musicPlayIpcChannel):
        print("UiFrameControllerImpl: requestToInjectMusicPlayIpcChannel()")

        self.__uiFrameService.injectMusicPlayIpcChannel(musicPlayIpcChannel)

    def requestToInjectNoWaitIpcChannel(self, uiNoWaitIpcChannel):
        print("UiFrameControllerImpl: requestToInjectMusicPlayIpcChannel()")

        self.__battleFieldRepository.injectNoWaitIpcChannel(uiNoWaitIpcChannel)

    def requestToSavePipe(self, conn_from_notify):
        self.__battleFieldFunctionService.savePipe(conn_from_notify)

    # def register_fake_battle_field_frame_which_one_has_socket_communication(self):
    #     rootWindow = self.__windowService.getRootWindow()
    #
    #     fakeBattleFieldFrame = self.__fakeBattleFieldFrameServiece.createFakeBattleFieldFrame(rootWindow, self.switchFrameWithMenuName)
    #     self.__uiFrameService.registerFakeBattleFieldUiFrame(fakeBattleFieldFrame)
