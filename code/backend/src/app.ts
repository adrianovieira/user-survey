import api from "./api";

const API_HOST = process.env.API_HOST || "0.0.0.0";
const API_PORT = process.env.API_PORT || 8000;

api.set("port", API_PORT);
api.set("host", API_HOST);

api.listen(() => {
  console.log(`API is running on ${API_PORT} port.`);
});
