import os
import time

from icecream import ic

from common.aidevs_taskhandler import TaskHandler
from common.files_read_and_download import get_file_name, download_file, read_file_contents
from common.logger_setup import configure_logger
from tasks.c03l02.c03l02_scraper_openAi_part import give_me_answer_based_on_context, user_template, system_template


# Rozwiąż zadanie z API o nazwie "scraper". Otrzymasz z API link do artykułu (format TXT), który zawiera pewną wiedzę,
# oraz pytanie dotyczące otrzymanego tekstu. Twoim zadaniem jest udzielenie odpowiedzi na podstawie artykułu. Trudność
# polega tutaj na tym, że serwer z artykułami działa naprawdę kiepsko — w losowych momentach zwraca błędy typu "error
# 500", czasami odpowiada bardzo wolno na Twoje zapytania, a do tego serwer odcina dostęp nieznanym przeglądarkom
# internetowym. Twoja aplikacja musi obsłużyć każdy z napotkanych błędów. Pamiętaj, że pytania, jak i teksty źródłowe,
# są losowe, więc nie zakładaj, że uruchamiając aplikację kilka razy, za każdym razem zapytamy Cię o to samo i będziemy
# pracować na tym samym artykule.

# 'msg': Return answer for the question in POLISH language, based on provided article. Maximum length for the answer is 200 characters
# 'input': '{AI_DEVS_SERVER}/text_pasta_history.txt',
# 'question': 'komu przypisuje się przepis na danie lagana?

# 'input': {AI_DEVS_SERVER}/text_pizza_history.txt
# 'question': 'w którym roku według legendy została wynaleziona pizza Margherita?

# server error X_X


def scraper_api_task():
    task_name = "scraper"
    log = configure_logger(task_name)
    try:
        handler = TaskHandler(task_name=task_name, logger=log)
        task_description = handler.get_task()
        log.info(f'task_description: {task_description.response_json}')

        file = get_file_name(task_description.input)
        retry = 5
        context = ""

        for i in range(retry):
            try:
                download_file(task_description.input)
                context = read_file_contents(file)
                ic(context)
                if "server error X_X" in context:
                    ic("server error X_X")
                    context = ""
                    raise ValueError
                else:
                    break
            except ValueError:
                if i == retry - 1:
                    raise

        question = task_description.question
        if context != "":
            task_answer = give_me_answer_based_on_context(user_template, question, system_template, context, log)
        else:
            raise ValueError
        log.info(f'Task_answer: {task_answer}')

        answer_response = handler.post_answer(task_answer)
        log.info(f'Answer Response: {answer_response.note}')

        assert answer_response.code == 0, "We have proper response code"
        assert answer_response.msg == 'OK', "We have proper response msg"
        assert answer_response.note == 'CORRECT', "We have proper response note"

    except Exception as e:
        log.exception(f"Exception {e}")


if __name__ == "__main__":
    scraper_api_task()
