import json
import urllib

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

    def app_runs(self):
        return self._query(model=models.AppRun, endpoint='/app_run')

    def app_run(self, id):
        return self._query(
            model=models.AppRun,
            endpoint='/app_run',
            id=id
        )

    def playbook_runs(self):
        return self._query(model=models.PlaybookRun, endpoint='/playbook_run')

    def playbook_run(self, id):
        return self._query(
            model=models.PlaybookRun,
            endpoint='/playbook_run',
            id=id
        )

    def version(self):
        return self._get('/version')

    def system_info(self):
        return self._get('/system_info')

    def _query(self, model=None, endpoint=None, id=None, page_size=10, page=0):
        query_string = urllib.parse.urlencode({
            'page_size': page_size,
            'page': page
        })

        if id is None:
            response = self._get(
                '{endpoint}?{query_string}'.format(
                    endpoint=endpoint,
                    query_string=query_string))
            collection = []
            for item in response['data']:
                collection.append(model(self, item))
            return {
                'data': collection,
                'count': response['count'],
                'num_pages': response['num_pages']
            }
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
