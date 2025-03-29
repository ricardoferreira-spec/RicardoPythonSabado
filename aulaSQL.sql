----- DDL - Data Definition Language
----- Criar um banco de dados
-------- CREATE database pythonsabado;
/*
USE pythonsabado;
CREATE TABLE clientes (
	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, 
	nome VARCHAR(100),
	idade INT
);
*/
-------- INSERT INTO clientes (nome, idade) values ('pafuncio',32);
-------- INSERT INTO clientes (nome, idade) values ('matheus',19), ('ichizack',20), ('ronaldo',47);
-------- atalho para executar a query Cntrl + shift + enter
select * from clientes;
-------- excluir apenas o cliente da linha 1
-------- DELETE FROM clientes WHERE ID = 1;

/*
USE pythonsabado;
CREATE TABLE Pedido(
	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, 
);
*/

/*
USE pythonsabado;
CREATE TABLE Produto(
	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, 
);
*/


CREATE DATABASE passay_database;

USE passay_database;

CREATE TABLE produtos (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    preco int
);

select * from produtos;



