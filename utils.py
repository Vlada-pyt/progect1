from flask import Flask
from utils import load_candidates
def load_candidates(file):

    """Функция, которая загружает данные из файла"""
    with open("file", "r") as file:
        file_contents = file.read()
        return file_contents
CANDIDATE = "candidatea.json"

candidates_list = load_candidates(CANDIDADET)

def get_all():
    """Функция, которая покажет всех кандидатов"""
    condidates = []
    for i in candidates_list:
        condidate = {i["name"]}
        condidates.append(i["name"])
    return condidates


def get_by_pk(pk):
    """Функция, которая вернет кандидата по pk"""
    for i in candidates_list:
        if i["pk"] == pk:
            return i["name"]

def get_by_skill(skill_name):
    """Функция, которая вернет кандидатов по навыку"""
    for skill in candidates_list:
        if skill["skills"] == skill_name:
            return skill["name"]

