import configparser, os
from Selunium_Automation.Lib.LogConfig import Logger


def ReadMapSection(section, file):
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../Utilities/' + file + '.ini'))
    dictionary = {}
    try:
        options = config.options(section)
    except configparser.NoSectionError:
        # print("test")
        Logger.logr.error("Section " + section + " does not exist")
    else:
        for option in options:
            dictionary[option] = config.get(section, option)
        return dictionary


def WriteMapSection(key, value):
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../Utilities/ResultLog.ini'))
    try:
        config.set('ResultSet', 'lasttestresult', value)
        config.set('ResultSet', key, value)
    except configparser.NoSectionError:
        Logger.logr.error("Section ResultSet or Result does not exist")
    else:
        with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../Utilities/ResultLog.ini'),
                  'w') as configfile:
            config.write(configfile)
            configfile.close()


def InitializeMapSection(section, file):
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../Utilities/' + file + '.ini'))
    dictionary = {}
    try:
        options = config.options(section)
    except configparser.NoSectionError:
        Logger.logr.error("Section ResultSet or Result does not exist")
    else:
        for index in range(len(options)):
            config.set(section, options[index], 'None')
        with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../Utilities/' + file + '.ini'),
                  'w') as configfile:
            config.write(configfile)
            configfile.close()

# def TestResult(method):
#     def wrapper_func(*args, **kwargs):
#         Errored, Failed, Passed = (method(*args, **kwargs))
#         if Errored:
#             Logger.logr.info(" ******* TestCase Status: Errored ******* ")
#         elif Failed:
#             Logger.logr.info(" ******* TestCase Status: Failed ******* ")
#         else:
#             Logger.logr.info(" ******* TestCase Status: Passed ******* ")
#
#     return wrapper_func
