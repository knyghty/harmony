from discord.ext import commands

import requests


class Admin:
    def __init__(self, bot):
        self.bot = bot

    # FIXME: Do something less bad.
    @commands.has_role('bot')
    @commands.command()
    async def set_avatar(self, url: str):
        r = requests.get(url, stream=True)
        image = b''.join(chunk for chunk in r.iter_content(chunk_size=128))
        await self.bot.edit_profile(avatar=image)
    
    @commands.command()
    async def meow(self):
        import discord
        await self.bot.say(embed=discord.Embed().set_image(url='https://i.imgur.com/4KotUds.jpg'))


def setup(bot):
    bot.add_cog(Admin(bot))
