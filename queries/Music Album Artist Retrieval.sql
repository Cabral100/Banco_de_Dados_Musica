SELECT m.titulo AS musica, a.titulo AS album, ar.nome AS artista
FROM musicas m
JOIN albuns a ON m.id_album = a.id_album
JOIN artistas ar ON a.id_artista = ar.id_artista;
