from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class EANValidator:
    message = _('Enter a valid EAN address.')
    code = 'invalid'

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        value_digits = value.replace('-', '')

        if not self.validate_checksum(value_digits):
            raise ValidationError(self.message, code=self.code)

    def validate_checksum(self, value):
        # Todo implement
        return True

    def __eq__(self, other):
        return (
                isinstance(other, EANValidator) and
                (self.message == other.message) and
                (self.code == other.code)
        )
