import random

from discord.ext import commands


class RNG:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, dice: str = None):
        """Roll some dice.

        Keyword arguments:
        dice -- number of dice (X) and faces (Y) in the format XdY
        """

        if not dice:
            await self.bot.say('Usage: !roll XdY')
            return

        try:
            num_dice, num_faces = map(int, dice.split('d'))
        except Exception:
            await self.bot.say('Format is XdY')
            return

        if num_dice > 20 or num_faces > 1000:
            await self.bot.say('Max 20 dice and 1000 faces')
            return

        if num_dice < 1 or num_faces < 1:
            await self.bot.say('Stick to positive numbers')
            return

        total = sum((random.randrange(1, num_faces) for _ in range(int(num_dice))))
        await self.bot.say(str(total))

    @commands.command()
    async def choose(self, *choices: str):
        """
        Choose between the options

        Keyword arguments:
        choices -- Space separated list of options
        """
        await self.bot.say(random.choice(choices))


def setup(bot):
    bot.add_cog(RNG(bot))
