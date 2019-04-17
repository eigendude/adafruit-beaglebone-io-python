# Adafruit Setuptools Configuration Module
# SPDX-License-Identifier: MIT

try:
  import configparser
except ImportError:
  # Python 2 compatibility
  import ConfigParser as configparser

class Adafruit_Config:
  """
  Class to obtain configuration provided by the setup.cfg configuration file
  used by setuptools.

  Adafruit-specific information is provided under an [adafruit] section.

  The reason for this interface is that the command-line to the setup.py
  script is out of our control and entirely up to the installer. The
  setup.cfg file was added to setuptools as a useful middle-ground between
  modifying the setup script and the command-line to the setup script.
  """

  #############################################################################
  # Parameters
  #############################################################################

  # Setuptools config file
  SETUPTOOLS_CONFIG_FILE = 'setup.cfg'

  # Section name in cfg file
  SECTION_NAME = 'adafruit'

  # Key name for specifying kernel >= 4.1.0 targets. Value must be 'true' to
  # target the newer kernel interface or 'false' to target the older one.
  KERNEL41_KEY = 'kernel41'

  #############################################################################
  # Interface
  #############################################################################

  def __init__(self):
    """
    Initialize the configuration object.
    """
    self._metadata = self.metadata_from_setupcfg(self.SECTION_NAME)

  def is_kernel41(self):
    """
    Return True if we are targeting a kernel >= 4.1.0, or False otherwise.
    Defaults to True if unknown.
    """
    return False if self.get_cfg_value(self.KERNEL41_KEY) == 'false' else True

  #############################################################################
  # Helpers
  #############################################################################

  def get_cfg_value(self, key):
    """
    Get a value associated with a key in the Adafruit section. Returns the
    value, or None if unknown.
    """
    return self._metadata.get(key, None)

  @classmethod
  def metadata_from_setupcfg(cls, section_name):
    """
    Read the [adafruit] section of setup.cfg and return it as a dict.
    """
    cfgparser = configparser.ConfigParser()
    cfgparser.read(cls.get_cfg_fname())

    return dict(cfgparser.items(section_name))

  @classmethod
  def get_cfg_fname(cls):
    """
    Get the name of the setuptools cfg file.
    """
    return cls.SETUPTOOLS_CONFIG_FILE
