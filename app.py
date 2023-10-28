from flask import Flask, json

app = Flask(__name__)

default_html = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Flask</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
  </head>
"""

table_html_first = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Flask</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
  </head>
    <body>
        <table class="table w-25 mt-3 m-auto text-center">
        <thead>
            <tr>
            <th scope="col">No.</th>
            <th scope="col">Llave</th>
            <th scope="col">Valor</th>
            </tr>
        </thead>
        <tbody>
"""

table_html_last = """
        </tbody>
        </table>
    </body>
</html>
"""

list_html_first = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Flask</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
  </head>
    <body>
        <ul class="list-group w-25 mt-3 m-auto text-center">
"""

list_html_last = """
        </ul>
    </body>
</html>
"""

@app.route("/dictionary/<path:dictionary>/add/<string:key>/<string:value>")
# Add a key-value pair to the dictionary, and show in the table hmtl
def addKeyValue(dictionary, key, value):
    dictionary = json.loads(dictionary)
    dictionary[key] = value
    table_html, i = table_html_first, 0
    for key, value in dictionary.items():
        i += 1
        table_html += f"""
            <tr>
            <th scope="row">{i}</th>
            <td>{key}</td>
            <td>{value}</td>
            </tr>
        """
    table_html += table_html_last
    return """
    <div class="alert alert-info w-25 mt-3 m-auto" role="alert">
    Se añadió el par clave-valor al diccionario.
    </div>
    """ + table_html

@app.route("/dictionary/<path:dictionary>/delete/<string:key>")
def deleteKeyValue(dictionary, key):
    dictionary = json.loads(dictionary)
    del dictionary[key]
    table_html, i = table_html_first, 0
    for key, value in dictionary.items():
        i += 1
        table_html += f"""
            <tr>
            <th scope="row">{i}</th>
            <td>{key}</td>
            <td>{value}</td>
            </tr>
        """
    table_html += table_html_last
    return """
    <div class="alert alert-danger w-25 mt-3 m-auto" role="alert">
    Se eliminó el par clave-valor del diccionario.
    </div>
    """ + table_html

@app.route("/dictionary/<path:dictionary>/modify/<string:key>/<string:value>")
def modifyKeyValue(dictionary, key, value):
    dictionary = json.loads(dictionary)
    if key in dictionary:
        dictionary[key] = value
        table_html, i = table_html_first, 0
        for key, value in dictionary.items():
            i += 1
            table_html += f"""
                <tr>
                <th scope="row">{i}</th>
                <td>{key}</td>
                <td>{value}</td>
                </tr>
            """
        table_html += table_html_last
        return """
        <div class="alert alert-warning w-25 mt-3 m-auto" role="alert">
        Se modificó el par clave-valor del diccionario.
        </div>
        """ + table_html
    else:
        return default_html + """
        <div class="alert alert-danger w-25 mt-3 m-auto" role="alert">
        No se pudo modificar el par clave-valor del diccionario.
        </div>
        """
    
@app.route("/dictionary/<path:dictionary1>/combine/<path:dictionary2>")
def combineDictionaries(dictionary1, dictionary2):
    dictionary1, dictionary2 = json.loads(dictionary1), json.loads(dictionary2)
    dictionary1.update(dictionary2)
    table_html, i = table_html_first, 0
    for key, value in dictionary1.items():
        i += 1
        table_html += f"""
            <tr>
            <th scope="row">{i}</th>
            <td>{key}</td>
            <td>{value}</td>
            </tr>
        """
    table_html += table_html_last
    return """
    <div class="alert alert-success w-25 mt-3 m-auto" role="alert">
    Se combinaron los dos diccionarios.
    </div>
    """ + table_html

@app.route("/set/<string:setList>/add/<string:element>")
def addElementToSet(setList, element):
    setList = set(setList.replace(" ", "").split(","))
    if element not in setList:
        return default_html + """
        <div class="alert alert-danger w-25 mt-3 m-auto" role="alert">
        No se pudo agregar el elemento al conjunto.
        </div>
        """
    else:
        setList.add(element)
        list_html = list_html_first
        for i in setList:
            list_html += f"""
            <li class="list-group-item">{i}</li>
            """
        list_html += list_html_last
        return """
        <div class="alert alert-info w-25 mt-3 m-auto" role="alert">
        Se agregó el elemento al conjunto.
        </div>
        """ + list_html

@app.route("/set/<string:setList>/delete/<string:element>")
def deleteElementFromSet(setList, element):
    setList = set(setList.replace(" ", "").split(","))
    if element not in setList:
        return default_html + """
        <div class="alert alert-danger w-25 mt-3 m-auto" role="alert">
        No se pudo eliminar el elemento al conjunto.
        </div>
        """
    else:
        setList.remove(element)
        list_html = list_html_first
        for i in setList:
            list_html += f"""
            <li class="list-group-item">{i}</li>
            """
        list_html += list_html_last
        return """
        <div class="alert alert-danger w-25 mt-3 m-auto" role="alert">
        Se eliminó el elemento del conjunto.
        </div>
        """ + list_html

@app.route("/set/<string:set1>/combine/<string:set2>")

def combineSets(set1, set2):
    set1, set2 = set(set1.replace(" ", "").split(",")), set(set2.replace(" ", "").split(","))
    set1.union(set2)
    list_html = list_html_first
    for i in set1:
        list_html += f"""
        <li class="list-group-item">{i}</li>
        """
    list_html += list_html_last
    return """
    <div class="alert alert-success w-25 mt-3 m-auto" role="alert">
    Se combinaron los dos conjuntos.
    </div>
    """ + list_html

@app.route("/set/<string:set1>/difference/<string:set2>")
def differenceOfSets(set1, set2):
    set1, set2 = set(set1.replace(" ", "").split(",")), set(set2.replace(" ", "").split(","))
    set1.difference(set2)
    list_html = list_html_first
    for i in set1:
        list_html += f"""
        <li class="list-group-item">{i}</li>
        """
    list_html += list_html_last
    return """
    <div class="alert alert-success w-25 mt-3 m-auto" role="alert">
    Se obtuvo la diferencia de los dos conjuntos.
    </div>
    """ + list_html

@app.route("/tuple/<string:tupleList>/add/<string:element>")
def addElementToTuple(tupleList, element):
    tupleList = tuple(tupleList.replace(" ", "").split(","))
    list = []
    for i in tupleList:
        list.append(i)
    list.append(element)
    list_html = list_html_first
    for i in list:
        list_html += f"""
        <li class="list-group-item">{i}</li>
        """
    list_html += list_html_last
    return """
    <div class="alert alert-success w-25 mt-3 m-auto" role="alert">
    Se agregó el elemento a la tupla.
    </div>
    """ + list_html

@app.route("/tuple/<string:tupleList>/delete/<string:element>")
def deleteElementFromTuple(tupleList, element):
    tupleList = tuple(tupleList.replace(" ", "").split(","))
    list = []
    for i in tupleList:
        list.append(i)
    list.remove(element)
    list_html = list_html_first
    for i in list:
        list_html += f"""
        <li class="list-group-item">{i}</li>
        """
    list_html += list_html_last
    return """
    <div class="alert alert-danger w-25 mt-3 m-auto" role="alert">
    Se eliminó el elemento de la tupla.
    </div>
    """ + list_html

@app.route("/tuple/<string:tuple1>/combine/<string:tuple2>")
def concatenateTuples(tuple1, tuple2):
    tuple1, tuple2 = tuple(tuple1.replace(" ", "").split(",")), tuple(tuple2.replace(" ", "").split(","))
    tuple1 += tuple2
    list_html = list_html_first
    for i in tuple1:
        list_html += f"""
        <li class="list-group-item">{i}</li>
        """
    list_html += list_html_last
    return """
    <div class="alert alert-success w-25 mt-3 m-auto" role="alert">
    Se combinaron las dos tuplas.
    </div>
    """ + list_html

@app.route("/tuple/<string:tupleList>/reverse")
def reverseTuple(tupleList):
    tupleList = tuple(tupleList.replace(" ", "").split(","))
    list = []
    for i in tupleList:
        list.append(i)
    list.reverse()
    list_html = list_html_first
    for i in list:
        list_html += f"""
        <li class="list-group-item">{i}</li>
        """
    list_html += list_html_last
    return """
    <div class="alert alert-success w-25 mt-3 m-auto" role="alert">
    Se revirtió el orden de la tupla.
    </div>
    """ + list_html

if __name__ == "__main__":
   app.run(debug=True)