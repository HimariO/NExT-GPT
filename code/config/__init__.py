import os
import yaml

HERE = os.path.dirname(__file__)


def load_model_config(stage, mode):
    # load special config for each model
    config_path = os.path.join(HERE, f'stage_{stage}.yaml')
    print(f'[!] load configuration from {config_path}')
    with open(config_path) as f:
        configuration = yaml.load(f, Loader=yaml.FullLoader)
        new_config = {}
        for key, value in configuration.items():
            if key in ['train', 'test', 'validation']:
                if mode == key:
                    new_config.update(value)
            else:
                new_config[key] = value
        configuration = new_config
    return configuration


def load_config(args):
    '''the configuration of each model can rewrite the base configuration'''
    # base config
    base_configuration = load_base_config()

    # load stage config
    # if args.get('mode'):
    stage_configuration = load_model_config(args['stage'], args.get('mode', "test"))

    # update and append the stage config for base config
    base_configuration.update(stage_configuration)
    configuration = base_configuration
    return configuration


def load_base_config():
    config_path = os.path.join(HERE, f'base.yaml')
    with open(config_path) as f:
        configuration = yaml.load(f, Loader=yaml.FullLoader)
    print(f'[!] load base configuration: {config_path}')
    return configuration
