import psycopg2
from dotenv import load_dotenv
import os
from faker import Faker
from random import randint, choice, uniform
from datetime import datetime
import re


def limpar_texto(texto):
    if texto is None:
        return ""
    texto = texto.replace("'", "")
    texto = re.sub(r'[^\w\s]', '', texto)
    return texto


faker = Faker('pt_BR')

generos_musicais = ['Pop', 'Rock', 'Hip Hop', 'Jazz', 'Clássica', 'Eletrônica', 'Reggae', 'Samba', 'MPB', 'Sertanejo']
planos = ['Grátis', 'Premium', 'Familia', 'Estudante']
dispositivos = ['Smartphone', 'Computador', 'Tablet', 'Smart TV', 'Smart Speaker']

usuarios = []
artistas = []
albuns = []
musicas = []
playlists = []
avaliacoes = []
reproducoes = []


def insertPlanos():
    for plano in planos:
        preco = round(uniform(5.99, 19.99), 2) if plano != 'Grátis' else 0.0
        cursor.execute(f"INSERT INTO planos (nome, preco) VALUES ('{plano}', {preco});")
        print(f"Plano {plano} inserido com preço {preco}.")


def insertUsuarios():
    for _ in range(50):
        nome = limpar_texto(faker.name())
        email = limpar_texto(faker.email()) + str(randint(100, 999)) + "@exemplo.com"
        senha = limpar_texto(faker.password())
        data_nascimento = faker.date_of_birth(minimum_age=18, maximum_age=65)
        plano = choice(planos)
        cursor.execute(
            f"INSERT INTO usuarios (nome, email, senha, data_nascimento, plano_id) VALUES ('{nome}', '{email}', '{senha}', '{data_nascimento}', (SELECT id_plano FROM planos WHERE nome = '{plano}' LIMIT 1));")
        usuarios.append([nome, email, plano])
        print(f"Usuário {nome} inserido com e-mail {email}.")


def insertArtistas():
    for _ in range(20):
        nome = limpar_texto(faker.name() + " " + faker.word())
        nacionalidade = limpar_texto(faker.country())
        cursor.execute(f"INSERT INTO artistas (nome, nacionalidade) VALUES ('{nome}', '{nacionalidade}');")
        artistas.append([nome, nacionalidade])
        print(f"Artista {nome} inserido.")


def insertAlbuns():
    for artista in artistas:
        for _ in range(randint(1, 3)):
            titulo = limpar_texto(
                faker.word() + "_" + str(randint(1000, 9999)))
            ano_lancamento = randint(1990, 2025)
            cursor.execute(
                f"INSERT INTO albuns (titulo, ano_lancamento, id_artista) VALUES ('{titulo}', {ano_lancamento}, (SELECT id_artista FROM artistas WHERE nome = '{artista[0]}' LIMIT 1));")
            albuns.append([titulo, ano_lancamento, artista[0]])
            print(f"Álbum {titulo} do artista {artista[0]} inserido.")


def insertMusicas():
    for album in albuns:
        for _ in range(randint(5, 12)):
            titulo = limpar_texto(
                faker.word() + "_" + str(randint(1000, 9999)))
            duracao = str(randint(3, 5)) + ":" + str(randint(0, 59)).zfill(2)
            genero = choice(generos_musicais)
            cursor.execute(
                f"INSERT INTO musicas (titulo, duracao, genero, id_album) VALUES ('{titulo}', '{duracao}', '{genero}', (SELECT id_album FROM albuns WHERE titulo = '{album[0]}' LIMIT 1));")
            musicas.append([titulo, duracao, genero, album[0]])
            print(f"Música {titulo} inserida no álbum {album[0]}.")


def insertPlaylists():
    for usuario in usuarios:
        nome_playlist = limpar_texto(
            faker.word() + "_" + str(randint(1000, 9999)))
        data_criacao = faker.date_this_decade()
        cursor.execute(
            f"INSERT INTO playlists (nome, id_usuario, data_criacao) VALUES ('{nome_playlist}', (SELECT id_usuario FROM usuarios WHERE email = '{usuario[1]}' LIMIT 1), '{data_criacao}');")
        playlists.append([nome_playlist, usuario[1], data_criacao])
        print(f"Playlist {nome_playlist} criada para o usuário {usuario[0]}.")


