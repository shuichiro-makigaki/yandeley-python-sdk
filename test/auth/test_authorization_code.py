import vcr

from mendeley import Mendeley
from test import configure_mendeley
from test.auth import DummyStateGenerator


def test_should_get_auth_code_login_url():
    mendeley = Mendeley('id', 'secret', 'https://example.com')
    auth = mendeley.start_authorization_code_flow(DummyStateGenerator())

    assert auth.get_login_url() == 'https://api.mendeley.com/oauth/authorize?' \
                                   'response_type=code&' \
                                   'client_id=id&' \
                                   'redirect_uri=https%3A%2F%2Fexample.com&' \
                                   'scope=all&' \
                                   'state=state1234'


@vcr.use_cassette('fixtures/auth/authorization_code/get_authenticated_session.yaml', filter_headers=['authorization'])
def test_should_get_authenticated_session():
    mendeley = configure_mendeley()
    auth = mendeley.start_authorization_code_flow(DummyStateGenerator())

    session = auth.authenticate('https://example.com?state=state1234&code=IXpvu_-TpqiWYz-i0nBfO45PxIE')

    assert session.token['access_token'] == \
        'MSwxNDA5MDYyODIwOTY5LDEyNDAxODUxLDgwMSxhbGwsLFYyYVlTNnBPWlBwZW5sVWNPUzlYdTZON09ONA'
    assert session.mendeley.host == 'https://api.mendeley.com'
