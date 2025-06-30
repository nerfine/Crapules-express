# main.py
import discord
from discord.ext import commands
from dotenv import load_dotenv

import os
import asyncio
import signal
import platform

load_dotenv()

token = os.getenv("DISCORD_TOKEN")
GUILD_ID = 1368272372230000711

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all(), application_id=1373334216233717840)

_shutting_down = False

@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user}')
    activity = discord.Activity(
        type=discord.ActivityType.streaming,
        name="🚧 Crapules Express 2.0",
        url="https://www.twitch.tv/nerfine"
    )
    await bot.change_presence(activity=activity)

    guild = discord.Object(id=GUILD_ID)
    try:
        synced = await bot.tree.sync(guild=guild)
        print(f"✅ Synced {len(synced)} slash command(s) to guild {GUILD_ID}.")
    except Exception as e:
        print(f"❌ Failed to sync slash commands: {e}")

    logger = bot.get_cog("BotLogger")
    changed_file = os.getenv("BOT_CHANGED_FILE", "unknown")
    if logger and changed_file != "unknown":
        await logger.send_log(
            f"👋 Le bot a redémarré en raison de modifications dans `{changed_file}`",
            title="♻️ Bot Restarted"
        )
        os.environ["BOT_CHANGED_FILE"] = "unknown"

async def load_extensions():
    await bot.load_extension("cogs.bot_commands")
    await bot.load_extension("cogs.permissions")
    await bot.load_extension("cogs.bot_info")
    await bot.load_extension("cogs.welcomer")
    await bot.load_extension("cogs.invite_tracker")
    await bot.load_extension("cogs.console")
    await bot.load_extension("cogs.bump_reminder")
    await bot.load_extension("cogs.ticket_system")
    await bot.load_extension("cogs.recruitment_survey")
    await bot.load_extension("cogs.bot_logger")
    print("✅ All cogs loaded successfully.")

def setup_signal_handlers(loop):
    def sync_shutdown_handler(signum, frame):
        global _shutting_down
        if _shutting_down:
            print("[DEBUG] Signal received but shutdown is already in progress.")
            return
            
        _shutting_down = True

        is_restarting = os.getenv("BOT_RESTARTING", "false").lower() == "true"
        manual_shutdown = not is_restarting

        asyncio.run_coroutine_threadsafe(
            shutdown(manual=manual_shutdown, restart=is_restarting), loop
        )

    for sig in (signal.SIGINT, signal.SIGTERM):
        signal.signal(sig, sync_shutdown_handler)

async def shutdown(manual=False, restart=False):
    global _shutting_down
    if _shutting_down:
        return
    _shutting_down = True

    print(f"[DEBUG] Shutdown called. manual={manual} restart={restart}")

    logger = bot.get_cog("BotLogger")
    changed_file = os.getenv("BOT_CHANGED_FILE", "unknown")

    if logger:
        await logger.shutdown(manual=manual, restart=restart, changed_file=changed_file)
    else:
        print("⚠️ BotLogger cog not loaded yet, skipping log.")

    await asyncio.sleep(1)
    await bot.close()
    print("👋 Bot is shutting down...")
    
async def main():
    if not token:
        print("❌ ERROR: DISCORD_TOKEN environment variable not set.")
        return

    await load_extensions()
    setup_signal_handlers(asyncio.get_running_loop())
    await bot.start(token)

    if "BOT_RESTARTING" in os.environ:
        del os.environ["BOT_RESTARTING"]

if __name__ == "__main__":
    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(main())
    finally:
        loop.run_until_complete(bot.close())
        loop.close()
