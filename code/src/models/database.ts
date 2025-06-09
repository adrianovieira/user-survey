import { DataType } from "sequelize-typescript";
import { sequelize } from "../service/database";

const UserSurveysModel = sequelize.define(
  "UserSurveys",
  {
    loaded_at: { type: DataType.DATE, defaultValue: DataType.NOW },
    origin: { type: DataType.STRING(15) },
    status: { type: DataType.INTEGER },
    count: { type: DataType.INTEGER },
  },
  {
    tableName: "mv_survey_loaded_at_origin_status",
  }
);

export { UserSurveysModel };
