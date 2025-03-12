import requests
import re


def get_all_player_ids():
    cookies = {
    'session-id': 'bbc6e14d-f806-4a3f-a3a0-aa3efb7cd0c8',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Referer': 'https://www.google.com/',
        'Connection': 'keep-alive',
        # 'Cookie': 'session-id=bbc6e14d-f806-4a3f-a3a0-aa3efb7cd0c8',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-User': '?1',
        'Priority': 'u=0, i',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = '{}'

    response = requests.post('https://www.unrivaled.basketball/stats/player', cookies=cookies, headers=headers)
    # Get ids that match the pattern below
    ids = re.findall(r'href="/player/?([^\'" >]+)', response.text)
    return ids


if __name__ == "__main__":
    print(get_all_player_ids())