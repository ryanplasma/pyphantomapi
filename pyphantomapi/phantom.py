import json

import requests

from . import models


class Phantom(object):
    def __init__(self, base_url=None, token=None):
        self.base_url = base_url
        self.token = token

        self.session = requests.Session()
        self.session.headers.update({'ph-auth-token': self.token})

    def containers(self):
        _data = self._get('/container')
        containers = []
        for container in _data['data']:
            containers.append(models.Container(self, container))
        return container

    def container(self, id):
        _data = self._get("/container/{}".format(id))
        return models.Container(self, _data)

    def create_container(self, container):
        return self._post('/container', container)

    def artifacts(self):
        _data = self._get('/artifact')
        artifacts = []
        for artifact in _data['data']:
            artifacts.append(models.Artifact(self, artifact))
        return artifacts

    def artifact(self, id):
        _data = self._get("/artifact/{}".format(id))
        return models.Artifact(self, _data)

    def create_artifact(self, artifact):
        return self._post('/artifact', artifact)

    def version(self):
        return self._get('/version')

    def _get(self, path):
        response = self.session.get(self.base_url + path, verify=False)
        return response.json()

    def _post(self, path, data):
        response = self.session.post(
            self.base_url + path, json=data, verify=False)
        return response.json()
