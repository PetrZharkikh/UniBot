import logging
import os

import openai

from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

_requests_count = 0


async def solve_task_with_gpt(task_text: str) -> str:
    """Send the task text to OpenAI and return the response."""
    global _requests_count
    response = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Solve this problem step-by-step:\n{task_text}"}],
        temperature=0.5,
    )
    _requests_count += 1
    logging.info("Solve task requests used: %d", _requests_count)
    return response.choices[0].message.content.strip()