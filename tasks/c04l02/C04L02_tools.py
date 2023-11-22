import os
import time
from datetime import datetime

from icecream import ic

from common.aidevs_taskhandler import TaskHandler
from common.files_read_and_download import get_file_name, download_file, read_file_contents
from common.logger_setup import configure_logger
from tasks.c04l02.C04L02_tools_openAI_part import run_function_call, function_tools


# Rozwiąż zadanie API o nazwie ‘tools’. Celem zadania jest zdecydowanie, czy podane przez API zadanie powinno zostać
# dodane do listy zadań (To Do), czy do kalendarza (jeśli ma ustaloną datę). Oba narzędzia mają lekko definicje
# struktury JSON-a (różnią się jednym polem). Spraw, aby Twoja aplikacja działała poprawnie na każdym zestawie
# danych testowych.

# {
#     'code': 0,
#     'msg': 'Decide whether the task should be added to the To Do list or to the calendar (if time is provided) and '
#            'return the corresponding JSON',
#     'hint': 'always use YYYY-MM-DD format for dates',
#     'example for To Do': 'Przypomnij mi, że mam kupić mleko = {'tool':'ToDo','desc':'Kup mleko' }',
#     'example for Calendar': 'Jutro mam spotkanie z Marianem = {'tool':'Calendar','desc':'Spotkanie z '
#                             'Marianem','date':'2023-11-20'}',
#     'question': 'Przypomnij mi, abym zapisał się na AI Devs 3.0'
# }

# second sample: Pojutrze mam kupić 1kg ziemniaków

def tools_task():
    task_name = "tools"
    log = configure_logger(task_name)
    try:
        handler = TaskHandler(task_name=task_name, logger=log)
        task_description = handler.get_task()
        log.info(f'task_description: {task_description.response_json}')

        question = handler.get_task().question
        current_date_time = datetime.now()
        formatted_date = current_date_time.strftime('%Y-%m-%d')

        system_context = f"Context:```\n Today is {formatted_date}\n```"
        answer = run_function_call(function_tools, question, system_context)

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
    tools_task()
