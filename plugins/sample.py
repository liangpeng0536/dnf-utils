#    dnf-utils - add-on tools for DNF
#    Copyright (C) 2014 Tim Lauridsen < timlau<AT>fedoraproject<DOT>org >
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

from dnfutils import logger, _, ArgumentParser

import dnf
import dnf.cli
import dnf.exceptions


# TODO: dnf Plugin class, rename to your <Command>
class Sample(dnf.Plugin):

    # TODO: Use your own command name here
    name = 'sample'

    def __init__(self, base, cli):
        self.base = base
        self.cli = cli
        logger.debug('Initialized %s plugin' % self.name)
        if self.cli is not None:
            # TODO: use your own <Command>Command class here
            self.cli.register_command(SampleCommand)


# TODO: dnf Command class, rename to your <Command>Command
class SampleCommand(dnf.cli.Command):
    """ the util command there is extending the dnf command line """

    # TODO: the tool command, use your own command
    aliases = ['sample']

    # TODO: summary for util, shown in dnf help, add your own
    summary = _('One line description of the util')
    # TODO usage string for the util, shown by dnf help <command>
    usage = _('[PARAMETERS]')

    def configure(self, args):
        demands = self.cli.demands
        # make dnf setup the sack
        demands.sack_activation = True

    def run(self, args):
        ''' execute the util action here '''
        logger.debug('Command sample : run')
        # Setup ArgumentParser to handle util
        # You must only add options not used by dnf already
        self.parser = ArgumentParser(prog='dnf ' + self.aliases[0])
        # a help-<command> is required for every tool
        # TODO: rename to your command
        self.parser.add_argument("--help-sample", action='store_true',
                                 help=_('show this help about query tool'))

        # TODO: example options/arg add your own
        self.parser.add_argument("cmd", nargs=1, help='the sub command')
        self.parser.add_argument("parms", nargs='*',
                            help='the parameters to the sub command')
        self.parser.add_argument("--some-option", action='store_true',
                            help='an optional option')

        # parse the options/args
        # list available options/args on errors & exit
        try:
            opts = self.parser.parse_args(args)
        except AttributeError as e:
            print(self.parser.format_help())
            raise dnf.exceptions.Error(str(e))

        # TODO: a help-<command> is required for every tool
        if opts.help_sample:
            print(self.parser.format_help())
            return 0, ''

        # TODO: the main tool code, add your own
        print('Sample util is running with :')
        print('    cmd =       : %s' % opts.cmd)
        print('    parms =     : %s' % opts.parms)
        print('    some-option : %s' % opts.some_option)

        return 0, ''
