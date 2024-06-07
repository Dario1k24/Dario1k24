
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

"""
    Nom : films_genres_afficher
    Auteur : OM 2021.05.01
    Définition d'une "route" /films_genres_afficher

    But : Afficher les films avec les genres associés pour chaque film.

    Paramètres : id_genre_sel = 0 >> tous les films.
                 id_genre_sel = "n" affiche le film dont l'id est "n"

"""


@app.route("/films_afficher/<int:id_film_sel>", methods=['GET', 'POST'])
def films_afficher(id_film_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                strsql_genres_films_afficher_data = """SELECT
                                                        c.ID_fournisseur, p.ID_produit, c.nom_fournisseur, c.adresse_fournisseur, c.numero_telephone_fournisseur, p.nom_produit, p.description_produit, p.poids_produit, p.prix_produit
                                                        FROM t_fournisseur c
                                                        LEFT JOIN t_produit p ON c.ID_produit = p.ID_produit
                                                        LEFT JOIN t_fournisseur_produit sc ON c.ID_fournisseur = sc.ID_fournisseur"""
                if id_film_sel == 0:
                    # le paramètre 0 permet d'afficher tous les films
                    # Sinon le paramètre représente la valeur de l'id du film
                    mc_afficher.execute(strsql_genres_films_afficher_data)
                else:
                    # Constitution d'un dictionnaire pour associer l'id du film sélectionné avec un nom de variable
                    valeur_id_film_selected_dictionnaire = {"value_id_film_selected": id_film_sel}
                    # En MySql l'instruction HAVING fonctionne comme un WHERE... mais doit être associée à un GROUP BY
                    # L'opérateur += permet de concaténer une nouvelle valeur à la valeur de gauche préalablement définie.
                    strsql_genres_films_afficher_data += """ HAVING ID_fournisseur= %(value_id_film_selected)s"""

                    mc_afficher.execute(strsql_genres_films_afficher_data, valeur_id_film_selected_dictionnaire)

                # Récupère les données de la requête.
                data_genres_films_afficher = mc_afficher.fetchall()
                print("data_genres ", data_genres_films_afficher, " Type : ", type(data_genres_films_afficher))

                # Différencier les messages.
                if not data_genres_films_afficher and id_film_sel == 0:
                    flash("""La table "t_film" est vide. !""", "warning")
                elif not data_genres_films_afficher and id_film_sel > 0:
                    # Si l'utilisateur change l'id_film dans l'URL et qu'il ne correspond à aucun film
                    flash(f"Le film {id_film_sel} demandé n'existe pas !!", "warning")
                else:
                    flash(f"Données sur les fournisseurs affichés", "success")

        except Exception as Exception_films_genres_afficher:
            raise ExceptionFilmsGenresAfficher(f"fichier : {Path(__file__).name}  ;  {films_afficher.__name__} ;"
                                               f"{Exception_films_genres_afficher}")

    print("films_afficher  ", data_genres_films_afficher)
    # Envoie la page "HTML" au serveur.
    return render_template("films/films_afficher.html", data=data_genres_films_afficher)

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
                    "Value_telephone": numero_telephone_fournisseur_add_wtf,
                }
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_film = """INSERT INTO t_fournisseur (ID_fournisseur, nom_fournisseur, adresse_fournisseur, numero_telephone_fournisseur) VALUES (NULL, %(value_nom_film)s, %(value_adresse)s, %(Value_telephone)s)"""
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_film, valeurs_insertion_dictionnaire)

                flash("Données insérées !!", "success")
                print("Données insérées !!")

                # Redirection vers le bon endpoint avec le bon paramètre
                return redirect(url_for('films_afficher', id_film_sel=0))

        except Exception as Exception_fournisseur_ajouter_wtf:
            raise ExceptionGenresAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{film_add_wtf.__name__} ; "
                                            f"{Exception_fournisseur_ajouter_wtf}")

    return render_template("films/film_add_wtf.html", form_add_film=form_add_film)

