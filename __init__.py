from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  

key = Fernet.generate_key()
f = Fernet(key)

@app.route('/')
def hello_world():
    return render_template('hello.html') #COMMENTAIRE

key = Fernet.generate_key()
f = Fernet(key)

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str

#Exercice 5.1
@app.route('/decrypt/<string:valeur>')
def decryptage(valeur):
    try:
        valeur_bytes = valeur.encode()
        decrypted = f.decrypt(valeur_bytes)
        return f"Valeur décryptée : {decrypted.decode()}"
    except Exception as e:
        return f"Erreur lors du déchiffrement : {str(e)}"

#Exercice 5.2
@app.route('/encrypt_key/<string:key>/<string:valeur>')
def encrypt_with_key(key, valeur):
    try:
        f_custom = Fernet(key.encode())
        token = f_custom.encrypt(valeur.encode())
        return f"Valeur encryptée avec votre clé : {token.decode()}"
    except Exception as e:
        return f"Erreur d'encryption avec votre clé : {str(e)}"

@app.route('/decrypt_key/<string:key>/<string:valeur>')
def decrypt_with_key(key, valeur):
    try:
        f_custom = Fernet(key.encode())
        decrypted = f_custom.decrypt(valeur.encode())
        return f"Valeur décryptée avec votre clé : {decrypted.decode()}"
    except Exception as e:
        return f"Erreur de déchiffrement avec votre clé : {str(e)}"

if __name__ == "__main__":
  app.run(debug=True)
