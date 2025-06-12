const { createDefaultPreset } = require("ts-jest");

const tsJestTransformCfg = createDefaultPreset().transform;

/** @type {import("jest").Config} **/


module.exports = {
  collectCoverage: true,
  testEnvironment: "node",
  displayName: "Integration tests",
  testMatch: ["<rootDir>/tests/**/*.test.ts"],
  transform: {
    ...tsJestTransformCfg,
  },
  testPathIgnorePatterns: [
    "<rootDir>/node_modules/",
    "<rootDir>/tests/fixtures/",
  ],
  coverageDirectory: "<rootDir>/coverage",
  coverageReporters: ['clover', 'cobertura', 'lcov', 'text', 'text-summary'],
  coverageThreshold: {
    global: {
      lines: 90
    },
  },
};

