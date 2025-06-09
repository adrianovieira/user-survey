import request from "supertest";
import api from "../src/api";

const createdAtStart = new Date();
const createdAtEnd = new Date();

createdAtStart.setFullYear(createdAtStart.getFullYear() - 1);
createdAtEnd.setFullYear(createdAtEnd.getFullYear() + 1);

const fixtureSurveyFullDate = {
  createdAt: {
    start: createdAtStart,
    end: createdAtEnd,
  },
  limit: 100,
  offset: 1,
};

const fixtureSurveyStartDate = {
  createdAt: {
    start: createdAtStart,
  },
  limit: 100,
  offset: 1,
};

const fixtureSurveyEndDate = {
  createdAt: {
    end: createdAtEnd,
  },
  limit: 100,
  offset: 1,
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
