# Copyright (c) 2023 Daniel Gabay

from injector import singleton, Module

from di.wrappers import DatabaseServiceUrlStringWrapper


class ServiceModule(Module):
    def configure(self, binder):
        binder.bind(DatabaseServiceUrlStringWrapper, to=DatabaseServiceUrlStringWrapper, scope=singleton)
