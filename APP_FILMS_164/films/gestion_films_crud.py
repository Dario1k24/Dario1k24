
"""Gestion des "routes" FLASK et des données pour les films.
Fichier : gestion_films_crud.py
Auteur : OM 2022.04.11
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for

from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.films.gestion_films_wtf_forms import FormWTFUpdateFilm, FormWTFAddFilm, FormWTFDeleteFilm

"""Ajouter un film grâce au formulaire "film_add_wtf.html"
Auteur : OM 2022.04.11
Définition d'une "route" /film_add

Test : exemple: cliquer sur le menu "Films/Genres" puis cliquer sur le bouton "ADD" d'un "film"

Paramètres : sans


Remarque :  Dans le champ "nom_film_update_wtf" du formulaire "films/films_update_wtf.html",
            le contrôle de la saisie s'effectue ici en Python dans le fichier ""
            On ne doit pas accepter un champ vide.
"""


@app.route("/film_add", methods=['GET', 'POST'])
def film_add_wtf():
    form_add_film = FormWTFAddFilm()
    if request.method == "POST":
        try:
            if form_add_film.validate_on_submit():
                nom_fournisseur_add_wtf = form_add_film.nom_fournisseur_add_wtf.data
                adresse_fournisseur_add_wtf = form_add_film.adresse_fournisseur_add_wtf.data
                numero_telephone_fournisseur_add_wtf = form_add_film.numero_telephone_fournisseur_add_wtf.data

                valeurs_insertion_dictionnaire = {
                    "value_nom_film": nom_fournisseur_add_wtf,
                    "value_adresse": adresse_fournisseur_add_wtf,
                    "Value_telephone": numero_telephone_fournisseur_add_wtf
                }
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_film = """INSERT INTO t_fournisseur (ID_fournisseur, nom_fournisseur, adresse_fournisseur, numero_telephone_fournisseur) VALUES (NULL, %(value_nom_film)s, %(value_adresse)s, %(Value_telephone)s)"""
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_film, valeurs_insertion_dictionnaire)

                flash("Données insérées !!", "success")
                print("Données insérées !!")

                return redirect(url_for('films_genres_afficher'))

        except Exception as Exception_genres_ajouter_wtf:
            raise ExceptionGenresAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{film_add_wtf.__name__} ; "
                                            f"{Exception_genres_ajouter_wtf}")

    return render_template("films/film_add_wtf.html", form_add_film=form_add_film)

"""Editer(update) un film qui a été sélectionné dans le formulaire "films_genres_afficher.html"
Auteur : OM 2022.04.11
Définition d'une "route" /film_update

Test : exemple: cliquer sur le menu "Films/Genres" puis cliquer sur le bouton "EDIT" d'un "film"

Paramètres : sans

But : Editer(update) un genre qui a été sélectionné dans le formulaire "genres_afficher.html"

Remarque :  Dans le champ "nom_film_update_wtf" du formulaire "films/films_update_wtf.html",
            le contrôle de la saisie s'effectue ici en Python.
            On ne doit pas accepter un champ vide.
