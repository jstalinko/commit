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

def generate_commit_message():
    icon = random.choice(github_icons)
    message = f"{icon} Updated LAST_COMMIT.txt with random message"
    return message

if __name__ == "__main__":
    print(generate_commit_message())
