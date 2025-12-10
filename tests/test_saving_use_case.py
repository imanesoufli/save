from unittest.mock import Mock
import pytest

from src.use_cases.saving_user.saving_use_case import SavingUseCase
from src.use_cases.saving_user.user_repository_interface import UserRepositoryInterface
from src.entities.user import User

@pytest.mark.parametrize("user",[User('imane', 'soufli'),
                                 User('ali','ali')])

def test_saving_user_save_in_the_repository(user):
    
    # Arrange
    spy_user_repository = Mock(spec=UserRepositoryInterface)
    spy_user_repository.save = Mock()
    dummy_notification_service = Mock()
    stub_authorization_service = Mock()
    stub_authorization_service.is_authoized = Mock(return_value=True)
    saving_user_case: SavingUseCase = SavingUseCase(spy_user_repository, dummy_notification_service,stub_authorization_service)

    #Act
    SavingUseCase.execute(user)

    #Assert

    spy_user_repository.save.assert_called_once_with(user)