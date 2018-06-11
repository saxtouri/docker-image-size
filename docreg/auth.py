# Copyright 2018 Stavros Sachtouris
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import requests
import logging
from docreg import DockerRegistryClientException

logger = logging.getLogger(__name__)


class DockerRegistryAuthClient:

    def __init__(self, url='https://auth.docker.io'):
        self.url = url

    def get_token(self, scope, service='registry.docker.io'):
        """
        :param scope: https://docs.docker.com/registry/spec/auth/scope/
        :param service: the authentication service
        """
        params = dict(scope=scope, service=service)
        r = requests.get('{}/token'.format(self.url), params=params)
        if r.status_code in (200, ):
            return r.json()['token']
        raise DockerRegistryClientException(r.text)


if __name__ == '__main__':
    dr = DockerRegistryAuthClient()
    print(dr.get_token(scope='repository:google/cadvisor:latest'))
