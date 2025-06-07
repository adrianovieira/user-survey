import { Router } from "express";
import { surveysRouter } from "./surveys";

const healthRouter = Router();

healthRouter.get("/health", (req, res) => {
  res.status(200).send({ code: 0, message: "API funcionando." });
});

export { healthRouter, surveysRouter };
