from app import app
from flask import render_template, request
import Form_python
import Ciphers

NUMBER_OF_DECRYPTIONS = 26



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ciphers/', methods=['GET', 'POST'])
def index1():
    form = Form_python.LoginForm()
    if form.validate_on_submit():
        try:
            text = form.text.data
            key = form.key.data
            if form.cript.data == "encrypt":
                if key.isalpha():
                    sp = str(key)
                    character = Ciphers.Cipher()
                    result = character.encrypt_vigenere(sp, text)
                else:
                    try:
                        sp_int = int(key)
                    except Exception:
                        result = "Неверный формат ключа. Введите слово или число "
                    else:
                        sp_int = sp_int % NUMBER_OF_DECRYPTIONS
                        character = Ciphers.Cipher()
                        result = character.encrypt_caesar(text, sp_int)
            elif form.cript.data == "decrypt":
                if key.isalpha():
                    sp = str(key)
                    character = Ciphers.Cipher()
                    result = character.decrypt_vigenere(sp, text)
                else:
                    try:
                        sp_int = int(key)
                    except Exception:
                        result = "Неверный формат ключа. Введите слово или число "
                    else:
                        sp_int = sp_int % NUMBER_OF_DECRYPTIONS
                        character = Ciphers.Cipher()
                        result = character.decrypt_caesar(text, sp_int)
            elif form.cript.data == "hack":
                result = Ciphers.main(text)

        except ValueError:
            result = 'Error'  # Хочу выводить сообщение об ошибке
    else:
        result = 'Not submitted'
    return render_template('index_posts.html',  form=form, result=result)
