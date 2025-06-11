import { DataType, Model } from "sequelize-typescript";
import { sequelize } from "../service/database";
import { ISurveysStatus } from "./surveys";

const UserSurveysModel = sequelize.define<ISurveysStatus>(
  "UserSurveys",
  {
    loaded_at: { type: DataType.DATE, defaultValue: DataType.NOW },
    origin: { type: DataType.STRING(15) },
    status: { type: DataType.INTEGER },
    count: { type: DataType.INTEGER },
  },
  {
    tableName: "mv_survey_loaded_at_status",
  }
);

export { UserSurveysModel };
