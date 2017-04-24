# -*- coding: utf-8 -*-
import json
from os.path import join, dirname, abspath
from posix import listdir


def main():
    資料夾 = join(dirname(abspath(__file__)), 'data')
    for 檔名 in sorted(listdir(資料夾)):
        if 檔名.endswith('jsonlines'):
            全部資料 = []
            with open(join(資料夾, 檔名)) as 檔案:
                for 一逝 in 檔案.readlines():
                    全部資料.append(json.loads(一逝))
            排好結果 = sorted(全部資料, key=lambda 資料: (資料['name']))
            with open(join(資料夾, 檔名[:-5]), 'w') as 檔案:
                json.dump(
                    排好結果, 檔案,
                    sort_keys=True, indent=2, ensure_ascii=False,
                )


main()
