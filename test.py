import yaml


path  = "./"
config_file = path + 'config.yml'
print(config_file)
with open(config_file, 'rb') as f:
    config = yaml.safe_load(f)
f.close()


