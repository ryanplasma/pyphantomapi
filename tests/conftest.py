import os

import betamax
import urllib3
from betamax_serializers import pretty_json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

betamax.Betamax.register_serializer(pretty_json.PrettyJSONSerializer)

with betamax.Betamax.configure() as config:
    config.cassette_library_dir = "tests/cassettes"
    config.default_cassette_options['record_mode'] = "new_episodes"
    config.define_cassette_placeholder(
        "<BASE_URL>", os.environ.get(
            'PHANTOM_BASE_URL', 'https://127.0.0.1/rest'
        )
    )
    config.define_cassette_placeholder(
        "<TOKEN>", os.environ.get('PHANTOM_TOKEN', 'x' * 44)
    )
    config.default_cassette_options['serialize_with'] = 'prettyjson'
