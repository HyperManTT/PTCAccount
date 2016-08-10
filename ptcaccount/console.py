import argparse
import sys

from ptcaccount import *
from ptcaccount.ptcexceptions import *


def parse_arguments(args):
    """Parse the command line arguments for the console commands.

    Args:
      args (List[str]): List of string arguments to be parsed.

    Returns:
      Namespace: Namespace with the parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description='Pokemon Trainer Club Account Creator'
    )
    parser.add_argument(
        '-u', '--username', type=str, default=None,
        help='Username for the new account (defaults to random string).'
    )
    parser.add_argument(
        '-p', '--password', type=str, default=None,
        help='Password for the new account (defaults to random string).'
    )
    parser.add_argument(
        '-e', '--email', type=str, default=None,
        help='Email for the new account (defaults to random email-like string).'
    )
    parser.add_argument(
        '-m', '--multiple', type=int, default=1,
        help='Create multiple accounts at once (defaults to 1)'
    )
    parser.add_argument(
        '--compact', action='store_true',
        help='Compact the output to "username:password"'
    )
    parser.add_argument(
        '--email-tag', action='store_true',
        help='Add the username as a tag to the email (i.e addr+tag@mail.com).'
    )
    return parser.parse_args(args)


def entry():
    """Main entry point for the package console commands"""
    args = parse_arguments(sys.argv[1:])
    try:
        print('Creating new account(s):')
        for _ in range(args.multiple):
            # Create the random account
            account_info = random_account(
                args.username, args.password, args.email, args.email_tag
            )

            if args.compact:
                print('{}:{}'.format(account_info[USERNAME], account_info[PASSWORD]))
            else:
                print('  Username:  {}'.format(account_info[USERNAME]))
                print('  Password:  {}'.format(account_info[PASSWORD]))
                print('  Email   :  {}'.format(account_info[EMAIL]))
                print('\n')


    # Handle account creation failure exceptions
    except PTCInvalidPasswordException as err:
        print('Invalid password: {}'.format(err))
    except (PTCInvalidEmailException, PTCInvalidNameException) as err:
        print('Failed to create account! {}'.format(err))
    except PTCException as err:
        print('Failed to create account! General error:  {}'.format(err))
