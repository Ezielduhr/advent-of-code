#!/usr/bin/env python3
from library.shared_functions import get_input


def main():
    challenge_input = get_input("input_06.txt")[0]
    start_pattern_length = 4
    start_message_length = 14

    char_cache = set()
    message_cache = set()
    lock_chars_checked = 4
    message_chars_checked = 14

    start_char = int()
    start_message_char = int()

    first_time_lock = True
    first_time_message = True

    for integer in range(len(challenge_input)):
        pattern_to_check = challenge_input[integer:lock_chars_checked]
        message_to_check = challenge_input[integer:message_chars_checked]
        char_cache.update(pattern_to_check)
        message_cache.update(message_to_check)

        if len(char_cache) == start_pattern_length and first_time_lock:
            start_char = integer + start_pattern_length
            first_time_lock = False

        if len(message_cache) == start_message_length and first_time_message:
            start_message_char = integer + start_message_length
            first_time_message = False

        # Up chars checked by one, so we check the next 4 chars
        lock_chars_checked += 1
        message_chars_checked += 1
        # Reset sets
        char_cache = set()
        message_cache = set()

    return start_char, start_message_char


if __name__ == "__main__":
    signal_lock, start_message = main()
    print(signal_lock, start_message)
