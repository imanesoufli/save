from src.entities.user import User
from src.use_cases_saving_user.user_repository_interface import UserRepositoryInterface


class SavingUseCase:
    def __init__(self, user_repository: UserRepositoryInterface, notification_service, authorization_service):
        self.user_repoository: UserRepositoryInterface = user_repository
        self.authorization_service = authorization_service
    
    def execute(self, user: User) -> None:
        if self.authorization_service.is_authorized():
            self.user_repoository.save(user)
