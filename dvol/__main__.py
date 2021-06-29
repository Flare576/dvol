#!/usr/local/bin/python3
# TODO: when `get` is called, always show override, but mark as disabled if container isn't curently using it
# TODO: when config set with -p but no other params, clear it?
# TODO: when removing, should loop through existing mappings, delete those folders, then nuke the root/project folder
# TODO: after removing files, recursivly delete empty folders upward

import cli

def main ():
    cli.dispatch()

if __name__ == '__main__':
    main()
