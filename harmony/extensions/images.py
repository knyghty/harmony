import glob
import os

from discord.ext import commands

from conf import settings


IMAGE_DIR = os.path.join(settings.BASE_DIR, 'media', 'images')


class Image:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def i(self, image: str):
        """
        Upload an image with the given filename.

        Keyword arguments:
        filename -- File name of the file to upload
        """
        matches = glob.glob(os.path.join(IMAGE_DIR, image + '.*'))
        if len(matches) != 1:
            await self.bot.say('uwotm8')
            return

        await self.bot.upload(matches[0])



def setup(bot):
    bot.add_cog(Image(bot))
