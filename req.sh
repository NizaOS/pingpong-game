#!/bin/bash

echo " Setting up Winter Ping-Pong environment..."


if ! command -v python3 &> /dev/null
then
    echo " Error: Python3 is not installed. Please install it first."
    exit
fi

echo " Installing Pygame..."
python3 -m pip install --upgrade pip
python3 -m pip install pygame

echo " Setup complete! You can now run the game using: python3 your_script_name.py"