import request from "supertest";
import api from "../src/api";

describe("API healty check", () => {
  it("GET /health should return a list of satus count", async () => {
    const response = await request(api).get("/health");

    expect(response.status).toBe(200);
    expect(JSON.stringify(response.body)).toBe(
      JSON.stringify({
        code: 0,
        message: "API funcionando.",
      })
    );
  });
});
