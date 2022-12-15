# Discord GPT-3 Bot

This code sets up a bot for the Discord chat platform using the discord.py library. The bot responds to commands that begin with /, such as /ask. When the /ask command is used, the bot sends a request to the OpenAI API to generate a response based on the provided prompt. The message the user feeds into the bot is checked against the OpenAI moderation API to ensure that it is appropriate. If the message the user posted is flagged as inappropriate, the bot sends a message indicating that it cannot respond. Otherwise, it sends the generated response to the user. The API key for both OpenAI services are NOT provided in the code and will need to be put in by the user. The bot token will also need to be added by the user, as it is linked directly to their discord bot.

You will need to install the following packages using the CLI:

pip install discord.py, 
pip install openai
