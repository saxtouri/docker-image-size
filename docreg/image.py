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


class DockerRegistryImageClient:
    """Request information on an image from a docker registry"""

    def __init__(
            self,
            prefix='registry.hub.docker.com',
            user=None, password=None, token=None):
        msg = 'init DockerRegistry({}, {}, {})'
        logger.debug(msg.format(prefix, user, password))
        self.prefix = prefix
        self.user = user
        self.password = password
        self.url = 'https://{}'.format(self.prefix)
        self.auth = requests.auth.HTTPBasicAuth(
            user, password) if user else None
        self.token = token or None

    def extract_image_info(self, image):
        """
        :param image: [registry-prefix/]image[:tag]
        :returns: registry-prefix or None, image, tag or None
        """
        logger.debug('extract_image_info({})'.format(image))
        tag = None
        if ':' in image:
            image, tag = image.split(':')
        prefix = None
        if image.startswith(self.prefix):
            _, image = image.split(self.prefix)
            prefix = self.prefix
        logger.debug('\textracted: {} {} {}'.format(prefix, image, tag))
        return prefix, image.strip('/'), tag

    def get_tags(self, image):
        """
        :param image: the image without registry prefix or tags
        :returns: (list) the tags
        """
        headers = {}
        if self.token:
            headers['Authorization'] = 'Bearer {}'.format(self.token)
        r = requests.get(
            '{url}/v2/{image}/tags/list'.format(url=self.url, image=image),
            auth=self.auth, headers=headers)
        if r.status_code not in (200, ):
            msg = 'Request for {image} tags returned status code {status_code}'
            raise DockerRegistryClientException(
                msg.format(image=image, status_code=r.status_code))
        return r.json()['tags']

    def get_layers(self, image, tag):
        """
        :param image: the image, without prefix or tags
        :param tag: the image tag
        :returns: the list of layers
        """
        headers = {
            'Accept': 'application/vnd.docker.distribution.manifest.v2+json'}
        if self.token:
            headers['Authorization'] = 'Bearer {}'.format(self.token)
        req_url = '{url}/v2/{image}/manifests/{tag}'.format(
            url=self.url, image=image, tag=tag)
        r = requests.get(req_url, auth=self.auth, headers=headers)
        if r.status_code not in (200, ):
            msg = 'Request for {image} layers returned status code {status}'
            raise DockerRegistryClientException(msg.format(
                image=image, status=r.status_code))
        return r.json()['layers']


if __name__ == '__main__':
    # prefix = 'snf-773633.vm.okeanos.grnet.gr'
    # img = '{}openminted/omtd-component-executor-uima:2.10'.format(prefix)
    # user, password = '', ''
    # dr = DockerRegistryImageClient(prefix, user, password)
    # _, image, tag = dr.extract_image_info(img)
    # tags = dr.get_tags(image)
    # if tag not in tags:
    #     print('Tag {tag} not in tag list {tags}'.format(tag=tag, tags=tags))
    # else:
    #     layers = dr.get_layers(image, tag)
    #     print(sum(map(lambda x: x['size'], layers)) // (1024*1024))
    img = 'google/cadvisor:latest'
    from docreg.auth import DockerRegistryAuthClient
    auth = DockerRegistryAuthClient()
    token = auth.get_token(scope='repository:google/cadvisor:*'.format(img))
    dr = DockerRegistryImageClient(token=token)
    _, image, tag = dr.extract_image_info(img)
    print(dr.get_tags(image))
    print(dr.get_layers(image, tag))
