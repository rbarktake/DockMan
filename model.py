import json

from docker import Client
CONSTANTS = { 'CONNECTION_URL': 'unix://var/run/docker.sock' }

class DockerInfo(object):

    def __init__(self):
        client = Client(base_url=CONSTANTS['CONNECTION_URL'])
        self.images = client.images()
        self.containers = client.containers(all=True, size=True)
        self.volumes = client.volumes()
        self.networks = client.networks()
        self.version = client.version()
        self.info = client.info()
        #self.datetime =
        pass

    def getImages(self):
        return self.images

    def getImageCount(self):
        return len(self.images)

    def getContainers(self):
        return self.containers

    def getContainerCount(self):
       return (self.info['Containers'])

    def getInfo(self):
        return json.loads(self.getPretty(self.info))

    def getHostName(self):
        return (self.info['Name'])
    
    def getHostOS(self):
        return (self.info['OperatingSystem'])
    
    def getHostVersion(self):
        return (self.info['ServerVersion'])

    def getRunningContainerCount(self):
        return (self.info['ContainersRunning'])

    def getVolumes(self):
        return self.volumes

    def getVolumeCount(self):
        return len(self.volumes)

    def getNetworks(self):
        return self.networks

    def getNetworkCount(self):
        return len(self.networks)
    
    def getPretty(self, obj):
        #return json.dump(obj, sort_keys=True, indent=4, separators=(',', ': '))
        return json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))

if __name__ == "__main__":
    cli = Client(base_url='unix://var/run/docker.sock')
    #print(len(cli.images()))
    #print(cli.containers(all=True))
    dc = DockerInfo()
    #print(len(dc.getImages()))
    #print(dc.getImages())
    #print(dc.getVolumes())
    #print(dc.getPretty(dc.getNetworks()))
    #print(dc.getImageCount())
    #print(dc.getContainerCount())
    #print(cli.info())
    print(dc.getPretty(dc.getInfo()))    
    #for key,value in dc.getInfo():
    #    print str(key) + ":" + str(value)
    
    #print(cli.version())



#images = [{u'Created': 1459458535, u'Labels': {}, u'VirtualSize': 125, u'ParentId': u'', u'RepoTags': [u'tianon/true:latest'], u'RepoDigests': None, u'Id': u'sha256:3ddfc220a32e9cd60c9cbe0de8f58c9d8d21a3919ebdfbc7010bf2e0eab39849', u'Size': 125}, {u'Created': 1459283369, u'Labels': {}, u'VirtualSize': 321278746, u'ParentId': u'sha256:26aaa17731f02b0da6b06feca380567cd3d56b2a7c4819d2b98fab96d3c9965d', u'RepoTags': [u'dockerelk_kibana:latest'], u'RepoDigests': None, u'Id': u'sha256:66173a68487c44023da42fa3357056f4840cb9c594738fb5df05b89763872158', u'Size': 321278746}, {u'Created': 1459122871, u'Labels': {}, u'VirtualSize': 48441985, u'ParentId': u'', u'RepoTags': [u'kanboard/kanboard:stable'], u'RepoDigests': None, u'Id': u'sha256:570103e275266460d1734064ac7efcab81caeac79884ff026e861f9c791d84aa', u'Size': 48441985}, {u'Created': 1458847847, u'Labels': {}, u'VirtualSize': 408816392, u'ParentId': u'', u'RepoTags': [u'beevelop/taiga-back:latest'], u'RepoDigests': None, u'Id': u'sha256:432ed1bf795cae4aea809dd73eb8598b7ad195e8fe83ddf101f98504ff532474', u'Size': 408816392}, {u'Created': 1458579554, u'Labels': {}, u'VirtualSize': 111619186, u'ParentId': u'', u'RepoTags': [u'beevelop/taiga-front:latest'], u'RepoDigests': None, u'Id': u'sha256:1d05a62f1877cc2cffe783c723cfa59d8a65ab81855cf2a54a49e9859dda1711', u'Size': 111619186}, {u'Created': 1458146718, u'Labels': {}, u'VirtualSize': 264567018, u'ParentId': u'', u'RepoTags': [u'postgres:latest'], u'RepoDigests': None, u'Id': u'sha256:dbc8c4900ce5bcfe7152fedbb4e52d71709b47b4016edf189a4ceba13b65aa4b', u'Size': 264567018}, {u'Created': 1458079152, u'Labels': {}, u'VirtualSize': 347106701, u'ParentId': u'', u'RepoTags': [u'elasticsearch:latest'], u'RepoDigests': None, u'Id': u'sha256:51340b3eab019ea2fd34eb9a8b71f1b9ada06e34ca9451210f4b1c1d267c5470', u'Size': 347106701}, {u'Created': 1458068617, u'Labels': {}, u'VirtualSize': 451348809, u'ParentId': u'', u'RepoTags': [u'logstash:latest'], u'RepoDigests': None, u'Id': u'sha256:1b59d252ce642570e3399afaf1098223a9517ccfe8f1a7f88f5b39fb2245c4a0', u'Size': 451348809}, {u'Created': 1457737572, u'Labels': {}, u'VirtualSize': 295451889, u'ParentId': u'', u'RepoTags': [u'kibana:latest'], u'RepoDigests': None, u'Id': u'sha256:2d8d26d280d3333928fcb9228fc0b239fe53432a4dade9f9a8e48a8104068dab', u'Size': 295451889}, {u'Created': 1444780068, u'Labels': None, u'VirtualSize': 960, u'ParentId': u'', u'RepoTags': [u'hello-world:latest'], u'RepoDigests': None, u'Id': u'sha256:690ed74de00f99a7d00a98a5ad855ac4febd66412be132438f9b8dbd300a937d', u'Size': 960}]