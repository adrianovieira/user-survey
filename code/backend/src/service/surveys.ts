import { Request, Response } from "express";
import { UserSurveysController } from "../controllers/surveys_status";
import { IE001 } from "../models/errors";

class UserSurveysService {
  static get_surveys(req: Request, res: Response) {
    UserSurveysController.surveys_status(req.body)
      .then((data) => res.status(200).send(data))
      .catch((error) => {
        console.log(error);
        res.status(IE001.status).send(IE001.details);
      });
  }
}

export { UserSurveysService };
