SELECT u.nome , COUNT(p.id_playlist) AS total_playlists

FROM usuarios u
JOIN playlists p ON u.id_usuario = p.id_usuario
GROUP BY u.nome
ORDER BY total_playlists DESC;