def insertMusicasPlaylists():
    for playlist in playlists:
        musica = choice(musicas)
        ordem = randint(1, 20)
        cursor.execute(
            f"INSERT INTO musicas_playlists (id_musica, id_playlist, ordem) VALUES ((SELECT id_musica FROM musicas WHERE titulo = '{musica[0]}' LIMIT 1), (SELECT id_playlist FROM playlists WHERE nome = '{playlist[0]}' LIMIT 1), {ordem});")
        print(f"Música {musica[0]} adicionada na playlist {playlist[0]}.")


def insertReproducoes():
    for usuario in usuarios:
        for _ in range(randint(10, 50)):
            musica = choice(musicas)
            dispositivo = choice(dispositivos)
            data_hora = faker.date_time_this_year()
            cursor.execute(
                f"INSERT INTO reproducoes (id_usuario, id_musica, data_hora, dispositivo) VALUES ((SELECT id_usuario FROM usuarios WHERE email = '{usuario[1]}' LIMIT 1), (SELECT id_musica FROM musicas WHERE titulo = '{musica[0]}' LIMIT 1), '{data_hora}', '{dispositivo}');")
            reproducoes.append([usuario[0], musica[0], data_hora, dispositivo])
            print(f"Reprodução da música {musica[0]} realizada pelo usuário {usuario[0]}.")


def insertAvaliacoes():
    for usuario in usuarios:
        for _ in range(randint(5, 15)):
            musica = choice(musicas)
            nota = randint(1, 5)
            comentario = limpar_texto(faker.sentence())
            data_avaliacao = faker.date_time_this_year()
            cursor.execute(
                f"INSERT INTO avaliacoes (id_usuario, id_musica, nota, comentario, data_avaliacao) VALUES ((SELECT id_usuario FROM usuarios WHERE email = '{usuario[1]}' LIMIT 1), (SELECT id_musica FROM musicas WHERE titulo = '{musica[0]}' LIMIT 1), {nota}, '{comentario}', '{data_avaliacao}');")
            avaliacoes.append([usuario[0], musica[0], nota, comentario, data_avaliacao])
            print(f"Avaliação da música {musica[0]} realizada pelo usuário {usuario[0]} com nota {nota}.")



load_dotenv("variables.env")
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

try:
    connection = psycopg2.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        dbname=DBNAME
    )

    # Create a cursor to execute SQL queries
    cursor = connection.cursor()

    # Clear tables before inserting new data
    cursor.execute("TRUNCATE TABLE planos RESTART IDENTITY CASCADE;")
    cursor.execute("TRUNCATE TABLE usuarios RESTART IDENTITY CASCADE;")
    cursor.execute("TRUNCATE TABLE artistas RESTART IDENTITY CASCADE;")
    cursor.execute("TRUNCATE TABLE albuns RESTART IDENTITY CASCADE;")
    cursor.execute("TRUNCATE TABLE musicas RESTART IDENTITY CASCADE;")
    cursor.execute("TRUNCATE TABLE playlists RESTART IDENTITY CASCADE;")
    cursor.execute("TRUNCATE TABLE musicas_playlists RESTART IDENTITY CASCADE;")
    cursor.execute("TRUNCATE TABLE reproducoes RESTART IDENTITY CASCADE;")
    cursor.execute("TRUNCATE TABLE avaliacoes RESTART IDENTITY CASCADE;")

    # Insert data into the database
    insertPlanos()
    insertUsuarios()
    insertArtistas()
    insertAlbuns()
    insertMusicas()
    insertPlaylists()
    insertMusicasPlaylists()
    insertReproducoes()
    insertAvaliacoes()
    connection.commit()

    # Close the cursor and connection
    cursor.close()
    connection.close()
    print("Connection closed.")

except Exception as e:
    print(f"Failed to connect: {e}")
