# Discord GPT-3 Bot

This code sets up a bot for the Discord chat platform using the discord.py library with slash-commands.

## How to use

To use this bot, use `/ask`. The bot will send a request to the OpenAI API to generate a response based on the prompt you provide.

The message the user feeds into the bot is checked against the OpenAI moderation API to ensure that it is appropriate. If the message the user posted is flagged as inappropriate, the bot sends a message indicating that it cannot respond.

Otherwise, it sends the generated response to the user. The API key for both OpenAI services are NOT provided in the code and will need to be put in by the user. The bot token will also need to be added by the user, as it is linked directly to their discord bot.

## Installation

Before running the bot, you will need to install necessary dependencies, which can be installed using:

```sh
pip install -r requirements.txt
```

## Configuration

Before running the bot, you will need to configure **[config.json]('./config.json)** with the following data:

* Discord bot token
* OpenAI API key
* Path for message logging

## Running the bot

To run the bot, use the following command:

```sh
cd /path/to/Discord-GPT3-Bot
python GPTBot.py
```

This will start the bot and allow it to listen for commands and generate responses.

## License

* **[MIT License]('./LICENSE)**