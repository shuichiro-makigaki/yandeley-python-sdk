import time

import vcr
import yaml
import os

from yandeley import Mendeley
from yandeley.session import MendeleySession
from test.yamlfileserializer import YamlFileSerializer


class DummyStateGenerator(object):
    @staticmethod
    def generate_state():
        return 'state1234'


def load_config_from_file(filename):
    with open(filename) as f:
        config = yaml.load(f)
        
        if 'MENDELEY_CLIENT_ID' in os.environ:
            config['clientId'] = os.environ.get('MENDELEY_CLIENT_ID')
        
        if 'MENDELEY_CLIENT_SECRET' in os.environ:
            config['clientSecret'] = os.environ.get('MENDELEY_CLIENT_SECRET')
        
        if 'MENDELEY_ACCESS_TOKEN' in os.environ:
            config['accessToken'] = os.environ.get('MENDELEY_ACCESS_TOKEN')

        if 'MENDELEY_REDIRECT_URI' in os.environ:
            config['redirectUri'] = os.environ.get('MENDELEY_REDIRECT_URI')

        return config


def load_config():
    try:
        return load_config_from_file('test_config.yml')
    except IOError:
        return load_config_from_file('test_config.yml.default')


def configure_mendeley():
    config = load_config()
    return Mendeley(config['clientId'],
                    config['clientSecret'],
                    config['redirectUri'],
                    state_generator=DummyStateGenerator())


def get_user_session():
    config = load_config()
    mendeley = configure_mendeley()
    token = {'access_token': config['accessToken']}

    return MendeleySession(mendeley, token)


def get_client_credentials_session():
    config = load_config()
    mendeley = configure_mendeley()

    if config['recordMode'] == 'none':
        token = {'access_token': config['accessToken']}
        return MendeleySession(mendeley, token)
    else:
        return mendeley.start_client_credentials_flow().authenticate()


def cassette(path):
    config = load_config()
    my_vcr = vcr.VCR()
    my_vcr.register_serializer('file', YamlFileSerializer())

    return my_vcr.use_cassette(path,
                               filter_headers=['authorization'],
                               record_mode=config['recordMode'],
                               serializer='file')


def sleep(seconds):
    config = load_config()

    if config['recordMode'] != 'none':
        time.sleep(seconds)
