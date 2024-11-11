import discord
from discord.ext import commands
import os
import random
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

# Start the web server in a separate thread
Thread(target=run).start()

SPECIFIC_CHANNEL_ID = 1303119535401861181

words = ["vagina","penis","pussy","dick","bum","asshole","cheeks","freak","freaky","freaker" or "boobs","tits","tit","boob","breasts","breast"]

responses = [
  "Everybody lies.",
  "I don't ask why patients lie, I just assume they all do.",
  "It's a basic truth of the human condition that everybody lies. The only variable is about what.",
  "Truth begins in lies.",
  "I've found that when you want to know the truth about someone that someone is probably the last person you should ask.",
  "You want to know how two chemicals interact, do you ask them? No, they're going to lie through their lying little chemical teeth. Throw them in a beaker and apply heat.",
  "...like the philosopher Jagger once said, 'You can't always get what you want.'",
  "Humanity is overrated.",
  "Reality is almost always wrong.",
  "We all make mistakes, and we all pay a price.",
  "...there's no I in 'team'. There is a me, though, if you jumble it up.",
  "Everybody does stupid things, it shouldn't cost them everything they want in life." ,
  "People like talking about people. Makes us feel superior. Makes us feel in control. And sometimes, for some people, knowing some things makes them care.",
  "Men are pigs. [They will] pretty much have sex with anyone, fat, skinny, married, single, complete strangers, relatives.",
  "I choose to believe that the white light people sometimes see... they're all just chemical reactions that take place when the brain shuts down.... There's no conclusive science. My choice has no practical relevance to my life, I choose the outcome I find more comforting.... I find it more comforting to believe that this isn't simply a test.",
  "It's been established that time is not a rigid construct.",
  "It's one of the great tragedies of life — something always changes.",
  "I was never that great at math, but next to nothing is higher than nothing, right?",
  "We treat it. If she[he] gets better we know that we're right.",
  "Our bodies break down, sometimes when we're 90, sometimes before we're even born, but it always happens and there's never any dignity in it. I don't care if you can walk, see, wipe your own ass. It's always ugly. Always. You can live with dignity, we can't die with it.",
  "I solved the case, my work is done.",
  "Patients always want proof, we're not making cars here, we don't give guarantees." ,
  "...treating illnesses is why we became doctors, treating patients is what makes most doctors miserable.",
  "Tests take time. Treatment's quicker.",
  "Pretty much all the drugs I prescribe are addictive and dangerous.",
  "Patients sometimes get better. You have no idea why, but unless you give a reason they won't pay you. Anybody notice if there's a full moon? ... let's rule out the lunar god and go from there.",
  "Occam's Razor.� The simplest explanation is almost always somebody screwed up.",
  "Never met a diagnostic study I couldn't refute.",
  "I take risks, sometimes patients die. But not taking risks causes more patients to die, so I guess my biggest problem is I've been cursed with the ability to do the math.",
  "Never trust doctors.",
  "That's a catchy diagnosis, you could dance to that.",
  "Idiopathic, from the Latin meaning we're idiots cause we can't figure out what's causing it.",
  "If he gets better, I'm right, if he dies, you're right.",
  "Tragedies happen.",
  "Weird works for me.",
  "In case I'm wrong. It has happened.",
  "It does tell us something. Though I have no idea what.",
  "I hurt my leg. I have a note.",
  "The eyes can mislead, the smile can lie, but the shoes always tell the truth.",
  "Hang up a shingle and condemn the narrowness and greed of Western medicine, you'd make a damn fine living.",
  "It is the nature of medicine that you are going to screw up.",
  "Right and wrong do exist. Just because you don't know what the right answer is — maybe there's even no way you could know what the right answer is — doesn't make your answer right or even okay. It's much simpler than that. It's just plain wrong.",
  "On average, drug addicts are stupid.... I believe drug addicts get sick. Actually, for some reason they tend to get sick more often than non-drug addicts.",
  "You know what's worse than useless? Useless and oblivious." ,
  "It is in the nature of medicine that you are gonna screw up. You are gonna kill someone. If you can't handle that reality, pick another profession. Or finish medical school and teach.",
  "Tell a surgeon it's okay to cut a leg off and he's going to spend the night polishing his good hacksaw.... they care about their patients. They just care about themselves more. Which is not an unreasonable position. Trying to maximize the tissue you save also maximizes the chances of something going wrong. Which means you've gotta be extra careful. Which is such a pain in the ass.",
  "If it works, we're right. If he dies, it was something else.",
  "Everything we do is dictated by motive.",
  "If her DNA was off by one percentage point she'd be a dolphin.",
  "Welcome to the end of the thought process.",
  "Sometimes we can't see why normal isn't normal.",
  "You want to make things right? Too bad. Nothing's ever right.",
  "New is good. Because old ended in death.",
  "There is not a thin line between love and hate. There is --- in fact --- a Great Wall of China with armed sentries posted every 20 feet between love and hate.",
  "The most successful marriages are based on lies.",
  "All of those clever reasons were wrong.",
  "...the answer...to life itself: Sex.",
  "...the fact that the sexual pleasure center of your cerebral cortex has been over-stimulated by spirochetes is a poor basis for a relationship. Learned that one the hard way.",
  "...there's no I in 'team'. There is a me, though, if you jumble it up.",
  "You could think I'm wrong, but that's no reason to stop thinking?",
  "And humility is an important quality. Especially if you're wrong a lot.... Of course, when you're right, self-doubt doesn't help anybody, does it?",
  "Read less, more TV.",
  "There's an evolutionary imperative why we give a crap about our family and friends. And there's an evolutionary imperative why we don't give a crap about anybody else. If we loved all people indiscriminately, we couldn't function.",
  "If you can fake sincerity, you can fake pretty much anything.",
  "Welcome to the world. Everyone's different, everyone gets treated different. You try fighting that, you end up dying of TB.",
  "What usually happens when you poke something with a stick? It pokes back.",
  "In this universe effect follows cause. I've complained about it but—",
  "The only problem with that theory is it's based on the assumption that the universe is a just place.",
  "You know me. Hostility makes me shrink up like a— I can't think of a non-sexual metaphor.",
  "Dying people lie too. Wish they'd worked less, been nicer, opened orphanages for kittens. If you really want to do something, you do it. You don't save it for a sound bite.",
  "Mistakes are as serious as the results they cause!",
  "Anomalies bug me.",
  "If you talk to God you're religious. If God talks to you, you're psychotic.",
  "There's nothing in this universe that can't be explained. Eventually.",
  "Saying there appears to be some clotting is like saying there's a traffic jam ahead. Is it a ten-car pile up, or just a really slow bus in the center lane? And if it is a bus, is that bus thrombotic or embolic? I think I pushed the metaphor too far.",
  "A psychic once told me that I'm psychic.",
  "Arrogance has to be earned.",
  "The treatments don't always work. Symptoms never lie.",
  "This vexes me."
]

