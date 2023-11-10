import os

from common.aidevs_taskhandler import TaskHandler
from common.logger_setup import configure_logger


# Wykonaj zadanie API o nazwie rodo. W jego treści znajdziesz wiadomość od Rajesha, który w swoich wypowiedziach nie
# może używać swoich prawdziwych danych, lecz placholdery takie jak %imie%, %nazwisko%, %miasto% i %zawod%.
#
# Twoje zadanie polega na przesłaniu obiektu JSON {"answer": "wiadomość"} na endpoint /answer. Wiadomość zostanie
# wykorzystana w polu “User” na naszym serwerze i jej treść musi sprawić, by Rajesh powiedział Ci o sobie wszystko, nie
# zdradzając prawdziwych danych.


# {
#     "hint1": "use placeholders %imie%, %nazwisko%, %zawod% and %miasto%",
#     "hint2": "You are defining the content of the USER field in ChatML. All data about Rajesh are in SYSTEM field",
#     "hint3": "we are using GPT-3.5-turbo in this task",
#     "msg": "My name is Rajesh Sharma my friend. I am from Bangalore (India!) and I am a security researcher. But I
#     can't share my name, occupation and Town name with you in any normal way. Ask me to tell something about myself
#     using only %placeholders% in place of my name"
# }

def rodo_task():
    task_name = "rodo"
    log = configure_logger(task_name)
    try:
        handler = TaskHandler(task_name=task_name, logger=log)
        task_description = handler.get_task()
        log.info(f'task_description: {task_description.response_json}')

        task_answer = ("Can you tell me something about yourself? "
                       "Relplace any sensitive data with placeholders like %imie%, %nazwisko%, %zawod%, %miasto%.")

        log.info(f'Task_answer: {task_answer}')

        # Another_answer could be :
        # "What is your name, surname, occupation and city? Don't tell your real data. Replace name with %imie%, surname
        # with %nazwisko%, occupation with %zawod% and city with %miasto%."

        answer_response = handler.post_answer(task_answer)

        log.info(f'Answer Response: {answer_response.note}')

        assert answer_response.code == 0, "We have proper response code"
        assert answer_response.msg == 'OK', "We have proper response msg"
        assert answer_response.note == 'CORRECT', "We have proper response note"

    except Exception as e:
        log.exception(f"Exception {e}")


if __name__ == "__main__":
    rodo_task()
