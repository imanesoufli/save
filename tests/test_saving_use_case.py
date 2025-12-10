def test_saving_user_save_in_the_repository(user):
saving_user_case: SavingUseCase = SavingUseCase()

#Act
saving_use_case.execute(user)

#Assert

spy_user_repository.save.assert_called_once_with(user)