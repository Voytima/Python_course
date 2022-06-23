# 2.*Написать скрипт, создающий из config.yaml стартер для проекта
import os
import yaml

with open('config.yaml') as f:
    project = yaml.safe_load(f)
# print(project)


def pj_starter(names, frame=""):
    for fold, path in names.items():
        fold_path = os.path.join(frame, fold)
        os.makedirs(fold_path, exist_ok=True)
        if isinstance(path, dict):
            pj_starter(path, fold_path)
        else:
            for n in path:
                if isinstance(n, dict):
                    pj_starter(n, fold_path)
                elif isinstance(n, str):
                    with open(os.path.join(fold_path, f'{n}'), 'a') as _:
                        pass


pj_starter(project)
