import discord

client = discord.Client()
channels = []

@client.event
async def on_ready():
    channels = [c for c in client.get_all_channels()]
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$yey'):
        await message.channel.send('イェイ')

    if message.content.startswith('$users'):
        await message.channel.send(client.users)

    if message.content.startswith('$allc'):
        channels = [c for c in client.get_all_channels()]
        print(channels)
        await message.channel.send(channels)
        

    if message.content.startswith('$guilds'):
        for c in client.get_all_channels():
            await message.channel.send(client.guilds)

@client.event
async def on_member_update(before, after):
    if before.activity != after.activity:
        if type(after.activity) == discord.Activity or type(before.activity) == discord.Activity:
            return
        print('on_member_update')
        print(before.display_name)
        print(before.activity, '->', after.activity)

        message = str(before.display_name) + ' playing ' + str(after.activity)
        channels = [c for c in client.get_all_channels()]
        for c in channels:
            if c.id == 494177568186957840:
                await c.send(message)

client.run(os.getenv('DISCORD_TOKEN'))
