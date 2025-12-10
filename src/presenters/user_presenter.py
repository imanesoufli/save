class UserPresenter:
    def present(self, response_dto):
        return {
            "success": response_dto.success,
            "message": response_dto.message,
            "data": response_dto.data
        }
