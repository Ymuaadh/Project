import datetime

class CreateUserDto:
    first_name: str
    last_name: str
    phone_number: int
    email: str
    password: str
    confirm_password: str


class ListUserDto:
    name: str
    phone_number: int
    email: str

class EditUserDto:
    id: int
    first_name: str
    last_name: str
    phone_number: int
    email: str

class UserDetailsDto:
    id: int
    first_name: str
    last_name: str
    phone_number: int
    password: str
    email: str
    active: bool
    last_login: datetime


class Authenticate:
    email: str
    password: str


class ChangePasswordDto:
    id: int
    email: str
    old_password: str
    new_password: str




