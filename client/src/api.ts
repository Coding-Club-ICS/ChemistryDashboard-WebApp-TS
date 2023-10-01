import axios from "axios";

export const instance = axios.create({
  baseURL: "https://chemix-server.onrender.com/chem",
});

export default instance;