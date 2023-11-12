from icecream import ic

from common.aidevs_taskhandler import TaskHandler
from common.logger_setup import configure_logger
from tasks.c03l04.qdrant_embeddings_full import QdrantVectorStore


# zaimportuj do swojej bazy wektorowej, spis wszystkich linków z newslettera
# unknowNews z adresu: https://unknow.news/archiwum.json


# Następnie wykonaj zadanie API o nazwie “search” — odpowiedz w nim na zwrócone przez API pytanie. Odpowiedź musi być
# adresem URL kierującym do jednego z linków unknowNews. Powodzenia!


def search_api_task():
    task_name = "search"
    log = configure_logger(task_name)
    qdrant_host = 'localhost'
    qdrant_port = 6333
    qdrant_collection_name = 'unknow_news'
    ai_vector_size = 1536

    vector_db_obj = QdrantVectorStore(host=qdrant_host,
                                      port=qdrant_port,
                                      collection_name=qdrant_collection_name,
                                      vector_size=ai_vector_size)

    try:
        handler = TaskHandler(task_name=task_name, logger=log)
        task_description = handler.get_task()
        log.info(f'task_description: {task_description.response_json}')

        question = handler.get_task().question
        hints = vector_db_obj.search_using_embedded_query(question)

        for hint in hints:
            task_answer = hint.get('url')
            log.info(f'Task_answer: {task_answer}')

            answer_response = handler.post_answer(task_answer)
            log.info(f'Answer Response: {answer_response.note}')

            assert answer_response.code == 0, "We have proper response code"
            assert answer_response.msg == 'OK', "We have proper response msg"
            assert answer_response.note == 'CORRECT', "We have proper response note"
            break


    except Exception as e:
        log.exception(f"Exception {e}")


if __name__ == "__main__":
    search_api_task()
