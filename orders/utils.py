import string
import secrets

from django.db import IntegrityError
from django.db import transaction
from .models import Coupon 

def generate_coupon_code(length=10):
    """

    Generate a unique alphanumeric coupon code of given length.
    this tries repeatedly until a unique code is found (i.e. not already presentin the DB).
    """

    if not isinstance(length, int) or length <=0:
        raise ValueError("Length must be a positive integer")

    valid_chars = string.ascii_uppercase + string.digits

    while True:
        code = ''.join(secrets.choice(valid_chars) for _ in range(length))

        with transaction.atomic():
            if not Coupon.objects.filter(code=code).exists():
                return code