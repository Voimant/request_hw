from pprint import pprint
import json
import requests

class Superhero():
    def super_carts(self,id):
        """Принимает на вход ID персонажей из глоссария
        Вводить только число, метод возвращает словарь карточки персонажа"""

        url = 'https://akabab.github.io/superhero-api/api'
        resp = requests.get(url + f'/id/{id}.json')
        x = resp.json()
        return(x)






def character_comparison(person_list):
    """принимает на вход список карточек персонажей"""
    dict_person = {}
    for card in person_list:
        name = (card['name'])
        int = card["powerstats"]["intelligence"]
        # pprint(name)
        # pprint(int)
        dict_person[name] = int
    return dict_person

    # pprint(person_list['powerstats']['intelligence'])
    # for k,v in person_list['powerstats'].items():

def max_int(dict_super):
    return(max(dict_super, key=dict_super.get))


if __name__ == '__main__':


    hulk = Superhero()
    # hulk.super_carts(332)
    # pprint(hulk.super_carts(332))

    id_1 = hulk.super_carts(332)
    capitan_america = Superhero()
    id_2 = capitan_america.super_carts(149)
    thanos = Superhero()
    id_3 = thanos.super_carts(655)


    list_1 = [id_1,id_2,id_3]

    print(character_comparison(list_1))
    print("Самый умный персонаж: ")
    print(max_int(character_comparison(list_1)))