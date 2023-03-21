# Copyright (c) 2023 Daniel Gabay

import requests

from tenacity import retry, stop_after_attempt, wait_exponential


class RequestHandler:
    """
    A handler class to perform POST requests with retry mechanism using tenacity.
    """

    class RETRY_POLICY:
        ATTEMPTS = 3
        EXP_MULTIPLIER, EXP_MIN, EXP_MAX = 1, 2, 8

        STOP_POLICY = stop_after_attempt(ATTEMPTS)
        WAIT_POLICY = wait_exponential(multiplier=EXP_MULTIPLIER, min=EXP_MIN, max=EXP_MAX)

    @staticmethod
    @retry(stop=RETRY_POLICY.STOP_POLICY, wait=RETRY_POLICY.WAIT_POLICY)
    def perform_get_request(url: str, endpoint: str) -> requests.Response:
        """
        Perform a GET request to the specified URL and endpoint with the given payload.

        :param url: The base URL.
        :param endpoint: The API endpoint.
        :return: A requests.Response object.
        """
        return requests.get(f"{url}/{endpoint}")

    @staticmethod
    @retry(stop=RETRY_POLICY.STOP_POLICY, wait=RETRY_POLICY.WAIT_POLICY)
    def perform_post_request(url: str, endpoint: str, payload: dict) -> requests.Response:
        """
        Perform a POST request to the specified URL and endpoint with the given payload.

        :param url: The base URL.
        :param endpoint: The API endpoint.
        :param payload: A dictionary containing the data to be sent in the request body.
        :return: A requests.Response object.
        """
        return requests.post(f"{url}/{endpoint}", json=payload)

    @staticmethod
    @retry(stop=RETRY_POLICY.STOP_POLICY, wait=RETRY_POLICY.WAIT_POLICY)
    def perform_patch_request(url: str, endpoint: str, payload: dict) -> requests.Response:
        """
        Perform a PATCH request to the specified URL and endpoint with the given payload.

        :param url: The base URL.
        :param endpoint: The API endpoint.
        :param payload: A dictionary containing the data to be sent in the request body.
        :return: A requests.Response object.
        """
        return requests.patch(f"{url}/{endpoint}", json=payload)

    @staticmethod
    @retry(stop=RETRY_POLICY.STOP_POLICY, wait=RETRY_POLICY.WAIT_POLICY)
    def perform_delete_request(url: str, endpoint: str) -> requests.Response:
        """
        Perform a DELETE request to the specified URL and endpoint.

        :param url: The base URL.
        :param endpoint: The API endpoint.
        :return: A requests.Response object.
        """
        return requests.delete(f"{url}/{endpoint}")
