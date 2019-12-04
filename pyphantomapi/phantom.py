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
        return self._query(model=models.Container, endpoint='/container')

    def container(self, id):
        return self._query(
            model=models.Container,
            endpoint='/container',
            id=id
        )

    def create_container(self, container):
        return self._post('/container', container)

    def artifacts(self):
        return self._query(model=models.Artifact, endpoint='/artifact')

    def artifact(self, id):
        return self._query(
            model=models.Artifact,
            endpoint='/artifact',
            id=id
        )

    def create_artifact(self, artifact):
        return self._post('/artifact', artifact)

    def action_runs(self):
        return self._query(model=models.ActionRun, endpoint='/action_run')

    def action_run(self, id):
        return self._query(
            model=models.ActionRun,
            endpoint='/action_run',
            id=id
        )

    def assets(self):
        return self._query(model=models.Asset, endpoint='/asset')

    def asset(self, id):
        return self._query(
            model=models.Asset,
            endpoint='/asset',
            id=id
        )

    def apps(self):
        return self._query(model=models.App, endpoint='/app')

    def app(self, id):
        return self._query(
            model=models.App,
            endpoint='/app',
            id=id
        )

    def version(self):
        return self._get('/version')

    def system_info(self):
        return self._get('/system_info')

    def _query(self, model=None, endpoint=None, id=None):
        if id is None:
            _data = self._get(endpoint)['data']
            collection = []
            for item in _data:
                collection.append(model(self, item))
            return collection
        else:
            item = self._get(
                '{endpoint}/{id}'.format(endpoint=endpoint, id=id))
            return model(self, item)

    def _get(self, path):
        response = self.session.get(self.base_url + path, verify=False)
        return response.json()

    def _post(self, path, data):
        response = self.session.post(
            self.base_url + path, json=data, verify=False)
        return response.json()
