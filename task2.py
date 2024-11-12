import re

def data_func():
    with open('data.txt', 'r', encoding='utf-8') as file:
        with open('data_new.txt', 'w', encoding='utf-8') as new_data:
            for i in file:
                pattern_email = r'[-\w\.]+@([-\w]+\.)+[-\w]{2,4}'
                pattern_telephone = r'\+380\(\d{2}\)\d{3}-\d{2}-\d{2}'
                pattern_birthday = r'\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/[0-9]{4}\b'

                result_birthday = re.finditer(pattern_birthday, i)
                result_email = re.finditer(pattern_email, i)
                result_telephone = re.finditer(pattern_telephone, i)

                for match in result_birthday:
                    new_data.write(match.group()+ '\n')

                for match in result_email:
                    new_data.write(match.group()+ '\n')

                for match in result_telephone:
                    new_data.write(match.group()+ '\n')


data_func()

