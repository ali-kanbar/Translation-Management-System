from flask import Flask,render_template,url_for,redirect,request,flash,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String,Integer
from sqlalchemy.orm import mapped_column,DeclarativeBase,Mapped
import os

class Base(DeclarativeBase):
    pass

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URI")
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Translations(db.Model):
    id : Mapped[int] = mapped_column(Integer, primary_key = True,autoincrement = True)
    initial_word : Mapped[str] = mapped_column(String,nullable=False,unique=True)
    translated_word : Mapped[str] = mapped_column(String,nullable=False)

with app.app_context():
    db.create_all()

@app.route("/")
def initial_page():
    return redirect(url_for("home"))

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/submit_word", methods=["POST"])
def add_word():
    word = request.form.get("word")
    translation = request.form.get("translation")
    if not word or not translation:
        flash("Word and Translation are required", "error")
        return redirect(url_for("add"))
    
    with app.app_context():
        query = db.select(Translations).where(Translations.initial_word == word)
        result = db.session.execute(query)
        if len(result.scalars().all()) == 0:
            new_word = Translations(initial_word=word, translated_word=translation)
            db.session.add(new_word)
            db.session.commit()
            flash("New word has been added", "success")
        else:
            flash("The word already exists", "error")
    return redirect(url_for("add"))

@app.route("/translate")
def translate():
    translated_word = session.pop('translated_word', "")
    original_word = session.pop('original_word', "")
    return render_template("translate.html",translated_word = translated_word,original_word=original_word)

@app.route("/translate_word",methods=["GET", "POST"])
def translate_word():
    word = request.form.get("word")
    translated_word = ""
    if not word:
        flash("Word is required", "error")
        return redirect(url_for("translate"))
    with app.app_context():
        query = db.select(Translations.translated_word).where(Translations.initial_word == word)
        result = db.session.execute(query)
        translations = result.scalars().all()
        if len(translations) == 0:
            flash("Your word doesn't exist in the database", "error")
        else:
            translated_word = translations[0]
            session['translated_word'] = translated_word
            session['original_word'] = word
    return redirect(url_for("translate"))

@app.route("/update")
def update():
    return render_template("update_word.html")

@app.route("/update_translation",methods=["GET","POST"])
def update_translation():
    word = request.form.get("word")
    updated_translation = request.form.get("updated_translation")
    if not word or not updated_translation:
        flash("Word and Updated_Translation are required", "error")
        return redirect(url_for("update"))
    with app.app_context():
        query = db.select(Translations).where(Translations.initial_word == word)
        result = db.session.execute(query)
        translation = result.scalars().first()
        if not translation:
            flash("Your word doesn't exist in the database", "error")
        else:
            translation.translated_word = updated_translation
            db.session.commit()
            flash("Translation updated successfully", "success")
    return redirect(url_for("update"))

@app.route("/delete")
def delete():
    return render_template("delete.html")

@app.route("/delete_word",methods=["GET","POST"])
def delete_word():
    word = request.form.get("word")
    if not word:
        flash("Word is required", "error")
        return redirect(url_for("delete"))
    with app.app_context():
        query = db.select(Translations).where(Translations.initial_word == word)
        result = db.session.execute(query)
        translation = result.scalars().first()
        if not translation:
            flash("Your word doesn't exist in the database", "error")
        else:
            db.session.delete(translation)
            db.session.commit()
            flash("Word deleted successfully", "success")
    return redirect(url_for("delete"))

app.run()