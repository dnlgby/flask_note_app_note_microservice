# Copyright (c) 2023 Daniel Gabay

import os


class DatabaseServiceUrlStringWrapper:
    def __init__(self):
        self.value = os.getenv("DATABASE_SERVICE_URL")
        if self.value is None:
            raise ValueError("The DATABASE_SERVICE_URL environment variable must be set")
