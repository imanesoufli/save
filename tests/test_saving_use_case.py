from unittest.mock import Mock
import pytest

from src.use_cases.saving_user.saving_use_case import SavingUseCase
from src.use_cases.saving_user.user_repository_interface import UserRepositoryInterface
from src.entities.user import User

@pytest.mark.parametrize("user",[User('imane', 'soufli')])

def test_saving_user_save_in_the_repository(user):
saving_user_case: SavingUseCase = SavingUseCase()

#Act
saving_use_case.execute(user)

#Assert

spy_user_repository.save.assert_called_once_with(user)