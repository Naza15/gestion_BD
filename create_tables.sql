CREATE TABLE Pasajeros (
    Pasajero_ID SERIAL PRIMARY KEY,
    Nombre VARCHAR(100),
    Direccion VARCHAR(255)
);

CREATE TABLE Vuelos (
    Vuelo_Numero VARCHAR(10) PRIMARY KEY,
    Vuelo_Fecha DATE
);

CREATE TABLE Checkins (
    Checkin_ID SERIAL PRIMARY KEY,
    Pasajero_ID INT REFERENCES Pasajeros(Pasajero_ID),
    Vuelo_Numero VARCHAR(10) REFERENCES Vuelos(Vuelo_Numero),
    Asiento VARCHAR(5),
    Estado_Checkin VARCHAR(20),
    Total_Fee DECIMAL(10, 2)
);
