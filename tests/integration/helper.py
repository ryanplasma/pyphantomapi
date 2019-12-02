import betamax
import pyphantomapi
import os
import random
import string
import unittest


class IntegrationHelper(unittest.TestCase):
    def setUp(self):
        self.base_url = os.environ.get(
            'PHANTOM_BASE_URL', 'https://127.0.0.1/rest'
        )
        self.token = os.environ.get('PHANTOM_TOKEN', 'x' * 44)
        self.phantom = self.get_client()
        self.session = self.phantom.session
        self.recorder = betamax.Betamax(self.session)

    def get_client(self):
        return pyphantomapi.Phantom(self.base_url, self.token)

    def cassette_name(self, method, cls=None):
        class_name = cls or self.described_class
        return '_'.join([class_name, method])

    def source_data_identifier(self, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    @property
    def described_class(self):
        class_name = self.__class__.__name__
        return class_name[4:]
