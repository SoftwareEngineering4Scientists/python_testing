import yaml

with open("yaml_ex.yml", "r") as yml_file:
    contents = yaml.full_load(yml_file)
    print(type(contents))
    print(contents.keys())
    print(contents['multi'])