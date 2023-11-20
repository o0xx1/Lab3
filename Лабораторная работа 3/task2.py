# TODO Напишите функцию find_common_participants
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
def find_common_participants(participants_first_group, participants_second_group, sep=','):
    first_group = participants_first_group.split(sep)
    second_group = participants_second_group.split(sep)
    common_participants_list = list(set(first_group).intersection(second_group))  # список общих участников среди двух групп
    common_participants_list.sort()
    return common_participants_list
# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, sep='|'))
