import { defineConfig } from 'cypress';
import dotenvPlugin from 'cypress-dotenv';

export default defineConfig({
  e2e: {
    baseUrl: 'http://localhost:5173',
    setupNodeEvents(on, config) {
      const updatedConfig = dotenvPlugin(
        config,
        { path: '.env.development' },
        true
      );

      return updatedConfig;
    },
  },
});