intents = discord.Intents.default()
intents.message_content = True  # Required to read message content

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  user_id = 803394550365290508  # Replace with the actual user ID
  user = bot.get_user(user_id)

  if "vicodin" in message.content.lower():
      await message.channel.send(file=discord.File('house1.jpg'))

  if "house" in message.content.lower():
    await message.channel.send(file=discord.File('house2.jpg'))

  if "rectum" in message.content.lower():
      await message.channel.send(file=discord.File('house6.jpg'))

  if "lupus" in message.content.lower():
    await message.channel.send(file=discord.File('house7.jpg'))

  if "vexes" in message.content.lower():
    await message.channel.send(file=discord.File('house3.jpg'))

  if "infarction" in message.content.lower():
    await message.channel.send(file=discord.File('house5.jpg'))

  if "ass" in message.content.lower():
    await message.channel.send("Do you have hair in your special place?")

  if "hospital" in message.content.lower():
    await message.channel.send("https://youtu.be/ry-Z6_yfZoE?si=U619gpfD57QQq2KL")

  if any(word.lower() in message.content.lower() for word in words):
    await message.channel.send(file=discord.File('house4.jpg'))
    
  if "meow" in message.content.lower():
    await message.channel.send({user.mention})
  
  # Check if the message is in the specified channel
  if message.channel.id == SPECIFIC_CHANNEL_ID and message.content.endswith("?"):
    # Randomly select True or False
    response = random.choice(["Yes", "No"])
    await message.channel.send(response)
  
  elif message.channel.id == SPECIFIC_CHANNEL_ID:
    # Check for keywords or just respond to any message in this channel
    await message.channel.send(random.choice(responses))
  
  await bot.process_commands(message)

# Run the bot with the token stored in environment variables
bot.run(os.getenv("DISCORD_BOT_TOKEN"))