import api from "./api";

const API_HOST = process.env.API_HOST || "0.0.0.0";
const API_PORT = process.env.API_PORT || 8000;

const server = api.listen(API_PORT as number, API_HOST as string, (result) => {
  const address = server.address();
  console.log("API em excução em %s", address);
});
