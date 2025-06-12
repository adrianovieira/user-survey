import { Sequelize } from "sequelize-typescript";

const dbHost = (process.env.DB_HOST || "localhost") as string;
const dbHostPort = (process.env.DB_HOST_PORT || 5432) as number;

const dbSchema = (process.env.DB_SCHEMA || "inside") as string;
const dbName = (process.env.DB_NAME || "iluminatti") as string;

const dbUserName = process.env.DB_USER_NAME as string;
const dbUserPass = process.env.DB_USER_PASS as string;

const sequelizeSettings = new Sequelize({
  dialect: "postgres",
  host: dbHost,
  port: dbHostPort,
  username: dbUserName,
  password: dbUserPass,
  database: dbName,
  schema: dbSchema,
  pool: {
    max: 5,
    min: 0,
    acquire: 60000,
    idle: 10000,
  },
});

function databaseValidate() {
  return sequelizeSettings
    .authenticate()
    .then((res) => {
      console.log("Conectado ao banco de dados com sucesso.");
      return true;
    })
    .catch((error) => {
      console.error("Falha ao tentar conectar ao banco de dados: ", error);
      return false;
    });
}

export { sequelizeSettings as sequelize, databaseValidate };
