import discord
import random
from discord.ext import commands

class Dad(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['funny'])
    async def dadjoke(self, ctx):
        dadjokes = ['What did the drummer call his twin daughters? Anna one, Anna two!',
                    'How did Darth Vader know what Luke got him for Christmas? He felt his presents!',
                    "Did you hear about the chameleon who couldn't change color? He had a reptile dysfunction.",
                    'I wanted to go on a diet, but I feel like I have way too much on my plate right now.',
                    "Want to hear a joke about construction? I'm still working on it.",
                    'What’s Forrest Gump’s password? 1forrest1',
                    'What sound does a witches car make? Broom Broom',
                    'To whoever stole my copy of Microsoft Office, I will find you. You have my Word!',
                    'What does a zombie vegetarian eat? “GRRRAAAIINS!”',
                    'This graveyard looks overcrowded. People must be dying to get in there.',
                    'What does a nosey pepper do? It gets jalapeno business!',
                    "I tell dad jokes, but I don't have any kids. I'm a faux pa.",
                    'Whenever the cashier at the grocery store asks my dad if he would like the milk in a bag he replies, "No, just leave it in the carton!"',
                    'Two goldfish are in a tank. One says to the other, "do you know how to drive this thing?"',
                    'What’s that Nevada city where all the dentists visit? Floss Vegas.',
                    'Atheism is a non-prophet organization.',
                    'You’re American when you go into the bathroom, and you’re American when you come out, but do you know what you are while you’re in there? European.',
                    'Why did the picture go to jail? Because it was framed.',
                    'What do you call a bear without any teeth? A gummy bear!',
                    "What do you call a hippie's wife? Mississippi.",
                    'The shovel was a ground-breaking invention.',
                    "Dad, can you put the cat out? I didn't know it was on fire.",
                    'Does anyone need an ark? I Noah guy!',
                    'How do you make holy water? You boil the hell out of it.',
                    '5/4 of people admit that they’re bad with fractions.',
                    'What do you call a man with a rubber toe? Roberto.',
                    'I would avoid the sushi if I was you. It’s a little fishy.',
                    "To the man in the wheelchair that stole my camouflage jacket... You can hide but you can't run.",
                    'What do you call a fish with two knees? A two-knee fish!',
                    "I bought some shoes from a drug dealer. I don't know what he laced them with, but I was tripping all day!",
                    'The rotation of earth really makes my day.',
                    "I thought about going on an all-almond diet. But that's just nuts.",
                    "Did you know the first French fries weren't actually cooked in France? They were cooked in Greece.",
                    'I’ve never gone to a gun range before. I decided to give it a shot!',
                    "What's black and white and goes around and around? A penguin in a revolving door."]

        await ctx.send('*{}*'.format(random.choice(dadjokes)))

def setup(client):
    client.add_cog(Dad(client))