"""Editer(update) un film qui a été sélectionné dans le formulaire "fournisseur_produit_afficher.html"
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
    id_film_update = request.values.get('id_film_btn_edit_html')  # Utilisation de get() pour éviter les erreurs KeyError
    form_update_film = FormWTFUpdateFilm()
    try:
        if request.method == "POST" and form_update_film.submit.data:
            nom_fournisseur_update = form_update_film.nom_fournisseur_update.data
            adresse_fournisseur_update = form_update_film.adresse_fournisseur_update.data
            numero_telephone_fournisseur_update = form_update_film.numero_telephone_fournisseur_update.data

            valeur_update_dictionnaire = {
                "value_id_film": id_film_update,
                "value_nom_film": nom_fournisseur_update,
                "value_adresse_fournisseur": adresse_fournisseur_update,
                "value_numero_telephone_fournisseur": numero_telephone_fournisseur_update,
            }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_nom_film = """UPDATE t_fournisseur SET nom_fournisseur = %(value_nom_film)s,
                                                            adresse_fournisseur = %(value_adresse_fournisseur)s,
                                                            numero_telephone_fournisseur = %(value_numero_telephone_fournisseur)s
                                                            WHERE ID_fournisseur = %(value_id_film)s"""
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_nom_film, valeur_update_dictionnaire)

            flash("Donnée mise à jour !!", "success")
            print("Donnée mise à jour !!")

            return redirect(url_for('films_afficher', id_film_sel=0))
        elif request.method == "GET":
            if id_film_update:  # Vérification si l'ID du film est présent
                str_sql_id_film = "SELECT * FROM t_fournisseur WHERE ID_fournisseur = %(value_id_film)s"
                valeur_select_dictionnaire = {"value_id_film": id_film_update}
                with DBconnection() as mybd_conn:
                    mybd_conn.execute(str_sql_id_film, valeur_select_dictionnaire)
                    data_film = mybd_conn.fetchone()
                    print("data_film ", data_film, " type ", type(data_film))

                    # Assurez-vous que les noms des champs dans le formulaire correspondent exactement aux attributs du formulaire
                    form_update_film.nom_fournisseur_update.data = data_film["nom_fournisseur"]
                    form_update_film.adresse_fournisseur_update.data = data_film["adresse_fournisseur"]
                    form_update_film.numero_telephone_fournisseur_update.data = data_film["numero_telephone_fournisseur"]

    except Exception as Exception_film_update_wtf:
        raise ExceptionFilmUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                     f"{film_update_wtf.__name__} ; "
                                     f"{Exception_film_update_wtf}")

    return render_template("films/film_update_wtf.html", form_update_film=form_update_film)

"""Effacer(delete) un film qui a été sélectionné dans le formulaire "fournisseur_produit_afficher.html"
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
    id_film_delete = request.values.get('id_film_btn_delete_html')
    form_delete_film = FormWTFDeleteFilm()

    try:
        if form_delete_film.submit_btn_annuler.data:
            return redirect(url_for("films_afficher", id_film_sel=0))

        if form_delete_film.submit_btn_conf_del_film.data:
            # Affiche un message Flash pour confirmer la suppression
            flash("Voulez-vous vraiment supprimer ce film ?", "warning")
            btn_submit_del = True

        if form_delete_film.submit_btn_del_film.data:
            # Vérifie si l'ID du film à supprimer est disponible
            if id_film_delete:
                valeur_delete_dictionnaire = {"value_id_film": id_film_delete}

                # Exécute la requête SQL pour supprimer le film de la base de données
                str_sql_delete_film = """DELETE FROM t_fournisseur WHERE ID_fournisseur = %(value_id_film)s"""
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_film, valeur_delete_dictionnaire)

                # Affiche un message Flash pour indiquer que le film a été supprimé avec succès
                flash("Film définitivement effacé !!", "success")
                print("Film définitivement effacé !!")

                # Redirige vers la page affichant tous les films
                return redirect(url_for('films_afficher', id_film_sel=0))
            else:
                # Si l'ID du film à supprimer est manquant, affiche un message d'avertissement
                flash("Impossible de trouver l'ID du film à supprimer.", "warning")

        if request.method == "GET":
            if id_film_delete:
                # Récupère les données du film à supprimer
                valeur_select_dictionnaire = {"value_id_film": id_film_delete}
                str_sql_genres_films_delete = """SELECT * FROM t_fournisseur WHERE ID_fournisseur = %(value_id_film)s"""
                with DBconnection() as mydb_conn:
                    mydb_conn.execute(str_sql_genres_films_delete, valeur_select_dictionnaire)
                    data_film_delete = mydb_conn.fetchall()
                    print("data_film_delete...", data_film_delete)
                    session['data_film_delete'] = data_film_delete

                if not data_film_delete:
                    # Affiche un message d'avertissement si aucun film n'est trouvé avec l'ID donné
                    flash("Aucun film trouvé avec cet ID.", "warning")
                    return redirect(url_for("films_afficher", id_film_sel=0))

            btn_submit_del = False

    except Exception as Exception_fournisseur_delete_wtf:
        # Gère les exceptions et les erreurs
        raise ExceptionFilmDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                     f"{film_delete_wtf.__name__} ; "
                                     f"{Exception_fournisseur_delete_wtf}")

    # Rend le modèle HTML avec les données récupérées et les messages Flash
    return render_template("films/film_delete_wtf.html",
                           form_delete_film=form_delete_film,
                           btn_submit_del=btn_submit_del,
                           data_film_del=data_film_delete)
