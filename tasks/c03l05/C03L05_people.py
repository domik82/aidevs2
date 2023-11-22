import os
import time

from icecream import ic

from common.aidevs_taskhandler import TaskHandler
from common.files_read_and_download import get_file_name, download_file, read_file_contents
from common.logger_setup import configure_logger
from tasks.c03l05.C03L05_people_openAI_part import give_me_answer_based_on_context, user_template, get_data_dictionary


# Rozwiąż zadanie o nazwie “people”. Pobierz, a następnie zoptymalizuj odpowiednio pod swoje potrzeby bazę danych
# https://zadania.aidevs.pl/data/people.json [jeśli pobrałeś plik przed 11:30, to pobierz proszę poprawioną wersję].
# Twoim zadaniem jest odpowiedź na pytanie zadane przez system. Uwaga!
# Pytanie losuje się za każdym razem na nowo, gdy odwołujesz się do /task.
# Spraw, aby Twoje rozwiązanie działało za każdym razem, a także, aby zużywało możliwie mało tokenów.
# Zastanów się, czy wszystkie operacje muszą być wykonywane przez LLM-a
# może warto zachować jakiś balans między światem kodu i AI?

# 'retrieve the data set (JSON) and answer the question. The question will change every time the task is called. I only
# ask about favourite colour, favourite food and place of residence',
# 'data': 'https://zadania.aidevs.pl/data/people.json',
# 'question': 'Gdzie mieszka Krysia Ludek?',
# 'hint1': 'Does everything have to be handled by the language model?',
# 'hint2': 'prepare knowledge DB for this task'

def people_task():
    task_name = "people"
    log = configure_logger(task_name)
    try:
        handler = TaskHandler(task_name=task_name, logger=log)
        task_description = handler.get_task()
        log.info(f'task_description: {task_description.response_json}')

        question = handler.get_task().question

        url = 'https://zadania.aidevs.pl/data/people.json'
        people_dict = get_data_dictionary(url)
        context = ""

        system_template = read_file_contents('name_category_system_prompt.txt')
        ai_response = give_me_answer_based_on_context(user_template, question, system_template, context, log)
        if "I don't know" in ai_response:
            raise ValueError

        name, category = ai_response.strip().split(';')
        name = name.strip().upper()
        category = category.strip()

        ic(name.upper())
        answer = people_dict[name].get(category)

        ic(answer)
        task_answer = answer

        answer_response = handler.post_answer(task_answer)
        log.info(f'Answer Response: {answer_response.note}')

        assert answer_response.code == 0, "We have proper response code"
        assert answer_response.msg == 'OK', "We have proper response msg"
        assert answer_response.note == 'CORRECT', "We have proper response note"

    except Exception as e:
        log.exception(f"Exception {e}")


if __name__ == "__main__":
    people_task()
