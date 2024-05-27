"""Gestion des "routes" FLASK et des données pour les genres.
Fichier : gestion_genres_crud.py
Auteur : OM 2021.03.16
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for

from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.genres.gestion_genres_wtf_forms import FormWTFAjouterGenres
from APP_FILMS_164.genres.gestion_genres_wtf_forms import FormWTFDeleteGenre
from APP_FILMS_164.genres.gestion_genres_wtf_forms import FormWTFUpdateGenre

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /genres_afficher

    Test : ex : http://127.0.0.1:5575/genres_afficher

    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_genre_sel = 0 >> tous les genres.
                id_genre_sel = "n" affiche le genre dont l'id est "n"
"""


@app.route("/genres_afficher/<string:order_by>/<int:id_genre_sel>", methods=['GET', 'POST'])
def genres_afficher(order_by, id_genre_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_genre_sel == 0:
                    strsql_genres_afficher = """SELECT * FROM t_employer ORDER BY nom_employer ASC"""
                    mc_afficher.execute(strsql_genres_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_genre"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les noms d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id du genre sélectionné avec un nom de variable
                    valeur_id_genre_selected_dictionnaire = {"value_id_genre_selected": id_genre_sel}
                    strsql_genres_afficher = """SELECT * FROM t_employer WHERE ID_employer = %(value_id_genre_selected)s"""
                    mc_afficher.execute(strsql_genres_afficher, valeur_id_genre_selected_dictionnaire)
                else:
                    strsql_genres_afficher = """SELECT * FROM t_employer ORDER BY nom_employer DESC"""

                    mc_afficher.execute(strsql_genres_afficher)

                data_genres = mc_afficher.fetchall()

                print("data_genres ", data_genres, " Type : ", type(data_genres))

                # Différencier les messages si la table est vide.
                if not data_genres and id_genre_sel == 0:
                    flash("""La table "t_genre" est vide. !!""", "warning")
                elif not data_genres and id_genre_sel > 0:
                    # Si l'utilisateur change l'id_genre dans l'URL et que le genre n'existe pas,
                    flash(f"Le genre demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_genre" est vide.
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Données genres affichés !!", "success")

        except Exception as Exception_genres_afficher:
            raise ExceptionGenresAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{genres_afficher.__name__} ; "
                                          f"{Exception_genres_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("genres/genres_afficher.html", data=data_genres)


"""
    Auteur : OM 2021.03.22
    Définition d'une "route" /genres_ajouter

    Test : ex : http://127.0.0.1:5575/genres_ajouter

    Paramètres : sans

    But : Ajouter un genre pour un film

    Remarque :  Dans le champ "name_genre_html" du formulaire "genres/genres_ajouter.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/genres_ajouter", methods=['GET', 'POST'])
def genres_ajouter_wtf():
    form = FormWTFAjouterGenres()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                name_genre_wtf = form.nom_genre_wtf.data
                name_genre = name_genre_wtf.lower()
                valeurs_insertion_dictionnaire = {"value_intitule_genre": name_genre}
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_genre = """INSERT INTO t_employer (ID_employer,nom_employer) VALUES (NULL,%(value_intitule_genre)s) """
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_genre, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
                return redirect(url_for('genres_afficher', order_by='DESC', id_genre_sel=0))

        except Exception as Exception_genres_ajouter_wtf:
            raise ExceptionGenresAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{genres_ajouter_wtf.__name__} ; "
                                            f"{Exception_genres_ajouter_wtf}")

    return render_template("genres/genres_ajouter_wtf.html", form=form)




"""
    Auteur : OM 2021.03.29
    Définition d'une "route" /genre_update

    Test : ex cliquer sur le menu "genres" puis cliquer sur le bouton "EDIT" d'un "genre"

    Paramètres : sans

    But : Editer(update) un genre qui a été sélectionné dans le formulaire "genres_afficher.html"

    Remarque :  Dans le champ "nom_genre_update_wtf" du formulaire "genres/genre_update_wtf.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/genre_update", methods=['GET', 'POST'])
def genre_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_genre"
    id_genre_update = request.values['id_genre_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update = FormWTFUpdateGenre()
    try:
        # Traitement du formulaire en cas de soumission
        if request.method == "POST" and form_update.submit.data:
            # Récupérer les données du formulaire
            name_genre_update = form_update.nom_genre_update_wtf.data
            name_genre_update = name_genre_update.lower()
            prenom_employer = form_update.prenom_employer_wtf.data

            # Créer un dictionnaire de valeurs pour la requête SQL
            valeur_update_dictionnaire = {
                "value_id_genre": id_genre_update,
                "value_name_genre": name_genre_update,
                "value_prenom_employer": prenom_employer

            }

            # Requête SQL pour mettre à jour le genre
            str_sql_update_intitulegenre = """
                UPDATE t_employer 
                SET nom_employer = %(value_name_genre)s, 
                    prenom_employer = %(value_prenom_employer)s 
                WHERE ID_employer = %(value_id_genre)s
            """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_intitulegenre, valeur_update_dictionnaire)

            # Message de succès
            flash(f"Donnée mise à jour !!", "success")

            # Redirection vers la page d'affichage des genres
            return redirect(url_for('genres_afficher', order_by="ASC", id_genre_sel=id_genre_update))

        elif request.method == "GET":
            # Récupération des données du genre à modifier depuis la base de données
            str_sql_id_genre = "SELECT * FROM t_employer WHERE ID_employer = %(value_id_genre)s"
            valeur_select_dictionnaire = {"value_id_genre": id_genre_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_genre, valeur_select_dictionnaire)
                data_nom_genre = mybd_conn.fetchone()

            # Pré-remplissage des champs du formulaire avec les données du genre
            form_update.nom_genre_update_wtf.data = data_nom_genre["nom_employer"]
            form_update.prenom_employer_wtf.data = data_nom_genre["prenom_employer"]

    except Exception as Exception_genre_update_wtf:
        # Gestion des exceptions
        raise ExceptionGenreUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{genre_update_wtf.__name__} ; "
                                      f"{Exception_genre_update_wtf}")

    # Affichage du formulaire de mise à jour du genre
    return render_template("genres/genre_update_wtf.html", form_update=form_update)




"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /genre_delete

    Test : ex. cliquer sur le menu "genres" puis cliquer sur le bouton "DELETE" d'un "genre"

    Paramètres : sans

    But : Effacer(delete) un genre qui a été sélectionné dans le formulaire "genres_afficher.html"

    Remarque :  Dans le champ "nom_genre_delete_wtf" du formulaire "genres/genre_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""



@app.route("/genre_delete", methods=['GET', 'POST'])
def genre_delete_wtf():
    form_delete = FormWTFDeleteGenre()
    data_films_attribue_genre_delete = None
    btn_submit_del = None

    try:
        if request.method == "POST":
            ID_employer_delete = request.form.get('ID_employer_btn_delete_html')
            if ID_employer_delete is None:
                raise KeyError('ID_employer_btn_delete_html')

            if request.form.get('submit_btn_annuler'):
                return redirect(url_for("genres_afficher", order_by="ASC", id_genre_sel=0))

            if request.form.get('submit_btn_conf_del'):
                # Si le formulaire est soumis avec le bouton "Confirmer la suppression"
                data_films_attribue_genre_delete = session.get('data_films_attribue_genre_delete', None)
                flash("Êtes-vous sûr de vouloir supprimer cet employer ?", "warning")
                btn_submit_del = True

            if request.form.get('submit_btn_del'):
                # Si le formulaire est soumis avec le bouton "Supprimer"
                ID_employer_delete = session.pop('ID_employer_delete', None)
                if ID_employer_delete:
                    with DBconnection() as mconn_bd:
                        str_sql_delete_employer = "DELETE FROM t_employer WHERE ID_employer = %s"
                        mconn_bd.execute(str_sql_delete_employer, (ID_employer_delete,))
                    flash("Employer définitivement effacé !!", "success")
                    return redirect(url_for('genres_afficher', order_by="ASC", id_genre_sel=0))

        elif request.method == "GET":
            ID_employer_delete = request.args.get('ID_employer_btn_delete_html')
            if ID_employer_delete is None:
                raise KeyError('ID_employer_btn_delete_html')

            str_sql_genres_employers_delete = """
                SELECT * FROM t_employer WHERE ID_employer = %s
            """
            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_genres_employers_delete, (ID_employer_delete,))
                data_films_attribue_genre_delete = mydb_conn.fetchall()
                session['data_films_attribue_genre_delete'] = data_films_attribue_genre_delete

                str_sql_id_employer = "SELECT * FROM t_employer WHERE ID_employer = %s"
                mydb_conn.execute(str_sql_id_employer, (ID_employer_delete,))
                data_nom_employer = mydb_conn.fetchone()

            form_delete.nom_genre_delete_wtf.data = data_nom_employer["nom_employer"]
            btn_submit_del = False

    except KeyError as e:
        flash(f"Erreur : clé manquante {str(e)}", "danger")
    except Exception as e:
        flash(f"Erreur générale : {str(e)}", "danger")

    return render_template("genres/genre_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_films_associes=data_films_attribue_genre_delete)

