from sorter import sorter
import difflib
from weather_func import get_weather
from user_interface import *
import holidays
from datetime import date


def parser(msg: str):
    """ Parser and handler AIO """
    command = None
    params = []

    for key in operations:
        if msg.lower().startswith(key):
            command = operations[key]
            msg = msg.lstrip(key)
            for item in filter(lambda x: x != '', msg.split(' ')):
                params.append(item)
            return command, params
    return command, params


def today_holiday(*args):
    if len(args):
        day = int(args[0])
    else:
        day = 0
    ua_holidays = holidays.country_holidays('UA')
    if day:
        result = []
        d_start = date.today().toordinal()
        for el in range(d_start, d_start+day):
            res = ua_holidays.get(date.fromordinal(el))
            if res:
                result.append((date.fromordinal(el).strftime('%d-%m-%Y'), res))
        if len(result):
            columns = ['Date', 'Name']
            return tabulate(result, headers=columns, tablefmt='psql')
        else:
            return 'No holiday in period'
    else:
        res = ua_holidays.get(date.today())
    if res is None:
        return 'No holiday today'
    return res


def incorrect_input(msg):
    """Function to check correctness"""
    guess = difflib.get_close_matches(msg, operations.keys())
    if guess:
        return f'Do you have paws too? Maybe you mean: {", ".join(guess)}'
    else:
        return f"Sorry, I don't know this command. Type for help for help."


operations = {
    'hello': CLI.hello,
    'help': CLI.help_to_console,
    'add_contact': CLI.add_contact_or_phone,
    'change_phone': CLI.change_phone,
    'change_address': CLI.change_address,
    'change_birthday': CLI.change_birthday,
    'change_email': CLI.change_email,
    'phone': CLI.phone_func,
    'show_all': CLI.show_all,
    'exit': CLI.goodbye,
    'delete_phone': CLI.delete_phone,
    'contact_delete': CLI.delete_user,
    'search': CLI.search_in_contacts,
    'sort': sorter,
    'note_add': CLI.adding_note,
    'note_delete': CLI.delete_note,
    'note_edit': CLI.editing_note,
    'note_show_all': CLI.show_all_note,
    'tag_search': CLI.searching_by_tag,
    'tag_sort': CLI.sorting_by_tags,
    'birthday': CLI.list_record_to_x_day_bd,
    'word_search': CLI.searching_by_word,
    'holiday': today_holiday,
    'weather': get_weather,
}


def startup_loader():
    CONTACTS.load_from_file(FILENAME_CONTACTS)
    NOTES.load_from_file(FILENAME_NOTES)
