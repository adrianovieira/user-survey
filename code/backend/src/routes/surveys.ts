import { Router } from "express";
import { UserSurveysService } from "../service/surveys";

const surveysRouter = Router();

surveysRouter.post("/surveys", UserSurveysService.get_surveys);

export { surveysRouter };
