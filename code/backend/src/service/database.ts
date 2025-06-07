import { Sequelize } from "sequelize-typescript";
const dbHost = process.env.DB_HOST || "localhost";
const dbHostPort = process.env.DB_HOST_PORT || 5432;
const dbUserName = process.env.DB_USER_NAME;
const dbUserPass = process.env.DB_USER_PASS;
const dbSchema = process.env.DB_SCHEMA || "inside";
const dbName = process.env.DB_NAME || "ilumeo";

const sequelizeSettings = new Sequelize({
  dialect: "postgres",
  host: dbHost,
  port: dbHostPort as number,
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

export { sequelizeSettings as sequelize };
