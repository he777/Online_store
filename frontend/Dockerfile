FROM node:12.2.0-alpine

# set working directory
RUN mkdir /frontend
WORKDIR /frontend

# add `/app/node_modules/.bin` to $PATH
ENV PATH /frontend/node_modules/.bin:$PATH

# install and cache app dependencies
COPY ./package*.json ./
RUN npm install --silent
RUN npm install react-scripts@3.0.1 -g --silent
COPY . .

# start app
CMD ["npm", "start"]
