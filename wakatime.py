import requests
import json
import os
from base64 import b64encode

wakatime_api_key = os.environ.get('WAKATIME_API_KEY')
wakatime_user_id = os.environ.get('WAKATIME_USER_ID')
wakatime_api_key = wakatime_api_key.encode()

wakatime_headers = {"Authorization": "Basic " +
                    b64encode(wakatime_api_key).decode()}

wakatime_stats = requests.get(
    "https://wakatime.com/api/v1/users/" + wakatime_user_id + "/stats/last_7_days", headers=wakatime_headers)

wakatime_languages = wakatime_stats.json()['data']['languages']

data = []

for wakadata in wakatime_languages:
    data.append((wakadata["name"], wakadata['digital'], wakadata["percent"]))

max_value = max(count for _, _, count in data)
increment = max_value / 25

longest_label_length = max(len(label) for label, _, _ in data)

output = ""

for label, time, count in data:

    round(count, 2)

    bar_chunks, remainder = divmod(int(count * 8 / increment), 8)

    bar = chr(9619) * bar_chunks

    if remainder > 0:
        bar += chr(9619)

    bar = bar or ""

    output += f'{label.rjust(longest_label_length)} {time}h - {count:#5.2f}% {bar} \n'


github_token = os.environ.get('GITHUB_TOKEN')
gist_id = os.environ.get('GIST_ID')

data = {
    "files": {
        "weekly_development_breakdown.txt": {
            "content": output,
            "filename": "weekly_development_breakdown.txt"
        }
    }
}

github_headers = {"Authorization": "token " + github_token}

gist = requests.patch("https://api.github.com/gists/" +
                      gist_id, data=json.dumps(data), headers=github_headers)

print(gist.json())
