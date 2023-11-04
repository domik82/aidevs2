from common.aidevs_taskhandler import TaskHandler
from common.logger_setup import configure_logger
from tasks.c01l05.c01l05_liar_openAI_part import validate_bot_answer


# Perform a task called liar. This is a mechanism that says off topic 1/3 of the time. Your task is to send your
# question in English (any question, e.g. "What is capital of Poland?") to the endpoint /task/ in a field named
# 'question' (POST method, as a regular form field, NOT JSON). The API system will answer that question (in the 'answer'
# field) or start telling you about something completely different, changing the subject.
#
# Your task is to write a filtering system (Guardrails) that will determine (YES/NO) whether the answer is on topic.
# Then return your verdict to the checking system as a single YES/NO word.
# If you retrieve the content of the task through the API without sending any additional parameters,
# you will get a set of prompts.
# How to know if the answer is 'on topic'?
# If your question # was about the capital of Poland, and in the answer you receive a list of monuments in Rome,
# the answer to send to the API is NO

def liar_api_task():
    task_name = "liar"
    log = configure_logger(task_name)
    try:
        handler = TaskHandler(task_name=task_name, logger=log)
        task_description = handler.get_task()

        question = "Co jest stolicą Polski?"
        log.info(f"Task question: {question}")

        bot_answer = handler.get_ai_devs_bot_answer(question)
        log.info(f"bot_answer: {bot_answer}")
        task_answer = validate_bot_answer(question, bot_answer, log)

        log.info(f'Task_answer: {task_answer}')
        #
        answer_response = handler.post_answer(task_answer)
        log.info(f'Answer Response: {answer_response.note}')

        assert answer_response.code == 0, "We have proper response code"
        assert answer_response.msg == 'OK', "We have proper response msg"
        assert answer_response.note == 'CORRECT', "We have proper response note"

    except Exception as e:
        log.error(f"Exception {e}")


if __name__ == "__main__":
    liar_api_task()
