from discord.ext import commands
import discord
import random

class Gmail(commands.Cog):
    def __init__(self, bot):
      self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print("Gmail Deals Cog Loaded Succesfully")
        print('---------------------------------------')

    @commands.command(aliases=['g', 'mail'])
    async def gmail(self, ctx, *, email, entry):
        list_emails = open("commands.email_text.emails.txt").read().split()
        gmail_domain = '@gmail.com'
      
        if entry:
          if entry > 30:
            entry = 30
          finished_email = ""
       
          file = open("commands.emailgenerated.txt", "w+")
          for i in range(entry):
            ran_email= random.choice(list_emails)
            finished_email = email+ran_email+gmail_domain+"\n"
            file.write(finished_email)
          file.close()
          print("+gmail was generated successfully!")
          await ctx.send(file=discord.File("commands.emailgenerated"))

    @gmail.error
    async def gmail_error(self, ctx, error):
      await ctx.send('Type /gmail is a bot that uses the gmail + trick to generate random gmail addresses\nBy simply adding a + to the end of your username you can create infinite variations of your gmail address.\n***Example: +gmail email@gmail.com 25***')

def setup(client):
    client.add_cog(Gmail(client))
