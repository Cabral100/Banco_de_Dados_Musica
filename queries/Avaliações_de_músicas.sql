SELECT u.nome AS usuario, m.titulo AS musica, a.nota, a.comentario, a.data_avaliacao
FROM avaliacoes a
JOIN usuarios u ON a.id_usuario = u.id_usuario
JOIN musicas m ON a.id_musica = m.id_musica
WHERE a.comentario IS NOT NULL
ORDER BY a.data_avaliacao DESC;
