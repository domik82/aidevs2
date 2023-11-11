from icecream import ic

from common.aidevs_taskhandler import TaskHandler
from common.logger_setup import configure_logger
from tasks.c03l03.c03l03_whoami_openAI_part import give_me_answer_based_on_context, user_template, system_template


# 'msg': 'Each time you call up this task, I will return a trivia item about a certain person
# (the person does not change). Guess who I am',
# 'hint': 'pracował jako technik w firmie Atari'

def whoami_api_task():
    task_name = "whoami"
    log = configure_logger(task_name)
    try:
        handler = TaskHandler(task_name=task_name, logger=log)
        task_description = handler.get_task()
        log.info(f'task_description: {task_description.response_json}')

        hint = task_description.hint
        context = ""
        final_response = ""
        i = 0  # avoid risks ;)
        while final_response == "" and i < 10:
            response = give_me_answer_based_on_context(user_template, hint, system_template, context, log)
            ic(response)
            i += 1
            if "I don't know" in response:
                context = context + "," + hint
                hint = handler.get_task_by_token(handler.get_task_token_value()).hint
                ic(hint)
            else:
                final_response = response
                ic(final_response)
                break

        task_answer = final_response
        log.info(f'Task_answer: {task_answer}')

        answer_response = handler.post_answer(task_answer)
        log.info(f'Answer Response: {answer_response.note}')

        assert answer_response.code == 0, "We have proper response code"
        assert answer_response.msg == 'OK', "We have proper response msg"
        assert answer_response.note == 'CORRECT', "We have proper response note"

    except Exception as e:
        log.exception(f"Exception {e}")


if __name__ == "__main__":
    whoami_api_task()
