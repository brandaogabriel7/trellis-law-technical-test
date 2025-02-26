# Stage 1: Build the application
FROM node:23.8.0-alpine AS builder

# Set the working directory
WORKDIR /app

# Copy the package.json and package-lock.json files
COPY package.json ./
COPY package-lock.json ./

# Install the dependencies
RUN npm install

# Copy the application code
COPY . .

# Build the application
RUN npm run build

# Stage 2: Serve the application
FROM node:23.8.0-alpine

# Set the working directory
WORKDIR /app

# Copy the built application
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/server.js ./server.js
COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/package-lock.json ./package-lock.json

# Install the production dependencies
RUN npm install --production

# Set the environment to production
ENV NODE_ENV=production

# Expose the port
EXPOSE 5173

# Start the application
CMD ["node", "server.js"]