from dependency_injector import containers, providers
from typing import Callable
from APIAPP.Repository.UserRepository import DjangoORMUserRepository, UserRepository
from APIAPP.Services.UserManagementservice import UserManagementService, DefaultUserManagementService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()


    user_repository : Callable[[],UserRepository] = providers.Factory(
        DjangoORMUserRepository
    )
    user_management_service: Callable[[], UserManagementService] = providers.Factory(
        DefaultUserManagementService,
        repository=user_repository
    )


api_service_provider = Container()