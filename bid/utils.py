import phonenumbers
from phonenumbers import NumberParseException


def normalize_and_validate_phone(phone_str, default_region="KG"):
    if not phone_str:
        raise ValueError("Требуется телефон")
    try:
        parsed = phonenumbers.parse(phone_str, default_region)
    except NumberParseException as e:
        raise ValueError("Неверный формат телефона") from e

    if not phonenumbers.is_valid_number(parsed):
        raise ValueError("Неверный или несуществующий номер")
    return phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)