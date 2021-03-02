import git
import datetime
import time

# urlは適宜自身が編集可能なレポジトリに書き換えてください
url = 'https://github.com/takumidev86/tracking_evolution_GH_SO.git'

# cloneしたプロジェクトを出力するパス
to_path = '.'
repo = git.Repo(to_path)
# print(repo.git.diff('HEAD'))

for item in repo.iter_commits('master', max_count=10):
    dt = datetime.datetime.fromtimestamp(
        item.authored_date).strftime("%Y-%m-%d %H:%M:%S")
    print("%s %s %s " % (item.hexsha, item.author, dt))
