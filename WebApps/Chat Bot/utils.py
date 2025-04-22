import random
from string import ascii_letters, digits

def generate_room_code(length: int, existing_codes: list[str]) -> str:
    while True:
        code_chars = [random.choice(ascii_letters + digits) for _ in range(length)]
        room_code = ''.join(code_chars)

        if room_code not in existing_codes:
            return room_code