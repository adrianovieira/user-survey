import { UserSurveys } from "../models/database";
import { ISurveysRequest } from "../models/surveys";
import Sequelize from "sequelize";

const { and, eq, gte, lte } = Sequelize.Op;

class UserSurveysController {
  static async surveys_status(body: ISurveysRequest) {
    let where: { [key: string]: any } = {};
    let createdAt, origin, limit, offset;
    if (body) {
      ({ createdAt, origin, limit, offset } = body);
      if (createdAt?.start && createdAt?.end) {
        where = {
          [and]: [
            { loaded_at: { [gte]: createdAt.start } },
            { loaded_at: { [lte]: createdAt.end } },
          ],
        };
      } else if (createdAt?.start) {
        where["loaded_at"] = { [gte]: createdAt.start };
      } else if (createdAt?.end) {
        where["loaded_at"] = { [lte]: createdAt.end };
      }

      if (origin) {
        where["origin"] = { [eq]: origin };
      }
    }

    const result = await UserSurveys.findAll({
      attributes: ["loaded_at", "origin", "status", "count"],
      where,
      limit,
      offset,
    });

    return result;
  }
}

export { UserSurveysController };
