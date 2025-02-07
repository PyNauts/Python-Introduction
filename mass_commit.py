import os
import subprocess

repo_path = os.getcwd()  # Ensure you're in the correct repo

for i in range(1, 10001):
    with open("commit_file.txt", "a") as f:
        f.write(f"Commit number {i}\n")  # Append new content

    subprocess.run(["git", "add", "commit_file.txt"], check=True)
    subprocess.run(["git", "commit", "-m", f"Commit {i}"], check=True)

    if i % 100 == 0:  # Push every 100 commits to avoid rate limits
        subprocess.run(["git", "push"], check=True)

# Final push
subprocess.run(["git", "push"], check=True)

print("10,000 commits completed and pushed!")
