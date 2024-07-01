import random

# List of GitHub emojis/icons
github_icons = [
    ":octocat:",
    ":atom:",
    ":zap:",
    ":fire:",
    ":rocket:",
    ":star:",
    ":bug:",
    ":sparkles:",
    ":tada:",
    ":recycle:",
    ":mag:",
    ":lock:",
    ":speech_balloon:",
    ":bell:",
    ":bulb:"
]

# List of random quotes
random_quotes = [
    "Code is like humor. When you have to explain it, it’s bad.",
    "Fix the cause, not the symptom.",
    "Optimism is an occupational hazard of programming: feedback is the treatment.",
    "Simplicity is the soul of efficiency.",
    "Before software can be reusable it first has to be usable.",
    "Make it work, make it right, make it fast.",
    "The function of good software is to make the complex appear to be simple.",
    "Simplicity is prerequisite for reliability.",
    "Programming isn't about what you know; it's about what you can figure out.",
    "Experience is the name everyone gives to their mistakes."
]

def generate_commit_message():
    icon = random.choice(github_icons)
    quote = random.choice(random_quotes)
    message = f"{icon}  {quote}"
    return message

if __name__ == "__main__":
    print(generate_commit_message())
