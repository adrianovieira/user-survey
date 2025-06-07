import express from "express";
import cors from "cors";
import { healthRouter, surveysRouter } from "./routes";

const port = 8000;

const api = express();

const corsAllowedOrigins = ["http://localhost:3000"];

const corsOptions: cors.CorsOptions = {
  origin: corsAllowedOrigins,
};

api.use(express.json());
api.use(cors(corsOptions));

api.use(healthRouter);
api.use(surveysRouter);

export default api;
