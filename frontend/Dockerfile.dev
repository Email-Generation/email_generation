# Use an official Node runtime as a parent image
FROM node:18

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the package.json and package-lock.json files to the container
COPY package.json ./

# Install any needed packages specified in package.json
RUN npm install

# Copy all files from the current directory to the container's working directory
COPY . .

# Expose PORT 3000
EXPOSE 3000

# Specify a start command
CMD ["npm", "start"]
