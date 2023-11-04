import json
from typing import Dict, Any

import requests

from common.aidevs_responsehandler import (
    ResponseTokenHandler,
    ResponseTaskHandler,
    ResponseAnswerHandler,
)
from common.constants import AI_DEVS_SERVER, AI_DEVS_USER_TOKEN
from common.logger_setup import configure_logger


class TaskHandler:
    def __init__(
            self,
            task_name: str = None,
            base_url: str = AI_DEVS_SERVER,
            user_api_key: str = AI_DEVS_USER_TOKEN,
            logger=None,
    ):
        self.base_url: str = base_url
        self.user_api_key: str = user_api_key
        self._user_api_key_json: Dict[str, str] = {"apikey": self.user_api_key}
        self.task_name: str = task_name
        self.task_token: ResponseTokenHandler = None
        self.task: ResponseTaskHandler = None
        self.ai_devs_bot: ResponseTaskHandler = None
        self.log = logger if logger is not None else configure_logger()
        self.log.info(f"Task Name: {self.task_name}")

    def get_task_token_by_task_name(self, task_name: str) -> ResponseTokenHandler:
        if task_name != "":
            response = requests.post(
                f"{self.base_url}/token/{task_name}", json=self._user_api_key_json
            )
            if response.status_code == 200:
                self.log.info(f"get_task_token response: {response.json()}")
                parsed_response = ResponseTokenHandler(response.json())
                return parsed_response
            else:
                raise Exception(
                    f"Failed to get token. Status code: {response.status_code}, body: {response.json()}"
                )
        else:
            raise ValueError(f"Please provide task name")

    def get_task_by_token(self, token_id: str) -> ResponseTaskHandler:
        if token_id != "":
            response = requests.get(
                f"{self.base_url}/task/{token_id}",
                json=self._user_api_key_json,
            )
            if response.status_code == 200:
                self.log.info(f"get_task_by_token response: {response.json()}")
                return ResponseTaskHandler(response.json())
            else:
                raise Exception(
                    f"Failed to get task. Status code: {response.status_code}, body: {response.json()}"
                )
        else:
            raise ValueError(f"Please provide token_id")

    def get_task(self) -> ResponseTaskHandler:
        self.task_token = self.get_task_token_by_task_name(self.task_name)
        self.task = self.get_task_by_token(self.task_token.token)
        return self.task

    def get_task_token_value(self) -> str:
        return self.task_token.token

    def post_answer(self, answer: Any, as_data=False) -> ResponseAnswerHandler:
        if (token_value := self.get_task_token_value()) != "":
            task_answer = {"answer": answer}
            self.log.info(f"task_answer: {json.dumps(task_answer)}")
            if as_data:
                response = requests.post(
                    f"{self.base_url}/answer/{token_value}", data=task_answer
                )
            else:
                response = requests.post(
                    f"{self.base_url}/answer/{token_value}", json=task_answer
                )
            if response.status_code == 200:
                self.log.info(f"post_answer response: {response.json()}")
                return ResponseAnswerHandler(response.json())
            else:
                raise Exception(
                    f"Failed to post answer. Status code: {response.status_code}, body: {response.json()}"
                )
        else:
            raise RuntimeError(f"Task token doesn't exist")

    def get_ai_devs_bot_answer(self, question: Any) -> ResponseTaskHandler:
        if self.task_token != "":
            self.log.info(f'task_token: {self.get_task_token_value()}')
            question = {"question": question}
            response = requests.post(
                f"{self.base_url}/task/{self.get_task_token_value()}",
                data=question,
            )
            if response.status_code == 200:
                self.log.info(f"get_task_by_token response: {response.json()}")
                self.ai_devs_bot = ResponseTaskHandler(response.json())
                return self.ai_devs_bot.answer
            else:
                raise Exception(
                    f"Failed to get task. Status code: {response.status_code}, body: {response.json()}"
                )
        else:
            raise ValueError(f"Please provide token_id")