"""

@app.route("/film_update", methods=['GET', 'POST'])
def film_update_wtf():
    id_film_update = request.values['id_film_btn_edit_html']
    form_update_film = FormWTFUpdateFilm()
    try:
        if request.method == "POST" and form_update_film.submit.data:
            nom_fournissuer_update = form_update_film.nom_fournissuer_update.data
            adresse_fournisseur_update = form_update_film.adresse_fournisseur_update.data
            numero_telephone_fournisseur_update = form_update_film.numero_telephone_fournisseur_update.data


            valeur_update_dictionnaire = {
                "value_id_film": id_film_update,
                "value_nom_film": nom_fournissuer_update,
                "value_adresse_fournisseur": adresse_fournisseur_update,
                "value_numero_telephone_fournisseur": numero_telephone_fournisseur_update,
            }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_nom_film = """UPDATE t_fournisseur SET nom_fournisseur = %(value_nom_film)s,
                                                        adresse_fournisseur = %(value_adresse_fournisseur)s,
                                                        numero_telephone_fournisseur = %(value_numero_telephone_fournisseur)s,
                                                        WHERE ID_fournisseur = %(value_id_film)s"""
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_nom_film, valeur_update_dictionnaire)

            flash("Donnée mise à jour !!", "success")
            print("Donnée mise à jour !!")

            return redirect(url_for('films_genres_afficher'))
        elif request.method == "GET":
            str_sql_id_film = "SELECT * FROM t_fournisseur WHERE ID_fournisseur = %(value_id_film)s"
            valeur_select_dictionnaire = {"value_id_film": id_film_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_film, valeur_select_dictionnaire)
            data_film = mybd_conn.fetchone()
            print("data_film ", data_film, " type ", type(data_film), " genre ",
                  data_film["nom_film"])

            form_update_film.nom_fournissuer_update.data = data_film["nom_film"]
            form_update_film.adresse_fournisseur_update.data = data_film["duree_film"]
            print(f" duree film  ", data_film["duree_film"], "  type ", type(data_film["duree_film"]))
            form_update_film.numero_telephone_fournisseur_update.data = data_film["description_film"]


    except Exception as Exception_film_update_wtf:
        raise ExceptionFilmUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                     f"{film_update_wtf.__name__} ; "
                                     f"{Exception_film_update_wtf}")

    return render_template("films/film_update_wtf.html", form_update_film=form_update_film)


"""Effacer(delete) un film qui a été sélectionné dans le formulaire "films_genres_afficher.html"
Auteur : OM 2022.04.11
Définition d'une "route" /film_delete

Test : ex. cliquer sur le menu "film" puis cliquer sur le bouton "DELETE" d'un "film"

Paramètres : sans

Remarque :  Dans le champ "nom_film_delete_wtf" du formulaire "films/film_delete_wtf.html"
            On doit simplement cliquer sur "DELETE"
"""


@app.route("/film_delete", methods=['GET', 'POST'])
def film_delete_wtf():
    data_film_delete = None
    btn_submit_del = None
    id_film_delete = request.values['id_film_btn_delete_html']
    form_delete_film = FormWTFDeleteFilm()
    try:
        if form_delete_film.submit_btn_annuler.data:
            return redirect(url_for("films_genres_afficher"))

        if form_delete_film.submit_btn_conf_del_film.data:
            data_film_delete = session['data_film_delete']
            print("data_film_delete ", data_film_delete)

            flash("Effacer le film de façon définitive de la BD !!!", "danger")
            btn_submit_del = True

        if form_delete_film.submit_btn_del_film.data:
            valeur_delete_dictionnaire = {"value_id_film": id_film_delete}
            print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

            str_sql_delete_fk_film_genre = """DELETE FROM t_fournisseur_produit WHERE ID_fournisseur = %(value_id_film)s"""
            str_sql_delete_film = """DELETE FROM t_fournisseur WHERE ID_fournisseur = %(value_id_film)s"""
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_delete_fk_film_genre, valeur_delete_dictionnaire)
                mconn_bd.execute(str_sql_delete_film, valeur_delete_dictionnaire)

            flash("Film définitivement effacé !!", "success")
            print("Film définitivement effacé !!")

            return redirect(url_for('films_genres_afficher'))
        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_film": id_film_delete}
            print(id_film_delete, type(id_film_delete))

            str_sql_genres_films_delete = """SELECT * FROM t_fournisseur WHERE ID_fournisseur = %(value_id_film)s"""
            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_genres_films_delete, valeur_select_dictionnaire)
                data_film_delete = mydb_conn.fetchall()
                print("data_film_delete...", data_film_delete)
                session['data_film_delete'] = data_film_delete

            btn_submit_del = False

    except Exception as Exception_film_delete_wtf:
        raise ExceptionFilmDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                     f"{film_delete_wtf.__name__} ; "
                                     f"{Exception_film_delete_wtf}")

    return render_template("films/film_delete_wtf.html",
                           form_delete_film=form_delete_film,
                           btn_submit_del=btn_submit_del,
                           data_film_del=data_film_delete
                           )
