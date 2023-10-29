import logging

from common.aidevs_taskhandler import TaskHandler

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


def hello_api_task():
    try:
        task_name = 'helloapi'
        handler = TaskHandler(task_name)

        question = handler.get_task().msg
        log.info(f'Task question: {question}')

        task_answer = handler.task.cookie
        log.info(f'Task_answer: {task_answer}')

        answer_response = handler.post_answer(task_answer)
        log.info(f'Answer Response: {answer_response.note}')

        assert answer_response.code == 0, "We have proper response code"
        assert answer_response.msg == 'OK', "We have proper response msg"
        assert answer_response.note == 'CORRECT', "We have proper response note"

    except Exception as e:
        log.error(f'Exception {e}')


if __name__ == "__main__":
    hello_api_task()
