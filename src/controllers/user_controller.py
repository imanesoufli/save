class UserController:
    def __init__(self, saving_user_use_case, presenter):
        self.saving_user_use_case = saving_user_use_case
        self.presenter = presenter

    def save_user(self, user_data):
        response = self.saving_user_use_case.execute(user_data)
        return self.presenter.present(response)
