import random

from discord.ext import commands


class RNG:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, dice: str):
        """Roll some dice.

        Keyword arguments:
        dice -- number of dice (X) and faces (Y) in the format XdY
        """
        try:
            num_dice, num_faces = map(int, dice.split('d'))
        except Exception:
            await self.bot.say('Format is XdY!')
            return

        if num_dice not in range(1, 21) or num_faces not in range(2, 121):
            await self.bot.say('Between 1 and 20 dice of between 2 and 120 faces.')
            return

        rolls = [random.randint(1, num_faces) for _ in range(num_dice)]
        await self.bot.say(', '.join(map(str, rolls)) + ' (total {})'.format(sum(rolls)))

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
