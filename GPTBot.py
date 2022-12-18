import os
import openai
import json
import discord
from discord import app_commands

with open('./config.json') as data:
    config = json.load(data)

path = config['LOG_PATH']
openai.api_key = config['OPENAI_API_KEY']


class aclient(discord.Client):

    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()

        await self.change_presence(activity=discord.Activity(
            type=discord.ActivityType.listening,
            name='your prompts!'
        ))

        if not self.synced:
            await tree.sync()
            self.synced = True

        print('Logged in as:')
        print(f'{self.user.name}, {self.user.id}')
        print(
            'Created by Joeyy#4628. The most up-to-date code can be found on github: https://github.com/Joeya1ds/Discord-GPT3-Bot')
        print(
            '--------------------------------------------------------------------------------------------------------------------')


client = aclient()
tree = app_commands.CommandTree(client)


@tree.command(name='ask', description='Ask the AI bot a question!')
async def ask(interaction: discord.Interaction, prompt: str):
    user = interaction.user.id

    # Moderation API flagging
    moderate = openai.Moderation.create(input=prompt)
    flagged = moderate['results'][0]['flagged']

    # Logging user message functions
    def createlog():
        if not os.path.exists(f'{path}/{user}'):
            print(f'User with ID: {user} does not have a log file created. Creating.')
            os.makedirs(f'{path}/{user}')

    def userlog():
        with open(f'{path}/{user}/{user}.txt', 'a') as f:
            f.write(f'{user} wrote: "{prompt}"')

    def userlogToken():
        with open(f'{path}/{user}/{user}.txt', 'a') as f:
            f.write(f' using {openairesponse["usage"]["total_tokens"]} tokens.')

    def userlogWarn():
        with open(f'{path}/{user}/{user}.txt', 'a') as f:
            f.write(f' and was flagged by the OpenAI Moderation API!')

    def userlogNL():
        with open(f'{path}/{user}/{user}.txt', 'a') as f:
            f.write(f'\n')
    
    # Functions for generating and sending bot responses to chat messages
    if flagged:
        createlog()
        userlog()
        userlogWarn()
        userlogNL()
        await interaction.response.send_message('I cannot respond to what you have said, it has been flagged by the Moderation API.')
        print(f'User with ID: {user} has had a prompt flagged by the Moderation API. Consider checking logs.')
        return

    openairesponse = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=200,
        temperature=0.8,
        top_p=0.8,
    )

    createlog()
    userlog()
    userlogToken()
    userlogNL()
    await interaction.response.send_message(openairesponse['choices'][0]['text'])


client.run(config['DISCORD_BOT_TOKEN'])
