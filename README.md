# docker-image-size

A python script to get the image size from a docker repository, without downloading the image locally. It could potentially provide more interaction with the Docker registry API v2, but at the moment it is an API library that supports only the requests we need.

version 0.1
----------
The only authentication method currently supported is username password on HTTP Auth, so it is assumed that docker registry is configured to run without its own authentication.

There is a class called "DockerRegistryImageClient" which provides a few methods.
It implies that there should be a "DockerRegistryClient" superclass, but for the time being, we keep it simple. Since we only provide a couple of image requests, there is no need for a class hierarchy.


version 0.2
-----------
Support token authentication. This allows authentication against dockerhub.