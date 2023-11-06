import os

from common.aidevs_taskhandler import TaskHandler
from common.logger_setup import configure_logger
from tasks.c02l05.c02l05_function_calling_openAi_part import function_definition_add_user

# Wykonaj zadanie o nazwie functions zgodnie ze standardem zgłaszania odpowiedzi opisanym na zadania.aidevs.pl. Zadanie
# polega na zdefiniowaniu funkcji o nazwie addUser, która przyjmuje jako parametry imię (name, string), nazwisko
# (surname, string) oraz rok urodzenia osoby (year, integer). Jako odpowiedź musisz wysłać jedynie ciało funkcji w
# postaci JSON-a.


# 'send me definition of function named addUser that require 3 params: name (string), surname (string) and year of born
# in field named "year" (integer). Set type of function to "object"',
# 'hint1': "I will use this function like this: addUser({'John','Smith',1974})",
# 'hint2': "send this definition as correct JSON structure inside 'answer' field (as usual)

hint = {"answer": {
    "name": "orderPizza",
    "description": "select pizza in pizzeria based on pizza name",
    "parameters": {
        "type": "object",
        "properties": {
            "name": {
                "type": "string",
                "description": "provide name of the pizza"
            }
        }
    }
}
}


def functions_api_task():
    task_name = "functions"
    log = configure_logger(task_name)
    try:
        handler = TaskHandler(task_name=task_name, logger=log)
        task_description = handler.get_task()
        log.info(f'task_description: {task_description.response_json}')

        task_answer = function_definition_add_user
        log.info(f'Task_answer: {task_answer}')

        answer_response = handler.post_answer(task_answer)
        log.info(f'Answer Response: {answer_response.note}')

        assert answer_response.code == 0, "We have proper response code"
        assert answer_response.msg == 'OK', "We have proper response msg"
        assert answer_response.note == 'CORRECT', "We have proper response note"

    except Exception as e:
        log.exception(f"Exception {e}")


if __name__ == "__main__":
    functions_api_task()
