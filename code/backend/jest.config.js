const { createDefaultPreset } = require("ts-jest");

const tsJestTransformCfg = createDefaultPreset().transform;

/** @type {import("jest").Config} **/


module.exports = {
  projects: [
    {
      testEnvironment: "node",
      displayName: "integration tests",
      testMatch: ["<rootDir>/tests/**/*.test.ts"],
      transform: {
        ...tsJestTransformCfg,
      },
      testPathIgnorePatterns: [
        "<rootDir>/node_modules/",
        "<rootDir>/tests/fixtures/",
      ],
      coverageDirectory: "<rootDir>/coverage",
    },
  ],
};

