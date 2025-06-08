import api from "./api";
import { databaseValidate } from "./service/database";

const API_HOST = process.env.API_HOST || "0.0.0.0";
const API_PORT = process.env.API_PORT || 8000;

// just to be in the safe side
databaseValidate();

const server = api.listen(API_PORT as number, API_HOST as string, (result) => {
  const address = server.address();
  console.log("API em excução em %s", address);
});
