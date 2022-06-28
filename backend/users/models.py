from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    phone = PhoneNumberField(blank=True, default='', db_index=True)

    class Meta(AbstractUser.Meta):
        abstract = False

    @classmethod
    def parse_name(cls, name: str) -> dict:
        parts = name.split(' ', 2)

        if len(parts) == 1:
            return {'first_name': parts[0]}

        if len(parts) == 2:
            return {'first_name': parts[0], 'last_name': parts[1]}

        return {'first_name': parts[0], 'last_name': ' '.join(parts[1:])}

    def __str__(self) -> str:
        name = f'{self.first_name} {self.last_name}'

        if len(name) < 3:
            return f'{self.username}'

        return name.strip()
