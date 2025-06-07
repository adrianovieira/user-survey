type TSurveysStatus = {
  loadedAt: string;
  status: string;
  count: number;
};

type TSurveysStausList = TSurveysStatus[];

type TSurveysRequest = {
  createdAt: string;
  origin: string;
  limit: number;
  offset: number;
};

interface ISurveysRequest {
  createdAt?: { start?: string; end?: string };
  origin?: string;
  limit?: number;
  offset?: number;
}

export { TSurveysStausList, TSurveysStatus, TSurveysRequest, ISurveysRequest };
