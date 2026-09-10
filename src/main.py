import ollama
import discord
from dotenv import load_dotenv
from os import getenv

load_dotenv()

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)


@client.event
async def on_ready() -> None:
    print("ログインしました")
    new_activity = f"テスト"
    await client.change_presence(activity=discord.Game(new_activity))
    await tree.sync()
    return


@tree.command(name="ketsu", description="文をケツ化する。")
async def ketsu_command(interaction: discord.Interaction, text: str) -> None:
    print("user input:")
    print(text)
    print(":user input")

    await interaction.response.defer()

    res = ollama.chat(
        model="gemma3:1b",
        messages=[
            {
                "role": "system",
                "content": """\
This is a joke application.
Replace the most effective word in the text with "ケツ" and output it as is.
""",
            },
            {
                "role": "user",
                "content": text,
            },
        ],
    )

    await interaction.followup.send(str(res.message.content))

    print("response:")
    print(res.message.content)
    print(":response")
    return


def main() -> None:
    TOKEN: str | None = getenv("TOKEN")
    assert TOKEN is not None
    client.run(TOKEN)


if __name__ == "__main__":
    main()
