import argparse

from commands import main, config, add, remove, get, enable, disable

def dispatch ():
    main_p = main.create()
    subs = main_p.add_subparsers(title = 'subcommands')

    add.create(subs)
    config.create(subs)
    remove.create(subs)
    enable.create(subs)
    disable.create(subs)

    try:
        args = main_p.parse_args()
        args.func(**vars(args))
    except Exception as uh_oh:
        print("Error: ", uh_oh)
        main.parse_args(['--help'])
