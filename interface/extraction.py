# _*_ encoding: utf-8 _*_
import geojson
import json
import csv
import xlwings as xw
from geojsonmaker import *
import os 

from tkinter import *

def wrote_geojson(filepath, data):
    with open(filepath, "a", encoding="utf8") as Af:
        geojson.dump({"type": "FeatureCollection",
        "name": "parcelle",
        "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } }, 'features': data}, Af)

def read_txt(filepath):
    with open(filepath, "r") as exs:
            lines = exs.readlines()
            lines = lines[0].split(",")
            return lines

def read_csv(filepath_csv, filepath_txt):
    excl = []
    with open(filepath) as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        for row in reader:
            excl.append(row[0])
    # with open(filepath_txt, "a", encoding="utf8") as exs:
    #     for i in excl:
    #         exs.write(i+",")
    return excl

def jointure(*tuple):
    global i
    join_ = "".join(tuple)
    return join_

def file_creator(repository="Geojson",fileName=" "):
    """
    Crée un fichier dans le dossier spécifié avec le contenu donné.
    Args:
        repository (str): Le chemin du dossier où le fichier doit etre créé.
        fileName (str): Le nom du fichier à créer. 
    Returns:
        str: Le chemin complet du fichier créé.
    """
    #Verifier si le repectoire existe, sinon le créer
    if not os.path.exists(repository):
        os.makedirs(repository)
    i=1
    # Chemin complet du fichier
    if fileName != " ":
        cheminFichier = os.path.join(".",repository, jointure(fileName,".geojson"))
        if not os.path.isfile(cheminFichier):
            return cheminFichier
        else:
            return os.path.join(".",repository, jointure(fileName,str(i),".geojson"))
            i+=1
    else:
        return "ArgError: \nNom du fichier compromis"



def main(path="None"):

    dic_caracter = {
        "\u00c0" :"À",
        "\u00c1" :"Á",
        "\u00c2" :"Â",
        "\u00c3" :"Ã",
        "\u00c4" :"Ä",
        "\u00c5" :"Å",
        "\u00c6" :"Æ",
        "\u00c7" :"Ç",
        "\u00c8" :"È",
        "\u00c9" :"É",
        "\u00ca" :"Ê",
        "\u00cb" :"Ë",
        "\u00cc" :"Ì",
        "\u00cd" :"Í",
        "\u00ce" :"Î",
        "\u00cf" :"Ï",
        "\u00d1" :"Ñ",
        "\u00d2" :"Ò",
        "\u00d3" :"Ó",
        "\u00d4" :"Ô",
        "\u00d5" :"Õ",
        "\u00d6" :"Ö",
        "\u00d8" :"Ø",
        "\u00d9" :"Ù",
        "\u00da" :"Ú",
        "\u00db" :"Û",
        "\u00dc" :"Ü",
        "\u00dd" :"Ý",
        "\u00df" :"ß",
        "\u00e0" :"à",
        "\u00e1" :"á",
        "\u00e2" :"â",
        "\u00e3" :"ã",
        "\u00e4" :"ä",
        "\u00e5" :"å",
        "\u00e6" :"æ",
        "\u00e7" :"ç",
        "\u00e8" :"è",
        "\u00e9" :"é",
        "\u00ea" :"ê",
        "\u00eb" :"ë",
        "\u00ec" :"ì",
        "\u00ed" :"í",
        "\u00ee" :"î",
        "\u00ef" :"ï",
        "\u00f0" :"ð",
        "\u00f1" :"ñ",
        "\u00f2" :"ò",
        "\u00f3" :"ó",
        "\u00f4" :"ô",
        "\u00f5" :"õ",
        "\u00f6" :"ö",
        "\u00f8" :"ø",
        "\u00f9" :"ù",
        "\u00fa" :"ú",
        "\u00fb" :"û",
        "\u00fc" :"ü",
        "\u00fd" :"ý",
        "\u00ff" :"ÿ"
    }

    name_file= path.split("/")
    inter = name_file[-1].split(".")
    name_file_geo = inter[0] #extraction du nom du fichier

    features_centrale = []
    featuress =[]
    
    foun = 0
    siz = 0
    if name_file_geo =="None" or name_file_geo =="":
        return "Veuillez reasseyer \nChemin non valide !"
    elif(inter[1] !="csv"):
        return "Veuillez selection \nun fichier .csv !"
    else:
        features = file_returned(path)
        chem = file_creator("interface\Geojson",name_file_geo)
        print (chem)
        if chem != "ArgError: \nNom du fichier compromis":
            with open(chem, "a", encoding="utf8") as Af:
                print("Entrer en ecriture")
                geojson.dump({"type": "FeatureCollection","name": "parcelle","crs":{ "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" }},'features': features}, Af)
                print("Fichier ecrit!!!")
            return chem
        else:
            return "ArgError: \nNom du fichier compromis"

# main("C:/Users/KOUASSIKOUADIOAIME/Desktop/code/Book1.csv")

def read_geojson(path):
    """
    Cette fonction prend en entré de le chemin d'un fichier geojson et retourne des infos
    telles que la le nom de producteur et les coordonnées de la parcelle.
    Args:
        path (str): chemin du fichier GEOJSON

    return:
        Retourne un tuple de deux tableaux 

    """
    data_show = []
    data_caption = []
    try:
        json_data = open(path).read()
        data = json.loads(json_data)
        for i in range (0, len(data["features"])):
            data_show.append(data["features"][i]['geometry']['coordinates'][0])
        for j in range (0, len(data["features"])):
            data_caption.append(data["features"][j]['properties']['NomduTuteur'])
        return (data_show, data_caption)
    except:
        return (data_show, data_caption)