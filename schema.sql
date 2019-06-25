CREATE TABLE "conta" (
        "codigo" serial,
	"numConta" VARCHAR(10) NOT NULL, 
	"agencia" VARCHAR(50) NOT NULL,
	"saldo" INT,
	"tipo" VARCHAR(100) NOT NULL,
	"codigoCliente" int,
	CONSTRAINT "codigoClientePK" PRIMARY KEY ("codigo"),
	CONSTRAINT "ContaFk" FOREIGN KEY ("codigoCliente")
        REFERENCES "cliente" 
        ON DELETE cascade
        ON UPDATE cascade,
	CONSTRAINT "cpfUnique" UNIQUE ("numConta")
);

CREATE TABLE "cliente"(
	"codigo" serial,
	"cpf" VARCHAR(14) NOT NULL,
	"nome" VARCHAR(100) NOT NULL,
	"email" VARCHAR(100) NOT NULL,
	CONSTRAINT "codigoPK" PRIMARY KEY ("codigo"));

INSERT INTO "cliente" ("cpf","nome","email") VALUES
('2327832','THAMY','thamy_cardoso@gmail.com')

INSERT INTO "conta" ("numConta", "agencia", "saldo","tipo","codigoCliente") VALUES
('9823712','12345', 10000, 'poupança', 1)
('0238929','56789', 500000, '21738129-34', 'Thamyris'),
('1293812','12345', 500, '912378917-45', 'Marcos');