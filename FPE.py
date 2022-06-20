{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "FPE.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyPKD1SxOfnmyQyMIc6MquAo",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ElHaban3ro/GoogleLogin/blob/main/FPE.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZVK7BIxc1tP1",
        "outputId": "fd9c4f74-d164-4832-e181-04a905cceec4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1349.0\n",
            "1851.0\n"
          ]
        }
      ],
      "source": [
        "# Ejercicio 1\n",
        "# Escribir una función que aplique un descuento a un precio y otra que aplique el \n",
        "# IVA a un precio. Escribir una tercera función que reciba un diccionario con los \n",
        "# precios y porcentajes de una cesta de la compra, y una de las funciones anteriores, \n",
        "# y utilice la función pasada para aplicar los descuentos o el IVA a los productos \n",
        "# de la cesta y devolver el precio final de la cesta.\n",
        "\n",
        "\n",
        "\n",
        "def descuento_f(precio, descuento):\n",
        "  return precio - (precio * descuento) / 100\n",
        "\n",
        "def iva_f(precio, iva):\n",
        "  return precio + (precio * iva)  / 100\n",
        "\n",
        "\n",
        "def compra(dict_compra, function):\n",
        "\n",
        "  total = 0\n",
        "  for precio, descuento in dict_compra.items(): # Una forma de enfocar los problemas con diccionarios.\n",
        "    total += function(precio, descuento)\n",
        "\n",
        "  return total\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "cesta = {1000:20, 500:10, 100:1}\n",
        "\n",
        "\n",
        "print(compra(cesta, descuento_f))\n",
        "print(compra(cesta, iva_f))"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Ejercicio 2\n",
        "# Escribir una función que simule una calculadora científica que permita calcular \n",
        "# el seno, coseno, tangente, exponencial y logaritmo neperiano. La función preguntará \n",
        "# al usuario el valor y la función a aplicar, y mostrará por pantalla una tabla con \n",
        "# los enteros de 1 al valor introducido y el resultado de aplicar la función a esos enteros.\n",
        "\n",
        "from numpy import log1p\n",
        "\n",
        "\n",
        "\n",
        "def seno(opuesto, hipotenusa):\n",
        "  return opuesto / hipotenusa\n",
        "\n",
        "\n",
        "def coseno(adyacente, hipotenusa):\n",
        "  return adyacente / hipotenusa\n",
        "\n",
        "\n",
        "def tangente(opuesto, adyacente):\n",
        "  return opuesto / adyacente\n",
        "\n",
        "\n",
        "def exponentes(base, exponente):\n",
        "  return base ** exponente\n",
        "\n",
        "\n",
        "def logaritmo_neperiano(x):\n",
        "  lg = round(log1p(x), 2) # Por alguna razón no es preciso.\n",
        "  return lg\n",
        "\n",
        "\n",
        "def calculadora(function, a, rango = 0, *args, **kwargs):\n",
        "  \n",
        "\n",
        "  if function != logaritmo_neperiano:\n",
        "    for i in range(rango):\n",
        "      print(f'b = {i+1}:   {function(a, i + 1)}')\n",
        "      # return \n",
        "    \n",
        "  else:\n",
        "    for a in range(a):\n",
        "      print(f'a = {a+1}:   {function(a + 1)}')\n",
        "\n",
        "\n",
        "def home():\n",
        "  print('Buen día, ¿qué quiere hacer?')\n",
        "\n",
        "  opciones = {'seno': seno, 'coseno': coseno, 'tangente': tangente, 'exponente': exponentes, 'ln': logaritmo_neperiano}\n",
        "  opcion = input('------------------>   ')\n",
        "  v1 = int(input('Ingrese el valor 1 para la función --------->  '))\n",
        "  rango_inp = int(input('Ingrese el valor 2 para la función--------->  '))\n",
        "\n",
        "\n",
        "  if opcion in opciones:\n",
        "    calculadora(opciones[opcion], v1, rango=rango_inp)\n",
        "\n",
        "  else:\n",
        "    print('No tenemos esa opción, asegurese de estar escrbiendolo bien!')\n",
        "\n",
        "\n",
        "\n",
        "home()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ecJhsuxEAsOt",
        "outputId": "0101cfe1-9f61-41a0-fde9-35437cdcfd6b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Buen día, ¿qué quiere hacer?\n",
            "------------------>   seno\n",
            "Ingrese el valor 1 para la función --------->  10\n",
            "Ingrese el valor 2 para la función--------->  10\n",
            "b = 1:   10.0\n",
            "b = 2:   5.0\n",
            "b = 3:   3.3333333333333335\n",
            "b = 4:   2.5\n",
            "b = 5:   2.0\n",
            "b = 6:   1.6666666666666667\n",
            "b = 7:   1.4285714285714286\n",
            "b = 8:   1.25\n",
            "b = 9:   1.1111111111111112\n",
            "b = 10:   1.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Ejercicio 3\n",
        "# Escribir una función que reciba otra función y una lista, y devuelva otra lista \n",
        "# con el resultado de aplicar la función dada a cada uno de los elementos de la lista.\n",
        "\n",
        "\n",
        "def transform(my_list, function):\n",
        "  print(f'Antigua Lista: {my_list}')\n",
        "  for element_list in my_list:\n",
        "    my_list[my_list.index(element_list)] = function(element_list)\n",
        "  print(f'Nueva Lista: {my_list}')\n",
        "\n",
        "\n",
        "def multiplicar(num):\n",
        "  return num * 5\n",
        "\n",
        "\n",
        "\n",
        "list_of_numbers = [3, 5, 7, 8, 13, 74, 1, 9, 39]\n",
        "\n",
        "transform(list_of_numbers, multiplicar)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mQq0mOqn9XJM",
        "outputId": "bc35cb5c-9395-4568-b8f2-fd82d21513d3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Antigua Lista: [3, 5, 7, 8, 13, 74, 1, 9, 39]\n",
            "Nueva Lista: [15, 25, 35, 40, 65, 370, 5, 45, 195]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Ejercicio 4\n",
        "# Escribir una función que reciba otra función booleana y una lista, y devuelva \n",
        "# otra lista con los elementos de la lista que devuelvan True al aplicarles la función booleana.\n",
        "\n",
        "def converted_lists(my_list, function):\n",
        "  print(f'Para la lista: {my_list}')\n",
        "  nw_list = []\n",
        "  for i in my_list:\n",
        "    if function(i) == True:\n",
        "      nw_list.append(i)\n",
        "\n",
        "  print(f' Obtenemos: {nw_list} ')\n",
        "\n",
        "\n",
        "\n",
        "def greater_boolean(num):\n",
        "  if num >= 30:\n",
        "    return True\n",
        "  elif num < 30:\n",
        "    return False\n",
        "\n",
        "\n",
        "list_of_numbers_b = [3, 5, 7, 31, 8, 13, 74, 10, 9, 39]\n",
        "\n",
        "converted_lists(list_of_numbers_b, greater_boolean)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "p_GfndbLAEZ_",
        "outputId": "fafea2da-5695-4cc3-d11f-9ff793b13ccb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Para la lista: [3, 5, 7, 31, 8, 13, 74, 10, 9, 39]\n",
            " Obtenemos: [31, 74, 39] \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Ejercicio 5\n",
        "# Escribir una función que reciba una frase y devuelva un diccionario con las \n",
        "# palabras que contiene y su longitud.\n",
        "\n",
        "\n",
        "\n",
        "def counter_letters(phrase):\n",
        "\n",
        "  dict_frecuency = {}\n",
        "  phrase = phrase.lower().split(' ')\n",
        "\n",
        "  for word in phrase:\n",
        "    if word not in dict_frecuency:\n",
        "      dict_frecuency[word] = len(word)\n",
        "\n",
        "  return dict_frecuency\n",
        "\n",
        "\n",
        "\n",
        "print(counter_letters('Hola como te encuentras? hola hola como estas'))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-ASWkQsyEndK",
        "outputId": "cdeb3751-8265-47b8-8972-33ec7088ccc8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'hola': 4, 'como': 4, 'te': 2, 'encuentras?': 11, 'estas': 5}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Ejercicio 6\n",
        "# Escribir una función reciba una lista de notas y devuelva la lista de calificaciones\n",
        "# correspondientes a esas notas.\n",
        "\n",
        "\n",
        "def calificaciones(notas_list):\n",
        "  if notas_list >= 11:\n",
        "    return 'tu eta loco pa'\n",
        "\n",
        "  elif notas_list >= 4:\n",
        "   return 'AP'\n",
        "\n",
        "  else:\n",
        "     return 'RP'\n",
        "\n",
        "\n",
        "misNotas = [3, 5, 7, 8, 15, 3.4, 1, 9, 5.5, 7.6]\n",
        "\n",
        "\n",
        "print(list(map(calificaciones, misNotas)))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "M6X454HxHx9n",
        "outputId": "7f7858c7-4844-4b09-e9ef-153d8645d8a8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['RP', 'AP', 'AP', 'AP', 'tu eta loco pa', 'RP', 'RP', 'AP', 'AP', 'AP']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Ejercicio 7\n",
        "# Escribir una función reciba un diccionario con las asignaturas y las notas de \n",
        "# un alumno y devuelva otro diccionario con las asignaturas en mayúsculas y las \n",
        "# calificaciones correspondientes a las notas.\n",
        "\n",
        "\n",
        "\n",
        "def mis_notas(notas_dict):\n",
        "  if notas_dict > 4:\n",
        "    return 'A'\n",
        "  else:\n",
        "    return 'R'\n",
        "\n",
        "  return  notas_dict\n",
        "\n",
        "\n",
        "def uppere(mstr):\n",
        "  return mstr.upper()\n",
        "\n",
        "misNotas = {'Fisica': 3, 'Economia': 5, 'Biologia': 7, 'Estadistica': 8, 'Mandarín': 15, 'Historia': 3.4, 'Francés': 1}\n",
        "\n",
        "valus = list(map(mis_notas, misNotas.values()))\n",
        "kis = list(map(uppere, misNotas.keys())) # En lugar de crear una función \"uppere\" podrías usar directametne str.upper. \n",
        "nw_dict = dict(zip(kis, valus))\n",
        "\n",
        "print(nw_dict)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wQqPnVtjPtrU",
        "outputId": "378194c7-df43-4982-db4c-8b8fc3bc6052"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'FISICA': 'R', 'ECONOMIA': 'A', 'BIOLOGIA': 'A', 'ESTADISTICA': 'A', 'MANDARÍN': 'A', 'HISTORIA': 'R', 'FRANCÉS': 'R'}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Ejercicio 8\n",
        "# Escribir una función reciba un diccionario con las asignaturas y las notas de \n",
        "# un alumno y devuelva otro diccionario con las asignaturas en mayúsculas y las \n",
        "# calificaciones correspondientes a las notas aprobadas.\n",
        "\n",
        "\n",
        "# NO LO HAGO ESTÁ REPETIDO xd"
      ],
      "metadata": {
        "id": "TnD0bZAHYPVl"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Ejercicio 9\n",
        "# Escribir una función que calcule el módulo de un vector.\n",
        "\n",
        "import math\n",
        "\n",
        "def vector_len_calculator(vector):\n",
        "  len_v = 0\n",
        "  for v in vector:\n",
        "    len_v += v**2\n",
        "\n",
        "  return math.sqrt(len_v)\n",
        "\n",
        "\n",
        "vector_len_calculator((1, 2, 3))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CSSG1otlYoIC",
        "outputId": "cee24f05-70cf-495b-aa53-e61cc6cbd957"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "3.7416573867739413"
            ]
          },
          "metadata": {},
          "execution_count": 130
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Ejercicio 10\n",
        "# Una inmobiliaria de una ciudad maneja una lista de inmuebles como la siguiente:\n",
        "\n",
        "# [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},\n",
        "# {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},\n",
        "# {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},\n",
        "# {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},\n",
        "# {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]\n",
        "# Construir una función que permita hacer búsqueda de inmuebles en función de un \n",
        "# presupuesto dado. La función recibirá como entrada la lista de inmuebles y un \n",
        "# precio, y devolverá otra lista con los inmuebles cuyo precio sea menor o igual \n",
        "# que el dado. Los inmuebles de la lista que se devuelva deben incorporar un nuevo \n",
        "# par a cada diccionario con el precio del inmueble, donde el precio de un inmueble \n",
        "# se calcula con las siguiente fórmula en función de la zona:\n",
        "\n",
        "# Zona A: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100)\n",
        "# Zona B: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100) * 1.5\n",
        "\n",
        "\n",
        "def compra_de_casa(inmuebles_list, presupuesto):\n",
        "  apto = []\n",
        "  for p in inmuebles_list:\n",
        "    precio = (p['metros'] * 1000 + p['habitaciones'] * 5000 + int(p['garaje']) * 15000) * (1 - (2021 - p['año']) / 100)\n",
        "    \n",
        "    if p['zona'] == 'B':\n",
        "      precio *= 1.5\n",
        "\n",
        "\n",
        "    if precio <= presupuesto:\n",
        "      p['precio'] = round(precio, 2)\n",
        "      apto.append(p)\n",
        "\n",
        "  return apto\n",
        "\n",
        "\n",
        "\n",
        "inmuebles = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},\n",
        "                {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},\n",
        "                {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},\n",
        "                {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},\n",
        "                {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]\n",
        "\n",
        "\n",
        "compra_de_casa(inmuebles, 100000)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "19wToAnuihT6",
        "outputId": "c0a4a365-0689-4142-ab34-e568cca81137"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[{'año': 1980,\n",
              "  'garaje': False,\n",
              "  'habitaciones': 4,\n",
              "  'metros': 120,\n",
              "  'precio': 82600.0,\n",
              "  'zona': 'A'},\n",
              " {'año': 2015,\n",
              "  'garaje': False,\n",
              "  'habitaciones': 2,\n",
              "  'metros': 90,\n",
              "  'precio': 94000.0,\n",
              "  'zona': 'A'}]"
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Ejercicio 11\n",
        "# Escribir una función que reciba una muestra de números y devuelva los valores \n",
        "# atípicos, es decir, los valores cuya puntuación típica sea mayor que 3 o menor \n",
        "# que -3. Nota: La puntuación típica de un valor se obtiene restando la media y \n",
        "# dividiendo por la desviación típica de la muestra.\n",
        "\n",
        "# Usaré esta muestra de números: 108, 31, 75, 87, 79, 88, 89, 118, 51, 89, 174, 95, 51, 70 y 73.\n",
        "\n",
        "import statistics as st\n",
        "\n",
        "\n",
        "\n",
        "def valores_atipicos(list_of_numbers):\n",
        "  list_of_numbers = sorted(list_of_numbers)\n",
        "  mediana = st.median(list_of_numbers)\n",
        "\n",
        "  m1 = list_of_numbers[:list_of_numbers.index(mediana)]\n",
        "  median_m1 = st.median(m1)\n",
        "\n",
        "  m2 = list_of_numbers[list_of_numbers.index(mediana) + 1:]\n",
        "  median_m2 = st.median(m2)\n",
        "\n",
        "  atipico_barrier = (1.5 * (median_m2 - median_m1)) + median_m2\n",
        "  atipicos_list = []\n",
        "\n",
        "  for a in list_of_numbers:\n",
        "    if a > atipico_barrier:\n",
        "      atipicos_list.append(a)\n",
        "\n",
        "  return atipicos_list\n",
        "\n",
        "\n",
        "my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1000]\n",
        "\n",
        "print(valores_atipicos(my_list))\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0-IVnAudsS7C",
        "outputId": "45a0aeb5-37c4-46cb-94bb-fcf92f8d9300"
      },
      "execution_count": 51,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1000]\n"
          ]
        }
      ]
    }
  ]
}