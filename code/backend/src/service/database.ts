import { Sequelize } from "sequelize-typescript";
const dbHost = process.env.DB_HOST || "localhost";
const dbHostPort = process.env.DB_HOST_PORT || 5432;
const dbUserName = process.env.DB_USER_NAME;
const dbUserPass = process.env.DB_USER_PASS;
const dbSchema = process.env.DB_SCHEMA || "inside";
const dbName = process.env.DB_NAME || "ilumeo";

const sequelizeSettings = new Sequelize({
  dialect: "postgres",
  host: dbHost as string,
  port: dbHostPort as number,
  username: dbUserName as string,
  password: dbUserPass as string,
  database: dbName as string,
  schema: dbSchema as string,
  pool: {
    max: 5,
    min: 0,
    acquire: 60000,
    idle: 10000,
  },
});

export { sequelizeSettings as sequelize };

const result = sequelizeSettings
  .authenticate()
  .then((res) => {
    console.log("Conectado ao banco de dados com sucesso.");
    return res;
  })
  .catch((error) => {
    console.error("Falha ao tentar conectar ao banco de dados: ", error);
  });
