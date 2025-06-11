import { Model } from "sequelize";

interface ISurveysStatus extends Model {
  loaded_at: string;
  status: string;
  count: number;
}

type TSurveysRequest = {
  createdAt: string;
  origin: string;
  limit: number;
  offset: number;
};

enum SurveyTypeRequest {
  STATUS = "STATUS",
  ORIGINS = "ORIGINS",
}

interface ISurveysRequest {
  createdAt?: { start?: string; end?: string };
  origin?: string;
  limit?: number;
  offset?: number;
  type?: SurveyTypeRequest;
}

type StatusData = {
  Aberto?: number;
  Pendente?: number;
  Valido?: number;
  Invalido?: number;
  Visualizou?: number;
  Incompleto?: number;
};

type ISurveysStatusResponse = {
  date: string;
  status: StatusData;
};

export {
  ISurveysStatus,
  TSurveysRequest,
  ISurveysRequest,
  ISurveysStatusResponse,
};
