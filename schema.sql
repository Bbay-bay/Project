-- Table User
CREATE TABLE User (
    id_user INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255),
    login VARCHAR(255) UNIQUE,
    password VARCHAR(255)
);

-- Table Client
CREATE TABLE Client (
    id_client INT PRIMARY KEY AUTO_INCREMENT,
    numero CHAR(10),
    id_user INT,
    FOREIGN KEY (id_user) REFERENCES User(id_user)
);

-- Table Commande
CREATE TABLE Commande (
    id_commande INT PRIMARY KEY AUTO_INCREMENT,
    reference INT,
    date DATE,
    id_client INT,
    FOREIGN KEY (id_client) REFERENCES Client(id_client)
);

-- Table Produit
CREATE TABLE Produit (
    id_produit INT PRIMARY KEY AUTO_INCREMENT,
    libelle VARCHAR(255),
    prix FLOAT
);

-- Table Lign_cmd (for many-to-many relationship between Commande and Produit)
CREATE TABLE Lign_cmd (
    id_lign_cmd INT PRIMARY KEY AUTO_INCREMENT,
    qte FLOAT,
    id_commande INT,
    id_produit INT,
    FOREIGN KEY (id_commande) REFERENCES Commande(id_commande),
    FOREIGN KEY (id_produit) REFERENCES Produit(id_produit)
);