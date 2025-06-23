
FROM node:22.14.0 AS build

WORKDIR /app

COPY package.json yarn.lock* package-lock.json* ./

# Install dependencies
RUN npm install

COPY . .

# Build the app for production
RUN npm run build

# Step 2: Serve the built app with a lightweight web server
FROM nginx:alpine

# Copy built files from the previous stage
COPY --from=build /app/dist /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start nginx server
CMD ["nginx", "-g", "daemon off;"]
