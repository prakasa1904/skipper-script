"""
skipper

Usage:
  skipper deploy
  skipper feature list

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  skipper deploy feature

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/prakasa1904/skipper-script

Original:
  For original source please open an issue on the Github repository:
  https://github.com/rdegges/skele-cli
"""


from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION


def main():
    """Main CLI entrypoint."""
    import skipper.commands
    options = docopt(__doc__, version=VERSION)

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for (k, v) in options.items(): 
        if hasattr(skipper.commands, k) and v:
            module = getattr(skipper.commands, k)
            skipper.commands = getmembers(module, isclass)
            command = [command[1] for command in skipper.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()
