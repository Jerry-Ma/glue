import os
import imp

def identity(x):
    return x

def default_config():
    import glue.qt

    result = {
        'qt_clients' : [glue.qt.ScatterWidget,
                        glue.qt.ImageWidget],

        'link_functions' : [identity]
    }

    return result

def load_configuration():
    '''
    Read in configuration settings from a config.py file.

    Search order:

     * current working directory
     * environ var GLUERC
     * HOME/.glue/config.py
    '''
    config = _load_config_file()

    # Populate a configuration dictionary
    config_dict = default_config()
    for key in config_dict.keys():
        try:
            config_dict[key] = getattr(config, key)
        except AttributeError:
            pass

    return config_dict

def _load_config_file():
    ''' Find and import a config.py file

    Returns
    -------
    The module object, or None if no file found
    '''
    search_order = [os.path.join(os.getcwd(), 'config.py')]
    if 'GLUERC' in os.environ:
        search_order.append(os.environ['GLUERC'])
    search_order.append(os.path.expanduser('~/.glue/config.py'))

    config = None
    for config_file in search_order:
        # Load the file
        try:
            config = imp.load_source('config', config_file)
            return config
        except IOError:
            pass
        except Exception as e:
            raise Exception("Error loading config file %s:\n%s" %
                            (config_file, e))
