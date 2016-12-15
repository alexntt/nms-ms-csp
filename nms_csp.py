import requests


LOGIN_URL='https://login.windows.net/common/oauth2/token'
RESOURCE_URL='https://api.partnercenter.microsoft.com'


class CspClient(object):
    """
    :param str username: Partner username, user@domain
    :param str client_id: Application id registered in the portal
    """
    def __init__(self, username, password, client_id):
        self.username = username
        self.password = password
        self.client_id = client_id

    def login(self):
        self.token = self._get_token_raw()['access_token']
        print self.token

    def _get_token_raw(self):
        response = requests.post(LOGIN_URL,
                                 data={'grant_type': 'password',
                                       'username': self.username,
                                       'password': self.password,
                                       'resource': RESOURCE_URL,
                                       'client_id': self.client_id})
        return response.json()

    def _get_customers_raw(self):
        response = requests.get('{0}/v1/customers'.format(RESOURCE_URL),
                            headers={'Authorization': 'Bearer {0}'.format(self.token),
                                     'Accept': 'application/json'})
        response.encoding = 'utf-8-sig'  # HACK: since a random point in time, JSON
                                         # returned contained a BOM and requests refused
                                         # to parse it; this strips the BOM
        return response.json()
