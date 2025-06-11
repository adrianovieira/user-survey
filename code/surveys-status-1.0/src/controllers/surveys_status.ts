import { UserSurveysModel } from "../models/database";
import {
  ISurveysRequest,
  ISurveysStatusResponse,
  ISurveysStatus,
} from "../models/surveys";
import Sequelize from "sequelize";
import { areEqualDates } from "../service/handlers";

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

    const result = await UserSurveysModel.findAll({
      attributes: ["loaded_at", "status", "count"],
      where,
      limit,
      offset,
      order: ["loaded_at"],
    });

    let dataResponse: ISurveysStatusResponse[] = [];
    if (result.length >= 1) {
      let dateLeft = new Date(result[0].loaded_at);
      let status: { [key: string]: any } = {};

      result.forEach((item) => {
        const row: ISurveysStatus = item.get();
        status[row.status] = row.count as number;
        const dateRigth = new Date(row.loaded_at);

        if (!areEqualDates(dateLeft, dateRigth)) {
          dataResponse.push({ date: dateLeft.toISOString(), status: status });
          status = {};
        }
        dateLeft = dateRigth;
      });
    }

    return JSON.parse(JSON.stringify(dataResponse)) as ISurveysStatusResponse;
  }
}

export { UserSurveysController };
