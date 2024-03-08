import csv 

def geojsonmaker(zone, nom, num, culture, region, ville, village) -> dict:
    dict_ = {
        "type": "Feature",
        "geometry":{
            "type":"Polygon",
            "coordinates":zone
        },
        "properties":{
            "NomduTuteur":nom,
            "Numerodetelephone":num,
            "TypedeCulture":culture,
            "EmplacementdelaParcelleRegion":region,
            "EmplacementdelaParcelleVille":ville,
            "EmplacementdelaParcelleVillage":village
        }
    }
    return dict_

 

def read_csv(filepath_csv) -> list:
    excl = []
    with open(filepath_csv) as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        for row in reader:
            excl.append(row)
    return excl

def file_returned(filepath_csv="") -> list:
    geojson = []
    exclusion_list = read_csv(filepath_csv)
    # print(type(eval(exclusion_list[0][6])))
    for val in exclusion_list:
        geojson.append(geojsonmaker(eval(val[6]),val[0],val[1],val[2],val[3],val[4],val[5]))
    return geojson


# if __name__ == "__main__":
#     file_returned("./Parcelles_agribooster_ngoran.csv")