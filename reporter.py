import requests
import os
from dataclasses import dataclass


@dataclass
class ResultTestrun:
    """
    Объект результата прогона автотестов
    """

    failed_tests: int = 0
    skipped_tests: int = 0
    passed_tests: int = 0


def send_message():
    """
    Отправить сообщение в slack
    :return:
    """
    messenger_endpoint = os.getenv('MESSENGER_ENDPOINT')
    messenger_token = os.getenv('MESSENGER_TOKEN')
    channel_id = os.getenv('CHANNEL_ID')
    username = find_user_id(messenger_endpoint, messenger_token)

    try:
        requests.post(
            url=messenger_endpoint + 'posts',
            headers={
                "Content-type": "application/json",
                "Authorization": f"Bearer {messenger_token}",
            },
            json={
                "channel_id": channel_id,
                "message": get_message(get_result_testrun(), username),
            },
        )
    except Exception as e:
        raise Exception(f"Не удалось отправить сообщение. Ошибка {e}")


def get_message(result: ResultTestrun, username) -> str:
    """
    Сформировать сообщение
    :return:
    """
    service_name = os.getenv('CI_PROJECT_NAME')
    stage = os.getenv('STAGE')
    test_group = os.getenv('TEST_GROUP')
    branch = os.getenv('CI_COMMIT_REF_NAME')
    allure_url = os.getenv('ALLURE_LAUNCH_URL')
    pipline_url = os.getenv('CI_PIPELINE_URL')

    try:
        return (
            f"| {service_name} Autotests Results |\n"
            f"| ----------- |\n"
            f"| *Test stage:* {stage} *Test branch:* {branch} *Test group:* {test_group} |\n"
            f"| *Author:* @{username} |\n"
            f"| ✅ *Passed:* {result.passed_tests} ❌ *Failed:* {result.failed_tests} :grey_question: *Skipped:* {result.skipped_tests} | \n"
            f"| *Report:* {allure_url} |\n"
            f"| *Pipeline url:* {pipline_url} |"
        )
    except Exception as e:
        raise Exception(
            f"Не удалось сформировать сообщение для отправки в slack. Ошибка {e}"
        )


def get_result_testrun() -> ResultTestrun:
    """
    Получить результаты прогона автотестов
    """
    allure_endpoint = os.getenv('ALLURE_ENDPOINT')
    allure_launchID = os.getenv('ALLURE_LAUNCH_ID')
    allure_token = os.getenv('ALLURE_TOKEN')

    all_result = ResultTestrun()

    response = requests.get(
        url=allure_endpoint + "api/rs/launch/" + allure_launchID + "/statistic",
        headers={
            "Content-type": "application/json",
            "Authorization": f"Api-Token {allure_token}",
        },
    )

    for result in response.json():
        if result['status'] == 'passed':
            all_result.passed_tests = result['count']
        if (result['status'] == "failed") | (result['status'] == "broken"):
            all_result.failed_tests += result['count']
        if result['status'] == 'skipped':
            all_result.skipped_tests += result['count']

    return all_result


def find_user_id(messenger_endpoint, messenger_token) -> str:
    gitlab_email = os.getenv('GITLAB_USER_EMAIL')

    response = requests.get(
        url=messenger_endpoint + "users/email/" + gitlab_email,
        headers={
            "Content-type": "application/json",
            "Authorization": f"Bearer {messenger_token}",
        },
    )
    if response.json()['username']:
        return response.json()['username']

    return ''


if __name__ == "__main__":
    send_message()
