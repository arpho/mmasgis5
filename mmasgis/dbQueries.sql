SQLite format 3   @                                                                     -�    � t"^� �                                                                                                                                     �'�)tablemarchimarchiCREATE TABLE "marchi" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "query_id" INTEGER,
    "category" INTEGER,
    "marchio_id" INTEGER
)�6!!�7tablepotenzialipotenzialiCREATE TABLE "potenziali" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "query_id" INTEGER,
    "category" INTEGER,
    "potenziale_id" INTEGER
)�A))�=tableparametri_mmasparametri_mmasCREATE TABLE "parametri_mmas" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "query_id" INTEGER,
    "category" INTEGER,
    "parametro_id" INTEGER
)P++Ytablesqlite_sequencesqlite_sequenceCREATE TABLE sqlite_sequence(name,seq)�	�itablequeriesqueriesCREATE TABLE "queries" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "nome" TEXT,
    "descrizione" TEXT
)   � �                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              +testtest load query   � ����                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   !potenziali
marchi
)parametri_mmasqueries   � �                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           	  �   � �                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
m   � �                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
 |