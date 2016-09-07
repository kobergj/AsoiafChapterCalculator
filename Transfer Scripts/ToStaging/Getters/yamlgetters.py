import yaml

import basicgetters as bsc

class YamlGetter(bsc.BasicGetter):
    def _connect(self, filename):
        with open(filename, "r") as opened:
            yamlfile = yaml.load(opened)

        def getinfo(key=None):
                return yamlfile[key]

        return getinfo

