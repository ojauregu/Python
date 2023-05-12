from flask import Flask, jsonify, request,send_file




print('hola')
import json
'''
numero =  input ('dame un numero: ')
numero = int(numero)

print('hola', numero)
'''

jsonData = '{"name": "Frank", "age": 39}'
jsonToPython = json.loads(jsonData)

print(jsonToPython)


pythonDictionary = {'name':'Bob', 'age':44, 'isEmployed':True}
dictionaryToJson = json.dumps(pythonDictionary)

print(dictionaryToJson)