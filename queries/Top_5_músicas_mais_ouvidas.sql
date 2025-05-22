SELECT m.titulo, COUNT(r.id_reproducao) AS total_reproducoes
FROM musicas m
JOIN reproducoes r ON m.id_musica = r.id_musica
GROUP BY m.titulo
ORDER BY total_reproducoes DESC --do maior ao menor
LIMIT 5;   
