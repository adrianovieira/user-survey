import request from "supertest";
import api from "../src/api";

const fixtureSurveyFullDate = {
  createdAt: {
    start: "2019-08-24T14:15:22Z",
    end: "2025-08-24T14:15:22Z",
  },
  origin: "wpp",
  limit: 100,
  offset: 1000,
};

const fixtureSurveyStartDate = {
  createdAt: {
    start: "2019-08-24T14:15:22Z",
  },
  origin: "wpp",
  limit: 100,
  offset: 1000,
};

const fixtureSurveyEndDate = {
  createdAt: {
    end: "2025-08-24T14:15:22Z",
  },
  origin: "wpp",
  limit: 100,
  offset: 1000,
};

describe("UserSurveys Controller should return a list of status count", () => {
  it("POST /surveys try it with full date", async () => {
    const response = await request(api)
      .post("/surveys")
      .send(fixtureSurveyFullDate);
    expect(response.status).toBe(200);
    expect(Array.isArray(response.body)).toBe(true);
  });

  it("POST /surveys try it with start date", async () => {
    const response = await request(api)
      .post("/surveys")
      .send(fixtureSurveyStartDate);
    expect(response.status).toBe(200);
    expect(Array.isArray(response.body)).toBe(true);
  });
  it("POST /surveys try it with end date", async () => {
    const response = await request(api)
      .post("/surveys")
      .send(fixtureSurveyEndDate);
    expect(response.status).toBe(200);
    expect(Array.isArray(response.body)).toBe(true);
  });
});
