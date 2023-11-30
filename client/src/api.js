import axios from "axios";

const axiosInstance = axios.create({
  baseURL: process.env.REACT_APP_API_URL,
  proxy: {
    host: process.env.REACT_APP_API_HOST,
    port: process.env.REACT_APP_API_PORT,
  },
});

export const analizeCode = async (code) => {
  return axiosInstance
    .post("/analizeCode", { code })
    .then((response) => response.data)
    .catch((error) => {
      if (error.response) {
        throw new Error(error.response.data);
      } else if (error.request) {
        console.log(error.request)
        throw new Error(error.request);
      } else {
        throw new Error("Error", error.message);
      }
    });
};
