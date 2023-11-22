import os
import time

from icecream import ic

from common.aidevs_taskhandler import TaskHandler
from common.files_read_and_download import get_file_name, download_file, read_file_contents
from common.logger_setup import configure_logger
from tasks.c03l05.C03L05_people_openAI_part import give_me_answer_based_on_context, user_template, get_data_dictionary
from tasks.c04l01.C04L01_knowledge_openAI_part import run_function_call, function_tools


# Wykonaj zadanie API o nazwie ‘knowledge’. Automat zada Ci losowe pytanie na temat kursu walut, populacji wybranego
# kraju lub wiedzy ogólnej. Twoim zadaniem jest wybór odpowiedniego narzędzia do udzielenia odpowiedzi (API z wiedzą
# lub skorzystanie z wiedzy modelu). W treści zadania uzyskanego przez API, zawarte są dwa API, które mogą być dla
# Ciebie użyteczne.

# {
#     'code': 0,
#     'msg': 'I will ask you a question about the exchange rate, the current population or general knowledge. Decide '
#            'whether you will take your knowledge from external sources or from the knowledge of the model',
#     'question': 'ile orientacyjnie ludzi mieszka w Polsce?',
#     'database #1': 'Currency http://api.nbp.pl/en.html (use table A)',
#     'database #2': 'Knowledge about countries https://restcountries.com/ - field 'population''
# }

# second sample question: jak nazywa się\xa0stolica Czech?

def knowledge_task():
    task_name = "knowledge"
    log = configure_logger(task_name)
    try:
        handler = TaskHandler(task_name=task_name, logger=log)
        task_description = handler.get_task()
        log.info(f'task_description: {task_description.response_json}')

        question = handler.get_task().question

        answer = run_function_call(function_tools, question)

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
    knowledge_task()
