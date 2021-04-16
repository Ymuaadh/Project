from APIAPP.Repository.UserRepository import *


class UserManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create_user(self, model: CreateUserDto):
        """Create USer"""
        raise NotImplementedError

    @abstractmethod
    def list_users(self) -> List[ListUserDto]:
        """List Users"""
        raise NotImplementedError

    @abstractmethod
    def edit_user(self, model: EditUserDto, user_id=None, email=None):
        """Edit Users"""
        raise NotImplementedError

    @abstractmethod
    def user_details(self, user_id=None, email=None) -> UserDetailsDto:
        """User Details"""
        raise NotImplementedError

    @abstractmethod
    def change_password(self, model: ChangePasswordDto, user_id=None, email=None):
        """Change Password"""
        raise NotImplementedError

    @abstractmethod
    def authenticate(self, model: Authenticate):
        """Authenticate"""
        raise NotImplementedError


class DefaultUserManagementService(UserManagementService):
    repository: UserRepository

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, model: CreateUserDto):
        user = self.repository.user_details(email=model.email)
        if user is not UserDetailsDto:
            self.repository.create_user(model)
            return True
        else:
            return False

    def list_users(self) -> List[ListUserDto]:
        return self.repository.list_users()

    def edit_user(self, model: EditUserDto, user_id=None, email=None):
        return self.repository.edit_user(model, user_id, email)

    def user_details(self, user_id=None, email=None) -> UserDetailsDto:
        user = self.repository.user_details(user_id, email)
        if isinstance(user, (UserDetailsDto,)):
            user.__delattr__('password')
            return user

    def change_password(self, model: ChangePasswordDto, user_id=None, email=None):
        return self.repository.change_password(model, user_id, email)

    def authenticate(self, model: Authenticate):
        user = self.repository.user_details(email=model.email)
        if isinstance(user, (UserDetailsDto,)):
            if user.password == model.password:
                user.__delattr__('password')
                return user
