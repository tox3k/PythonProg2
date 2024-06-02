CREATE TABLE actors (
    act_id int NOT NULL,
    act_first_name VARCHAR(255),
	act_last_name VARCHAR(255),
	act_gender VARCHAR(1),
    PRIMARY KEY ("act_id")
); 

CREATE TABLE movie (
    mov_id int NOT NULL,
	mov_title VARCHAR(255),
    PRIMARY KEY ("mov_id")
); 

CREATE TABLE director (
    dir_id int NOT NULL,
    dir_first_name VARCHAR(255),
	dir_last_name VARCHAR(255),
    PRIMARY KEY ("dir_id")
); 

CREATE TABLE movie_cast (
    act_id int,
    mov_id int,
	role VARCHAR(255),
    FOREIGN KEY (act_id) REFERENCES actors(act_id) ON DELETE CASCADE,
	FOREIGN KEY (mov_id) REFERENCES movie(mov_id) ON DELETE CASCADE
	
); 

CREATE TABLE oscar_awarded (
    award_id int,
    mov_id int,
	PRIMARY KEY ("award_id"),
    FOREIGN KEY (mov_id) REFERENCES movie(mov_id) ON DELETE SET NULL
); 

CREATE TABLE movie_direction (
    dir_id int,
    mov_id int,
    FOREIGN KEY (dir_id) REFERENCES director(dir_id) ON DELETE CASCADE,
	FOREIGN KEY (mov_id) REFERENCES movie(mov_id) ON DELETE CASCADE
	
); 