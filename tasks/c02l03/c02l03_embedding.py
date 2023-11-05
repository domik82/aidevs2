from common.aidevs_taskhandler import TaskHandler
from common.logger_setup import configure_logger
from tasks.c01l05.c01l05_liar_openAI_part import validate_bot_answer
from tasks.c02l03.c02l03_embedding_openAI_part import create_embedding


def embedding_api_task(text):
    task_name = "embedding"
    log = configure_logger(task_name)
    try:
        handler = TaskHandler(task_name=task_name, logger=log)
        task_description = handler.get_task()
        log.info(f'task_description: {task_description}')

        task_answer = create_embedding(text, log)
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
    text = "Hawaiian pizza"
    embedding_api_task(text)
