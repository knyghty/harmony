from discord.ext import commands

import requests


class Admin:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def set_avatar(self, ctx, url: str):
        print(self.bot.application_info())
        if ctx.message.author == self.bot.application_info().owner:
            r = requests.get(url, stream=True)
            image = b''.join(chunk for chunk in r.iter_content(chunk_size=128))
            await self.bot.edit_profile(avatar=image)


def setup(bot):
    bot.add_cog(Admin(bot))
