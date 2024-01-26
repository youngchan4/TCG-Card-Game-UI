from battle_field_function.controller.battle_field_function_controller import BattleFieldFunctionController
from battle_field_function.service.battle_field_function_service_impl import BattleFieldFunctionServiceImpl


class BattleFieldFunctionControllerImpl(BattleFieldFunctionController):
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__battleFieldFunctionService = BattleFieldFunctionServiceImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def callSurrender(self):
        self.__battleFieldFunctionService.surrender()