from textwrap import dedent

from west.commands import WestCommand

from tools.addr2src import addr2src


class DebugTools(WestCommand):
    def __init__(self):
        super().__init__(
            "dbt",
            "Convenient debugging tools.",
            dedent(
                """
                dbt is a collection of tools that make debugging Zephyr
                applications more convenient.
                """
            ),
        )

    def do_add_parser(self, parser_adder):
        parser = parser_adder.add_parser(
            self.name, help=self.help, description=self.description
        )
        subparsers = parser.add_subparsers(
            metavar="<subcommand>",
            dest="subcommand",
            help="Select a subcommand.",
        )
        addr2src_parser = subparsers.add_parser(
            "addr2src",
            help="Emit file, line number, and source for address.",
            epilog=dedent(
                """
                Emits the file path, line number, and source at the specified
                address.
                """
            ),
        )
        addr2src_parser.add_argument("address", help="Instruction address.")

        return parser

    def do_run(self, args, unknown_args):
        cmd = addr2src(self.topdir, self.config.get("zephyr.base"), args.address)
        self.check_call(cmd, **{})
