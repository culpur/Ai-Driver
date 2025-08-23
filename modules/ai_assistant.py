# /opt/ai_driver/modules/ai_assistant.py

import os
import json
import re
from pathlib import Path
from openai import OpenAI

# Live thoughts queue (used by TUI for streaming sidebar)
AI_THOUGHTS = []

# Load config
CONFIG = json.loads(Path(".env").read_text())
OPENAI_API_KEY = CONFIG.get("openai_api_key")

client = OpenAI(api_key=OPENAI_API_KEY)

def stream_thought(thought):
    """Send a new thought to the global stream queue."""
    if len(AI_THOUGHTS) >= 20:
        AI_THOUGHTS.pop(0)
    AI_THOUGHTS.append(f"🧠 {thought}")


def ask_ai(recon_data):
    print("[AI ➤ Asking for next step...]")
    stream_thought("Analyzing recon data for actionable next steps...")

    try:
        messages = [
            {
                "role": "system",
                "content": (
                    "You are a highly skilled penetration testing AI assistant. "
                    "Based on the following recon and loot data, suggest additional commands "
                    "to enumerate, exploit, or pivot further. Return only shell commands if possible."
                )
            },
            {
                "role": "user",
                "content": f"Recon and loot data:\n{json.dumps(recon_data)[:7000]}"
            },
        ]

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            max_tokens=800,
            temperature=0.3
        )

        suggestion = response.choices[0].message.content.strip()
        stream_thought("Commands prepared based on recon.")
        return suggestion

    except Exception as e:
        error_msg = f"AI request failed: {e}"
        print(f"[AI ➤ ERROR] {error_msg}")
        stream_thought(f"❌ {error_msg}")
        return None


def parse_ai_commands(ai_response):
    """
    Extract shell commands from the AI response.
    """
    if not ai_response:
        return []

    commands_text = ""
    # Extract code block if present
    match = re.search(r"```(?:bash)?\n(.*?)```", ai_response, re.DOTALL)
    if match:
        commands_text = match.group(1).strip()
    else:
        # Try to extract lines that look like commands
        commands_text = "\n".join(
            line.strip()
            for line in ai_response.splitlines()
            if line.strip() and not line.strip().startswith("#")
        )

    # Parse into individual commands
    commands = []
    for line in commands_text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        commands.append(line.split())

    stream_thought(f"Parsed {len(commands)} commands for execution.")
    return commands


def get_thoughts():
    """Return the current list of AI thoughts (for dashboard use)."""
    return AI_THOUGHTS.copy()
