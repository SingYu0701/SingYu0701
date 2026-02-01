from github import Github
import matplotlib.pyplot as plt
from collections import Counter
import os


g = Github(token)
user = g.get_user("SingYu0701") 

langs = []

for repo in user.get_repos():
    if not repo.fork and repo.language:
        langs.append(repo.language)

if not langs:
    print("沒有抓到語言，請確認你的 repo 是否有語言資訊")
    exit(0)

counter = Counter(langs)
labels = list(counter.keys())
sizes = list(counter.values())

plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Top Languages")
plt.tight_layout()

os.makedirs("assets", exist_ok=True)
plt.savefig("assets/top-langs.svg")
plt.close()

print("Top Languages 圖生成完成 → assets/top-langs.svg")
