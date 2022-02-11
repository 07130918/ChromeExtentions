# make manifest.json and set icon to dist

import os
import json
import shutil


def main():
    content = {
        "name": "To Do List",
        "description": "A simple to-do list extension, You can also write your own not to do list",
        "manifest_version": 3,
        "version": "1.0",
        "permissions": ["activeTab", "scripting", "storage"],
        "action": {
            "default_icon": "icon.png",
            "default_popup": "index.html"
        }
    }

    os.system('npm run build')
    os.system('touch dist/manifest.json')
    with open('dist/manifest.json', 'w') as f:
        json.dump(content, f, ensure_ascii=False, indent=4, separators=(',', ': '))

    shutil.copy('./icon.png', './dist')


if __name__ == '__main__':
    main()
