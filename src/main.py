# main.py
import discord
from discord.ext import commands
from dotenv import load_dotenv
import aiohttp

import os
import asyncio
import signal
import platform
from utils.shutdown import shutdown
from utils.locker_db import LockerDB

load_dotenv()

token = os.getenv("DISCORD_TOKEN")
GUILD_ID = 1368272372230000711

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents, application_id=1373334216233717840)

_shutting_down = False
_bot_ready = False

async def fetch_latest_github_version():
    url = "https://api.github.com/repos/nerfine/Crapules-express/releases/latest"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
                return data.get("tag_name", "unknown")
            return "unknown"

@bot.event
async def on_ready():
    global _bot_ready
    print(f'✅ Logged in as {bot.user}')
    latest_version = await fetch_latest_github_version()
    activity = discord.Activity(
        type=discord.ActivityType.playing,
        name=f"{latest_version} | /commands",
        details="discord.gg/crxp | TruckersMP: /vtc/80146"
    )
    await bot.change_presence(activity=activity, status=discord.Status.online)

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

    _bot_ready = True

async def load_extensions():
    extensions = [
        "cogs.bot_logger",
        "cogs.bot_commands",
        "cogs.permissions",
        "cogs.bot_info",
        "cogs.welcomer",
        "cogs.invite_tracker",
        "cogs.console",
        "cogs.bump_reminder",
        "cogs.ticket_system",
        "cogs.recruitment_survey",
        "cogs.convoy_survey",
        "cogs.ticket_control",
        "cogs.promotion_checker",
    ]
    for ext in extensions:
        try:
            await bot.load_extension(ext)
            print(f"✅ Loaded {ext}")
        except Exception as e:
            print(f"❌ Failed to load {ext}: {e}")
    print("✅ All cogs loaded successfully.")

def setup_signal_handlers(loop):
    def sync_shutdown_handler(signum, frame):
        global _shutting_down, _bot_ready
        if _shutting_down:
            print("[DEBUG] Signal received but shutdown is already in progress.")
            return

        if not _bot_ready:
            print("[DEBUG] Shutdown signal received before bot was ready. Ignoring.")
            return

        _shutting_down = True

        is_restarting = os.getenv("BOT_RESTARTING", "false").lower() == "true"
        manual_shutdown = not is_restarting

        asyncio.run_coroutine_threadsafe(
            shutdown(manual=manual_shutdown, restart=is_restarting), loop
        )

    for sig in (signal.SIGINT, signal.SIGTERM):
        signal.signal(sig, sync_shutdown_handler)

async def main():
    if not token:
        print("❌ ERROR: DISCORD_TOKEN environment variable not set.")
        return

    await LockerDB.ensure_table()
    await load_extensions()
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
