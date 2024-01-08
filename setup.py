#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Standard library import
import json
from typing import NoReturn


def main() -> NoReturn:
    """
    Function to make credential for bot

    Returns:
        None (typing.NoReturn)
    """
    # Set account credential
    try:
        with open("credential.json", "w") as data:
            # Get API-ID and API-Hash from user
            api_id: int = int(input(":: Enter API ID: "))
            api_hash: str = input(":: Enter API Hash: ")

            # Send confirmation prompt
            if input("  Continue? [or send Ctrl+C] ") == "":
                # Dump data to credential file
                json.dump({
                    "api_ID": api_id,
                    "api_Hash": api_hash
                    }, data, indent=4
                )
                
                # Print success message
                print(":: Credential file created at credential.json\n  run main.py to create session!")

    # Handle keyboard interrupt
    except KeyboardInterrupt:
        raise SystemExit("  Keyboard Interrupt received.")

    # Handle value error
    except ValueError:
        raise SystemExit("  Value error: API-ID must be integer!")


if __name__ == '__main__':
    main()