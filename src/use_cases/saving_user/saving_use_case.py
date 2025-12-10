from src.entities.user import User
from src.use_cases_saving_user.user_repository_interface import UserRepositoryInterface


class SavingUseCase:
    def __init__(self, user_repository: UserRepositoryInterface, notification_service, authorization):
        pass
    
    def execute(self, user: User) -> None:
        pass
