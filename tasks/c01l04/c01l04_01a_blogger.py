from common.aidevs_taskhandler import TaskHandler
from common.logger_setup import configure_logger
from tasks.c01l04.c01l04_01b_openAI_part import generate_blog_content


# Write a blog post (in Polish) about making Margherita pizza. The task in the API is called "blogger". As input, you
# will receive an array of 4 chapters that must appear in the entry. As an answer,
# you must return an array (in JSON format) consisting of 4 fields representing these four chapters, e.g.:
# {"answer":["text1", "text2", "text3", "text4"]}.

# 'Wstęp: kilka słów na temat historii pizzy', 'Niezbędne składniki na pizzę', 'Robienie pizzy', 'Pieczenie pizzy w piekarniku'


def blogger_api_task():
    task_name = "blogger"
    log = configure_logger(task_name)
    try:
        handler = TaskHandler(task_name=task_name, logger=log)

        question = handler.get_task().msg
        log.info(f"Task question: {question}")

        task_answer = generate_blog_content(handler.task.blog, log)
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
    blogger_api_task()
