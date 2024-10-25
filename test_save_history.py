import json
import os

history_file = 'test_save_history.json'

def save_history(filepath, link):
    history = []
    if os.path.exists(history_file):
        with open(history_file, 'r') as f:
            history = json.load(f)
    history.append({'filepath': os.path.basename(filepath), 'download_link': link})
    with open(history_file, 'w') as f:
        json.dump(history, f, indent=4)


def test_save_history():
    test_filepath = 'test_file.txt'
    test_download_link = 'https://file.io/sdvfdfgd'

    save_history(test_filepath, test_download_link)

    with open('test_save_history.json', 'r') as f:
        history = json.load(f)
        assert len(history) == 1
        assert history[0]['filepath'] == test_filepath
        assert history[0]['download_link'] == test_download_link

    os.remove('test_save_history.json')

test_save_history()