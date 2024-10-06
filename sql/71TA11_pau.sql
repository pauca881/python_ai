CREATE DATABASE IF NOT EXISTS gardface;

USE gardface;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    nickname VARCHAR(50) NOT NULL UNIQUE,
    name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    born_date DATE NOT NULL
);

INSERT INTO users (email, password, nickname, name, last_name, born_date) VALUES
('usuario1@example.com', 'contraseña1', 'nick1', 'Juan', 'Pérez', '1990-01-15'),
('usuario2@example.com', 'contraseña2', 'nick2', 'Ana', 'Gómez', '1992-02-20'),
('usuario3@example.com', 'contraseña3', 'nick3', 'Luis', 'Martínez', '1988-03-30'),
('usuario4@example.com', 'contraseña4', 'nick4', 'María', 'Hernández', '1995-04-10'),
('usuario5@example.com', 'contraseña5', 'nick5', 'Carlos', 'López', '1985-05-25'),
('usuario6@example.com', 'contraseña6', 'nick6', 'Laura', 'Sánchez', '1991-06-05'),
('usuario7@example.com', 'contraseña7', 'nick7', 'Jorge', 'Ramírez', '1980-07-14'),
('usuario8@example.com', 'contraseña8', 'nick8', 'Clara', 'Torres', '1993-08-22'),
('usuario9@example.com', 'contraseña9', 'nick9', 'David', 'Vázquez', '1987-09-30'),
('usuario10@example.com', 'contraseña10', 'nick10', 'Isabel', 'Morales', '1994-10-12');

-- Otras tablas

CREATE TABLE IF NOT EXISTS insignias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    fecha_obtencion DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Insertar datos en la tabla insignias
INSERT INTO insignias (user_id, nombre, descripcion, fecha_obtencion) VALUES
(1, 'Insignia de Novato', 'Otorgada por completar el registro.', '2023-10-01'),
(1, 'Insignia de Explorador', 'Otorgada por explorar el sitio.', '2023-10-02'),
(2, 'Insignia de Participante', 'Otorgada por participar en foros.', '2023-10-03'),
(3, 'Insignia de Colaborador', 'Otorgada por contribuir con contenido.', '2023-10-04'),
(4, 'Insignia de Maestro', 'Otorgada por completar un curso.', '2023-10-05'),
(5, 'Insignia de Experto', 'Otorgada por responder preguntas.', '2023-10-06'),
(6, 'Insignia de Amistad', 'Otorgada por hacer una donación.', '2023-10-07'),
(7, 'Insignia de Amistad', 'Otorgada por referir a un amigo.', '2023-10-08'),
(8, 'Insignia de Logros', 'Otorgada por alcanzar metas.', '2023-10-09'),
(9, 'Insignia de Creatividad', 'Otorgada por proyectos creativos.', '2023-10-10');


CREATE TABLE IF NOT EXISTS card_game (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    fecha_obtencion DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Insertar datos en la tabla card_game
INSERT INTO card_game (user_id, tipo, nombre, descripcion, fecha_obtencion) VALUES
(1, 'Persona Famosa', 'Albert Einstein', 'Físico teórico, conocido por la teoría de la relatividad.', '2023-10-01'),
(1, 'Videojuego', 'The Legend of Zelda', 'Un videojuego de aventuras y exploración.', '2023-10-02'),
(2, 'Persona Famosa', 'Marie Curie', 'Pionera en el campo de la radiactividad.', '2023-10-03'),
(3, 'Videojuego', 'Super Mario Bros', 'Clásico juego de plataformas.', '2023-10-04'),
(4, 'Persona Famosa', 'Leonardo da Vinci', 'Artista, inventor y científico renacentista.', '2023-10-05'),
(5, 'Videojuego', 'Minecraft', 'Juego de construcción y aventura en un mundo abierto.', '2023-10-06'),
(6, 'Persona Famosa', 'Isaac Newton', 'Matemático y físico, conocido por sus leyes del movimiento.', '2023-10-07'),
(7, 'Videojuego', 'The Witcher 3', 'Juego de rol aclamado por la crítica.', '2023-10-08'),
(8, 'Persona Famosa', 'Frida Kahlo', 'Pintora mexicana famosa por sus autorretratos.', '2023-10-09'),
(9, 'Videojuego', 'Portal', 'Juego de rompecabezas en primera persona.', '2023-10-10');


-- Consultas 
-- Mostrar usuarios que han nacido antes del 1990
Select *
from users
WHERE born_date < '1990-01-01';

-- Mostrar todas las insignias de Amistad
Select *
from insignias
where nombre LIKE '%amistad%';

-- Mostrar todos las cartas de una personas famosa
Select *
from card_game
where tipo LIKE '%famosa%';

-- Mostrar tabla los usuarios con sus insignias
SELECT 
u.nickname,
i.nombre AS insignia_nombre,
i.descripcion
FROM 
users u
left JOIN 
insignias i ON u.id = i.user_id
ORDER BY 
u.id, i.fecha_obtencion;

-- Mostrar las cartas que tiene cada usuario
-- 
select
u.nickname,
c.nombre as Carta,
c.tipo,
c.descripcion
from users u 
right join card_game c ON u.id = c.user_id;

-- Mostrar los usuarios con todas sus ( numero total ) insignias, y sus cartas
select u.nickname,
count(i.user_id) as numero_insignias,
count(c.id) as numero_cartas,
group_concat(i.nombre	SEPARATOR ', ') as insignias,
group_concat(c.nombre	SEPARATOR ', ') as cartas
from users u
right join insignias i on u.id = i.user_id
right join card_game c on u.id = i.user_id
group by u.id;




