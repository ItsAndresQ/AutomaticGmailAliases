import discord
import os
from discord.ext import commands
from up_time_robot import alive

my_secret = os.environ['TOKEN']
client = commands.Bot(command_prefix='$')
client.remove_command('help')


@client.event
async def on_ready():
    print('---------------------------------------')
    print('{0.user} is working!'.format(client))
    print('---------------------------------------')
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game('Just Us'))

@client.event
async def on_command_error(ctx, issue):
    if isinstance(issue, commands.CommandNotFound):
        await ctx.send(
            'That command is not recognized. Please type $help check what commands are available and try again.')


@client.command(aliases=['l'])
async def load(ctx, extension):
    client.load_extension(f'commands.{extension}')
    await ctx.send('Extension loaded!')

@client.command(aliases=['ul'])
async def unload(ctx, extension):
    client.unload_extension(f'commands.{extension}')
    await ctx.send('Extension unloaded!')

@client.command(aliases=['rl'])
async def reload(ctx, extension):
    client.unload_extension(f'commands.{extension}')
    client.load_extension(f'commands.{extension}')
    await ctx.send('Extension reloaded!')

@load.error
async def load_error(ctx, error):
    await ctx.send('Please specify an extension to load!')

@unload.error
async def unload_error(ctx, error):
    await ctx.send('Please specify an extension to unload!')


@reload.error
async def reload_error(ctx, error):
    await ctx.send('Please specify an extension to reload!')

for filename in os.listdir('./commands'):
  if filename.endswith('.py'):
      client.load_extension(f'commands.{filename[:-3]}')


# Stop Bot
#@client.command()
#async def stop(ctx):
 #   await ctx.send('Stopping bot.')
  #  print('Stopping bot.')
   # await client.close()

alive()
client.run(my_secret)
